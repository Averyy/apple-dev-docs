# App Sandbox

**Framework**: Security

Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.

#### Overview

App Sandbox provides protection to system resources and user data by limiting your app’s access to resources requested through entitlements.

> ❗ **Important**:  To distribute a macOS app through the Mac App Store, you must enable the App Sandbox capability.

## Topics

### Essentials
- [App Sandbox Entitlement](../BundleResources/Entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [Protecting user data with App Sandbox](protecting-user-data-with-app-sandbox.md)
  Guard user data and operating system resources from malicious attacks by limiting your app’s access to files, network connections, and hardware capabilities.
- [Embedding a command-line tool in a sandboxed app](../Xcode/embedding-a-helper-tool-in-a-sandboxed-app.md)
  Add a command-line tool to a sandboxed app’s Xcode project so the resulting app can run it as a helper tool.
- [Discovering and diagnosing App Sandbox violations](discovering-and-diagnosing-app-sandbox-violations.md)
  Determine when your macOS app behaves incorrectly because of a sandbox violation, and fix sandbox-related issues.
### Network
- [com.apple.security.network.server](../BundleResources/Entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [com.apple.security.network.client](../BundleResources/Entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.
### Hardware
- [Camera entitlement](../BundleResources/Entitlements/com.apple.security.device.camera.md)
  A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](../BundleResources/Entitlements/com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](../BundleResources/Entitlements/com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](../BundleResources/Entitlements/com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](../BundleResources/Entitlements/com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.
### App Data
- [Address book entitlement](../BundleResources/Entitlements/com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](../BundleResources/Entitlements/com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](../BundleResources/Entitlements/com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
### File Access
- [Accessing files from the macOS App Sandbox](accessing-files-from-the-macos-app-sandbox.md)
  Read and write documents and supporting files while maintaining security protection.
- [Migrating your app’s files to its App Sandbox container](migrating-your-app-s-files-to-its-app-sandbox-container.md)
  Simplify your app’s access to documents and supporting files.
- [com.apple.security.files.user-selected.read-only](../BundleResources/Entitlements/com.apple.security.files.user-selected.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](../BundleResources/Entitlements/com.apple.security.files.user-selected.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](../BundleResources/Entitlements/com.apple.security.files.downloads.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Downloads folder.
- [com.apple.security.files.downloads.read-write](../BundleResources/Entitlements/com.apple.security.files.downloads.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Downloads folder.
- [com.apple.security.assets.pictures.read-only](../BundleResources/Entitlements/com.apple.security.assets.pictures.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Pictures folder.
- [com.apple.security.assets.pictures.read-write](../BundleResources/Entitlements/com.apple.security.assets.pictures.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Pictures folder.
- [com.apple.security.assets.music.read-only](../BundleResources/Entitlements/com.apple.security.assets.music.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Music folder.
- [com.apple.security.assets.music.read-write](../BundleResources/Entitlements/com.apple.security.assets.music.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Music folder.
- [com.apple.security.assets.movies.read-only](../BundleResources/Entitlements/com.apple.security.assets.movies.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Movies folder.
- [com.apple.security.assets.movies.read-write](../BundleResources/Entitlements/com.apple.security.assets.movies.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Movies folder.
- [All files entitlement](../BundleResources/Entitlements/com.apple.security.files.all.md)
  A Boolean value that indicates whether the app may have access to all files.
- [NSAppDataUsageDescription](../BundleResources/Information-Property-List/NSAppDataUsageDescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/app-sandbox)*