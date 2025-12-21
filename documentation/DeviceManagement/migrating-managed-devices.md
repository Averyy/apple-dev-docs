# Migrating managed devices

**Framework**: Device Management

Migrate managed devices from one device management service to another.

#### Overview

Apple School Manager and Apple Business Manager support device management migration to transfer management of a device from one service, the original, to another, the destination, using a simple and reliable process.

Some reasons for migrating include: replacing one service product with a different one, creating a separate pool of managed devices for testing a new version of a service, or incorporating devices from another organization, for example, as the result of an acquisition.

Migration typically involves either erasing a device and enrolling it with the destination service, or manually unenrolling and then reenrolling with the destination service. These operations require significant organization support to guide users through the process, and are disruptive, taking significant time to complete.

The Apple School Manager and Apple Business Manager migration process simplifies and improves the experience for admins, support personnel, and users. An overview of the order of operations for this process is as follows:

1. An admin reassigns a managed device from the original device management service to the destination service in Apple School Manager or Apple Business Manager.
2. The admin sets a deadline for enforcing the migration on the device.
3. The destination service detects a new device in its device assignment list and assigns an Automated Device Enrollment [`Profile`](profile.md) to the device.
4. Apple School Manager or Apple Business Manager updates the [`Profile`](profile.md) assigned to the device to include the migration deadline, and sends a push notification to the device to have it fetch the new profile.
5. When it receives the new [`Profile`](profile.md), the device detects the need for migration and prompts the user with a notification that shows the required deadline, and gives them an option to start migration immediately or postpone it.
6. If the user postpones migration, the device repeats the notification daily or more frequently close to the deadline. If the user keeps postponing the migration, the device forces migration when it reaches the deadline.
7. When the user triggers migration, or when the device reaches the deadline, it starts the migration flow, and displays progress as it unenrolls from the original service and reenrolls with the destination service.
8. When migration is complete, the device is ready to use and the destination service manages it.

The requirements for Apple School Manager and Apple Business Manager migration are:

- The device needs to have iOS 26 or later, or macOS 26 or later.
- The admin needs to assign the device to Apple School Manager or Apple Business Manager.
- The device needs to use Automated Device Enrollment.
- An iOS device can migrate only if the device management service specified by Automated Device Enrollment still manages it. If the device unenrolls and then reenrolls in the same or a different service, it can’t use the migration flow.
- A macOS device can migrate if any device management service manages it, including when it unenrolls from the original Automated Device Enrollment service and reenrolls with the same or a different service, provided the new enrollment is a profile-driven device enrollment.

#### Handle Migration in the Original Device Management Service

The original device management service doesn’t need to take any special actions when migration occurs. Apple School Manager or Apple Business Manager removes the device from the original service’s [`Device Assignment`](device-assignment.md), which the original service detects when it next synchronizes that list. When migration starts, the original service receives a [`Check Out`](check-out.md) request from the device, indicating unenrollment of the device.

> **Note**:  The device sends the [`Check Out`](check-out.md) request on a best-effort basis, and the device management service may not always receive it. The service needs to handle previously enrolled devices that no longer respond to requests.

#### Handle Migration in the Destination Device Management Service

Apple School Manager or Apple Business Manager adds the migrating device to the [`Device Assignment`](device-assignment.md) for the destination device management service. It includes a `mdm_migration_deadline` field in the device record, indicating the timestamp of the migration deadline, and this tells the destination service that the next enrollment from the device is due to a migration.

> ❗ **Important**:  The device management service needs to set the `X-Server-Protocol-Version` header to version 8 or later in the Apple School Manager or Apple Business Manager HTTP request, to ensure device records include the `mdm_migration_deadline` field.

When the destination device management service detects a migrating device, it assigns a [`Profile`](profile.md) to the device using the [`Assign a Profile`](assign-profile.md) request. Apple School Manager or Apple Business Manager then updates the corresponding device with the new [`Profile`](profile.md), starting the migration flow.

The destination device management service also needs to set the `await_device_configured` key to `true` in the device’s [`Profile`](profile.md). This allows the destination service to preserve Activation Lock and managed apps before the device is available again to the user.

> **Note**:  The admin can cancel the migration before it starts, reverting the device to the original device management service, and cancelling migration prompts on the device.

##### Preserve Activation Lock

Activation Lock is a feature of iCloud and Automated Device Enrollment that makes it harder for anyone to use or resell a lost or stolen device. Device management services can set Activation Lock by using the Apple School Manager or Apple Business Manager [`Activation Lock a Device`](activation-lock-devices.md) request. Users can also set their own Activation Lock via iCloud if allowed by the service.

For device migration, the following rules apply for Activation Lock:

- If the original service has a lock on the device before migration, the migration process always removes that lock and invalidates any bypass codes.
- The destination service can opt to lock the device during migration, or leave it unlocked.
- If migration fails, Apple School Manager or Apple Business Manager removes any prior lock and invalidates any bypass codes, and then applies a lock on the device that only the admin can unlock.

If the destination device management service wants to apply Activation Lock during migration, before migration starts, it assigns an [`Profile`](profile.md) with the `await_device_configured` key with a value of `true` to the device, to ensure the device enters the await configuration state during migration. Then, after the device enrolls and enters the await configuration state, it sends a [`Activation Lock a Device`](activation-lock-devices.md) request to Apple School Manager or Apple Business Manager to lock the device, before it sends the [`Device Configured`](device-configured-command.md) command to allow the device to proceed.

##### Preserve Managed Apps

During migration, a device management service can preserve managed apps on iOS devices. Normally, devices remove managed apps and their local data when unenrolling from a service, which happens when the device starts migrating. If the admin wants users to have the same set of managed apps after migration as they had before migration, then preserving apps during migration ensures no data loss and a quicker migration because the device doesn’t need to download previously installed managed apps.

The app preservation behavior works for apps installed using MDM commands such as [`Install Application`](install-application-command.md), or declarative management using [`AppManaged`](appmanaged.md) declarations. To support this, the following occurs:

1. Before migration starts, the destination device management service assigns a [`Profile`](profile.md) with the `await_device_configured` key with a value of `true` to the device, to ensure the device enters the await configuration state during migration.
2. When migration starts, the device stores the list of currently managed apps before unenrolling from the original service. Then, when the device unenrolls, it ensures the system doesn’t delete the previously managed apps.
3. After the device enrolls and enters the await configuration state,  before sending the [`Device Configured`](device-configured-command.md) command, the destination service installs MDM or declarative management apps it wants preserved. The device won’t download these apps again. It also installs any other apps, profiles, or declarations needed for setup. The device downloads any new apps, but the download and install operations happen in the background, allowing the migration to continue.
4. When migration completes, the device compares the new set of managed apps with the preserved list from the original service, and removes any apps in the preserved list that weren’t reinstalled by the destination service.

> **Note**:  The destination device management service needs to ensure each preserved App Store app has a valid App Store license assigned to it in Apple School Manager or Apple Business Manager.

#### Handle Multiple Users When Migrating Macos Devices

MacOS devices can have multiple user accounts. When a device management service manages a device, if it includes the value `com.apple.mdm.per-user-connections` in the `ServerCapabilities` key in its [`MDM`](mdm.md) profile payload, then it can also manage a single user account on the device. That applies to local and network user accounts on the device. The following rules apply when migrating macOS devices:

- If there’s a managed local user prior to migration, the device can start migration only when that user is signed in, with either the user triggering migration themselves or the device triggering migration when it reaches the deadline. After migration, if the destination service supports managing users, then it manages the same local user that was managed before.
- If there’s a managed local user, but they aren’t signed in, the device notifies other signed-in users about the migration, but they can’t trigger migration themselves, and the device can’t trigger migration when it reaches the deadline. Instead, the device advises the nonmanaged user that the managed local user needs to sign in to start migration.
- If there’s no managed local user prior to migration, the device allows any user to trigger migration or proceed with migration when it reaches the deadline. After migration, if the destination service supports managing users, then it manages the user that was signed in at the time of migration.

#### Ensure the Filevault Recovery Key Resets

If the original device management service sets a FileVault Full Disk Encryption recovery key by installing a `com.apple.security.FDERecoveryKeyEscrow` profile payload, that key remains on the device after migration until the destination service sends its own `com.apple.security.FDERecoveryKeyEscrow` profile payload. If this happens, the device creates a new recovery key. To achieve optimal security, the destination service needs to install the `com.apple.security.FDERecoveryKeyEscrow` profile payload during the await configuration state.

> **Note**:  The destination device management service needs to support the bootstrap token management feature in order to create a new recovery key.

## See Also

- [Implementing Device Management](implementing-device-management.md)
  Set up an MDM server and send commands to managed devices.
- [Commands and Queries](commands-and-queries.md)
  Manage the configuration and behavior of your devices.
- [Check-in](check-in.md)
  Authenticate devices and maintain push tokens with these commands.
- [Account-driven enrollment](account-driven-enrollment.md)
  Authenticate devices using a user identity-focused workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/migrating-managed-devices)*