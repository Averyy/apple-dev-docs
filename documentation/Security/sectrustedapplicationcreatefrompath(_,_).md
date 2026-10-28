# SecTrustedApplicationCreateFromPath(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a trusted app instance based on the app at the given path in the file system.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<CChar>?, _ app: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus
```

```c
OSStatus SecTrustedApplicationCreateFromPath(const char *path, SecTrustedApplicationRef*app);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

Use this method to create a trusted app instance, which both identifies an app and provides data that can be used to ensure that the app hasn’t been altered since the instance was created.

You can use the created instance as input to the [`SecAccessCreate(_:_:_:)`](./secaccesscreate%28_,_,_%29.md) method, which creates an access instance. The access instance, in turn, is used as input to the [`SecKeychainItemSetAccess(_:_:)`](./seckeychainitemsetaccess%28_,_%29.md) function to specify the set of apps that are trusted to access a specific keychain item.

## Parameters

- `path`: The path to the app to trust. For application bundles, use the path to the bundle directory. Pass `nil` to refer to the calling app.
- `app`: On return, points to the newly created trusted app instance. Call the [`CFRelease`](../CoreFoundation/cfrelease.md) method to release this instance when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustedapplicationcreatefrompath(_:_:))*