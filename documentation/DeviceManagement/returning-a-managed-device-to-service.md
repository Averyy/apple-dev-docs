# Returning a managed device to service

**Framework**: Device Management

Use a device management service to return managed devices to service quickly after use.

#### Overview

Organizations often have managed devices that multiple people use, such as shift workers who pick up, use, and return devices. When a person returns a device, the device management service needs to reset it to erase any data associated with that person, ensuring a clean device for the next person. The service sends an [`Erase Device`](erase-device-command.md) command to reset the device, causing it to erase and return to the Setup Assistant screen for a new device. In some cases, the user or the device can directly trigger the return to service.

A device management service uses the [`Erase Device`](erase-device-command.md) command in three ways:

> **Note**:  When using the return-to-service with app preservation flow, the device preserves only the app executable data during the erase, and always erases all locally stored user-generated data for the app.

The two return-to-service flows automate and speed up resetting and reenrolling devices. The app preservation flow is optimized for users needing managed apps. The standard return-to-service flow is available for iOS, iPad OS, tvOS, and visionOS devices. The return-to-service with app preservation flow is available for iOS, iPad OS, and visionOS devices.

#### Return a Device to Service

The device management service uses the [`Erase Device`](erase-device-command.md) command to trigger the standard return-to-service flow for any device with a device enrollment. The service includes additional properties in the command to automatically reenroll the device after the erase operation completes, as the “Trigger return to service” section below discusses. After a device erases itself, the following sequence of operations occurs:

1. The device enters Setup Assistant.
2. The device automatically joins the Wi-Fi network specified by the device management service, if present.
3. The device automatically enrolls with the device management service specified by the device management service if present, or the service specified in its Automated Device Enrollment [`Profile`](profile.md).
4. The device proceeds through Setup Assistant (without requiring user interaction on iOS, and with a minimum required interaction on visionOS), entering and exiting the await configuration state that the device management service controls.
5. The device exits Setup Assistant and is ready to use.
6. If the device management service triggers the standard return-to-service flow again, the device erases itself and returns to step 1 in this sequence.

##### Trigger Return to Service

The device management service triggers each return-to-service flow by setting the `ReturnToService` key in the [`Erase Device`](erase-device-command.md) command it sends. This key contains a dictionary with the following keys:

| Key | Type | Content |
| --- | --- | --- |
| `Enabled` | Boolean | (Required) The key that, if `true`, prompts the device to use a return-to-service flow after erasure |
| `MDMProfileData` | Data | (Optional) The enrollment profile the device installs after erasure when `Enabled` is `true` |
| `WiFiProfileData` | Data | (Optional) The Wi-Fi profile the device installs after erasure when `Enabled` is `true` |
| `BootstrapToken` | Data | (Optional) The bootstrap token the device needs to erase itself when `Enabled` is `true` and it’s preserving apps |

The device management service sets the `Enabled` key to `true` in the [`Erase Device`](erase-device-command.md) command to ensure a return-to-service flow after the erase. The service deactivates any Activation Lock on the device before it sends the command. If the device has an Activation Lock, a user needs to be present during the Setup Assistant flow to activate it, which prevents a fully automatic return-to-service flow.

If the device only has a Wi-Fi connection, the device management service sets the `/WiFiProfileData` key in the [`Erase Device`](erase-device-command.md) command to a value that’s a Base64-encoded profile with a [`WiFi`](wifi.md) payload. The device uses this key to join a Wi-Fi network and connect to the device management service to automatically enroll.

The device management service sets the `MDMProfileData` key in the [`Erase Device`](erase-device-command.md) command for the following situations:

- The device isn’t using Automated Device Enrollment. The device needs the enrollment profile to automatically reenroll.
- The device is using Automated Device Enrollment and the [`Profile`](profile.md) contains a `configuration-web-url` key. The device needs the enrollment profile to automatically reenroll by bypassing the sign-in flow, which the `configuration-web-url` key normally triggers.
- The device is using Automated Device Enrollment and the [`Profile`](profile.md) contains a `url` key for an HTTP endpoint requiring HTTP authentication to fetch the enrollment profile. The device needs the enrollment profile to bypass this authentication flow and automatically reenroll.

The value of the `MDMProfileData` key needs to be a Base64-encoded profile with an [`MDM`](mdm.md) payload and any other necessary payloads.

The device management service only sets the `BootstrapToken` key in the [`Erase Device`](erase-device-command.md) command when using the return-to-service with app preservation flow.

#### Return a Device to Service and Preserve Apps

The first time through the return-to-service with app preservation flow, the device downloads and installs managed apps that the device management service requires, and takes a snapshot of the system data volume. For subsequent times, after erasure, the device restores the last snapshot and doesn’t need to download the managed apps present in the snapshot, if the device management service reinstalls them. However, it does have to download other managed apps that the device management service adds.

The return-to-service with app preservation flow requires a device using Automated Device Enrollment. The device management service sets the `is_return_to_service` key to `true` in the [`Profile`](profile.md) for the device to ensure app preservation. When that key is set, the device always assumes the value of the `await_device_configured` key in the [`Profile`](profile.md) is `true`. This ensures the device enters the await configuration state, causing it to wait for the service to indicate when it can proceed. The service can then provision the device with an appropriate management state by sending commands before a user can access it. The service uses the await configuration state for app preservation as described below.

After the device first enrolls with the device management service, it sends its bootstrap token to the service using the [`Set Bootstrap Token`](set-bootstrap-token.md) check-in request. The service persists the bootstrap token and returns it when needed. The device can preserve apps only when it receives the bootstrap token from the service. Without the bootstrap token, the device performs a standard return-to-service flow without app preservation.

There are three ways to trigger the return-to-service with app preservation flow on the device:

- Service triggered: The device management service sends a [`Erase Device`](erase-device-command.md) command.
- User triggered: The user triggers return to service on the device (visionOS only).
- Device triggered: The device triggers return to service when it’s idle for a set amount of time (visionOS only).

##### Trigger a Device From the Device Management Service

The device management service uses the [`Erase Device`](erase-device-command.md) command to trigger the device. The command has the same requirements as the standard return-to-service flow, described in the “Trigger return to service” section above, with the additional requirement that the `BootstrapToken` key is present and set to the bootstrap token value the device previously sent. When the device receives the command, it uses the bootstrap token to erase user data while preserving system data, including managed apps.

##### Handle the User Trigger

On visionOS devices, a person can trigger the return-to-service with app preservation flow from the lock screen or control center. When they trigger the device, it sends a [`Return To Service`](return-to-service.md) check-in request to the device management service. The service includes a `ReturnToService` key in the [`ReturnToServiceResponse`](returntoserviceresponse.md) response, with that key matching the `ReturnToService` key in the [`Erase Device`](erase-device-command.md) command. When the device processes the response, it uses the bootstrap token to erase user data while preserving system data, including managed apps.

##### Handle the Device Trigger

On visionOS devices, a device can trigger the return-to-service with app preservation flow when it’s idle for a set amount of time. To set a timeout, the device management service sends a [`Settings`](settings-command.md) command with a `SharedDeviceConfiguration` object that contains the `TemporarySessionTimeout` key, and sets the value to the required timeout in seconds. The device doesn’t trigger an idle timeout if the value is zero or the setting isn’t present. When the device triggers the idle timeout, it uses the [`Return To Service`](return-to-service.md) check-in request to start the return-to-service flow, as the previous section describes.

##### Preserve Apps

When the device uses the return-to-service with app preservation flow, after erasure, the following sequence of operations occurs:

1. The device enters Setup Assistant.
2. If it’s not the first time through the flow, the device restores the last snapshot it took. If a snapshot exists, it contains the device management service enrollment and any managed apps that were present when it took the snapshot.
3. The device saves a list of any managed apps that are present.
4. The device unenrolls from any device management service that is present, without removing managed apps.
5. The device joins the Wi-Fi network if the server set it prior to the erasure.
6. The device enrolls with the device management service using the enrollment profile the server set during erasure, or using the Automated Device Enrollment [`Profile`](profile.md) to fetch an enrollment profile.
7. The device enters the await configuration state.
8. The device management service uses MDM commands or declarative management to provision the device, including any managed apps it wants preserved for the next time it triggers the flow. The device doesn’t have to download apps that it preserved in the previous snapshot.
9. The device management service sends the [`Device Configured`](device-configured-command.md) command to exit the await configuration state.
10. The device immediately responds to the command, but doesn’t proceed through Setup Assistant.
11. The device pauses processing of device management commands, responding with `NotNow` if it receives any further commands.
12. The device waits for all provisioned, but not preserved, managed apps to download and install.
13. The device removes apps in the saved list that aren’t reinstalled.
14. The device takes a snapshot of the system data volume, including the new set of managed apps.
15. The device reenables processing of device management service commands. If it previously sent `NotNow`, it sends `Idle` to indicate readiness.
16. The device automatically proceeds through Setup Assistant without requiring user interaction, except in visionOS, where the device requires the user to step through only the Setup Assistant screens that calibrate the headset.
17. The device exits Setup Assistant and is ready to use.
18. If an action triggers the flow again, the device erases itself and returns to step 1.

> **Note**:  If the device management service installs managed apps after the device takes the snapshot (after step 14), those apps aren’t preserved for the next return-to-service with app preservation cycle. The device management service can reinstall the apps in step 8 during the next cycle to preserve them for subsequent cycles, but the device needs to download them again to include them in the next snapshot.

##### Handle Software Updates

The device disables software updates — both automatic and user-initiated — when the return-to-service with app preservation state is active because the device effectively reverts any OS update when restoring the snapshot taken in step 14 above.

The device management service can trigger a software update by returning the [`ErrorCodeSoftwareUpdateRequired`](errorcodesoftwareupdaterequired.md) HTTP 403 error code during enrollment in step 6 if using the service that its [`Profile`](profile.md) specifies. In that case, the device does a software update, then reboots to restart the flow. Otherwise, a software update is possible only by turning off the return-to-service with app preservation flow.

##### Allow Visionos Devices to Join Wi Fi on Reboot

When a person finishes using an Apple Vision Pro device, they remove the headset and then often disconnect the device from its power source. When the next user picks up the device to use it, it does a “cold” boot when powered on and remains locked to the previous user. In order for the new user to trigger the return-to-service flow from the lock screen, the device needs to be on a Wi-Fi network so it can send requests to the device management service. However, after a cold boot, the device isn’t connected to Wi-Fi, preventing the new user from triggering the return-to-service flow.

To work around this situation, the device management service can install a [`WiFi`](wifi.md) payload on the device, and set the payload’s `AllowJoinBeforeFirstUnlock` key to `true` to allow the device to join that Wi-Fi network automatically after a cold boot. The following conditions apply when using the `AllowJoinBeforeFirstUnlock` key:

- The device supports it only when in the return-to-service with app preservation mode.
- The device allows it in only one Wi-Fi payload.
- The Wi-Fi payload can’t include the `EAPClientConfiguration` key.
- The Wi-Fi payload’s `IsHotspot` key needs to be set to `false` or not be present.
- The Wi-Fi payload can’t include the `QoSMarkingPolicy` key.
- The Wi-Fi payload’s `ProxyType` key needs to be set to `None` or not be present.

When these conditions apply, the device places any Wi-Fi network credentials into Class D storage in its keychain, and it stores any other Wi-Fi network details in a file using Class D storage. The device makes items in Class D storage available after the cold boot, before first unlock. Thus the device uses those details to join the Wi-Fi network before first unlock.

To use this mechanism, the device management service needs to install this Wi-Fi profile in each cycle of return to service. The best time to install the profile is during the await configuration state, before the next user starts accessing the device.

## See Also

- [Managing MDM Devices and Users in macOS](managing-mdm-devices-and-users-in-macos.md)
  Manage devices and users as separate entities in macOS.
- [Enabling Network and Mobile User Logins](enabling-network-and-mobile-user-logins.md)
  Manage network users on macOS devices bound to an Open Directory server, and mobile users on shared iPads.
- [Managing Passcodes](managing-passcodes.md)
  Ensure data security by managing device passcodes and compliance with policies.
- [Dealing with Inactive MDM Devices and Invalid Push Tokens](dealing-with-inactive-mdm-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/returning-a-managed-device-to-service)*