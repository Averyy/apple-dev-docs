# App Groups Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A list of identifiers specifying the groups your app belongs to.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- macOS 10.7+
- tvOS 9.0+
- watchOS 2.0+

#### Discussion

App groups allow multiple apps produced by a single development team to access shared containers and keychain access groups, and communicate using interprocess communication (IPC). Apps may belong to one or more app groups.

Format the identifier as follows:

```console
group.<group name>
```

Apple ensures that the group name you choose is unique when you register the app group on the Apple Developer website. For more information, see [`Register an app group`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-identifiers/register-an-app-group).

In macOS, you can also create app groups or add apps to existing app groups using this identifier format:

```console
<team identifier>.<group name>
```

You don’t need to register app groups that use this format on the Apple Developer website.

Apps within an app group share access to a group container. For more information about container creation, location, and deletion, see [`containerURL(forSecurityApplicationGroupIdentifier:)`](https://developer.apple.com/documentation/foundation/filemanager/1412643-containerurl).

Apps within a group can communicate with other members in the group using IPC mechanisms including Mach IPC, XPC, POSIX semaphores and shared memory, and UNIX domain sockets. In macOS, use app groups to enable IPC communication between two sandboxed apps, or between a sandboxed app and a nonsandboxed app. You use the app group identifier in the service identifier for your IPC mechanism, so keep these restrictions in mind when creating your app group identifier:

| IPC mechanism | Requirements |
| --- | --- |
| Mach IPC, XPC | The service name has the format `<group identifier>.<unique name>`. The maximum length of the service name is `BOOTSTRAP_MAX_NAME_LEN` characters. |
| POSIX semaphores | The service identifer has the format `<group identifier>/<unique name>`. The maximum length of the service identifier is `PSEMNAMLEN` characters. |
| POSIX shared memory | The service identifer has the format `<group identifier>/<unique name>`. The maximum length of the service identifier is `PSHMNAMLEN` characters. |
| UNIX domain sockets | The path to the socket needs to be in your app group container, and the name of the socket is limited to `SOCK_MAXADDRLEN` characters, which includes two bytes that are reserved for `sun_len` and `sun_family`. |

App groups that you register in your Apple Developer profile also act as keychain access groups. For more information about the relationship between app groups and keychain access groups, see [`Sharing access to keychain items among a collection of apps`](https://developer.apple.com/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps).

To add this entitlement to your app, enable the App Groups capability in Xcode, and add the groups your app belongs to.

## See Also

- [App Sandbox](../Security/app-sandbox.md)
  Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- [App Sandbox Entitlement](entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [com.apple.security.network.server](entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [com.apple.security.network.client](entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.
- [Camera entitlement](entitlements/com.apple.security.device.camera.md)
  A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](entitlements/com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](entitlements/com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](entitlements/com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](entitlements/com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.
- [Address book entitlement](entitlements/com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](entitlements/com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](entitlements/com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [com.apple.security.files.user-selected.read-only](entitlements/com.apple.security.files.user-selected.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](entitlements/com.apple.security.files.user-selected.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](entitlements/com.apple.security.files.downloads.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.application-groups)*