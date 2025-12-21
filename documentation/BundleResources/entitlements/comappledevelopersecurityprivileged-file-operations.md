# Privileged File Operations

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that permits apps to create symbolic links, replace files, and set file attributes.

**Availability**:
- macOS 10.15+

#### Discussion

Add this entitlement to your app before you call [`requestAuthorization(to:completionHandler:)`](https://developer.apple.com/documentation/AppKit/NSWorkspace/requestAuthorization(to:completionHandler:)) to request permission to perform privileged file operations. If someone grants your app permission, pass the authorization you receive to [`init(authorization:)`](https://developer.apple.com/documentation/Foundation/FileManager/init(authorization:)) and use the [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) you create to perform the operation.

To request this entitlement for your app, [`fill out the request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/privileged-file-operations/).

## See Also

- [App Sandbox Entitlement](entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [com.apple.security.files.user-selected.read-only](entitlements/com.apple.security.files.user-selected.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](entitlements/com.apple.security.files.user-selected.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](entitlements/com.apple.security.files.downloads.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Downloads folder.
- [com.apple.security.files.downloads.read-write](entitlements/com.apple.security.files.downloads.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Downloads folder.
- [com.apple.security.assets.pictures.read-only](entitlements/com.apple.security.assets.pictures.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Pictures folder.
- [com.apple.security.assets.pictures.read-write](entitlements/com.apple.security.assets.pictures.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Pictures folder.
- [com.apple.security.assets.music.read-only](entitlements/com.apple.security.assets.music.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Music folder.
- [com.apple.security.assets.music.read-write](entitlements/com.apple.security.assets.music.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Music folder.
- [com.apple.security.assets.movies.read-only](entitlements/com.apple.security.assets.movies.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Movies folder.
- [com.apple.security.assets.movies.read-write](entitlements/com.apple.security.assets.movies.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Movies folder.
- [All files entitlement](entitlements/com.apple.security.files.all.md)
  A Boolean value that indicates whether the app may have access to all files.
- [Data Protection Entitlement](entitlements/com.apple.developer.default-data-protection.md)
  The level of data protection for sensitive user data when an app accesses it on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.security.privileged-file-operations)*