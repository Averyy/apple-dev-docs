# App Attest Environment

**Framework**: Bundle Resources  
**Kind**: typealias

The environment for an app that uses the App Attest service to validate itself.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

#### Discussion

To add this entitlement to your app, add the key to your app’s entitlements file manually, choose the `String` type, and set the associated value to either `development` or `production`. Alternatively, add the App Attest capability to your app target. This adds the entry to the app’s entitlements file with `development` as the associated value. If you omit the entitlement during development, your app uses the App Attest sandbox servers by default. You can test your app during development against the App Attest production servers by setting the entitlement to `production`.

After distributing your app through TestFlight, the App Store, or the Apple Developer Enterprise Program, your app ignores the entitlement you set and uses the production environment.

> ❗ **Important**:  If you use the App Attest service in an App Clip, be sure to add the App Attest capability and the corresponding entry for both your app and your App Clip. Similarly, if you use the App Attest service in your app and an app extension, make sure to configure the capability and the App Attest sandbox environment for both your app and your extension.

 If you use the App Attest service in an App Clip, be sure to add the App Attest capability and the corresponding entry for both your app and your App Clip. Similarly, if you use the App Attest service in your app and an app extension, make sure to configure the capability and the App Attest sandbox environment for both your app and your extension.

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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.devicecheck.appattest-environment)*