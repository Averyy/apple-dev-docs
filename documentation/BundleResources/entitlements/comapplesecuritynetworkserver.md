# com.apple.security.network.server

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app may listen for incoming network connections.

**Availability**:
- macOS 10.7+

#### Discussion

Use this key to allow other computers to initiate network connections to your sandboxed app.

> **Note**:  For TCP sockets, the `com.apple.security.network.server` and [`com.apple.security.network.client`](entitlements/com.apple.security.network.client.md) entitlements restrict only the initiation of a network connection, not the flow of data. Outgoing and incoming connections can both send and receive data. For UDP sockets, the network entitlements restrict both initiation and data flow. For example, an app with only the server entitlement enabled can receive, but not send, data. Apps using UDP usually require both entitlements.

 For TCP sockets, the `com.apple.security.network.server` and [`com.apple.security.network.client`](entitlements/com.apple.security.network.client.md) entitlements restrict only the initiation of a network connection, not the flow of data. Outgoing and incoming connections can both send and receive data.

For UDP sockets, the network entitlements restrict both initiation and data flow. For example, an app with only the server entitlement enabled can receive, but not send, data. Apps using UDP usually require both entitlements.

To add this entitlement to your app, enable the App Sandbox capability in Xcode, and under Network, select Incoming Connections (Server).

## See Also

- [App Sandbox](../Security/app-sandbox.md)
  Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- [App Sandbox Entitlement](entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
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
- [com.apple.security.files.downloads.read-write](entitlements/com.apple.security.files.downloads.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.network.server)*