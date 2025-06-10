# init(accessControl:authenticationContext:)

**Framework**: Apple CryptoKit  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!, authenticationContext: LAContext? = nil) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa65/privatekey/init(accesscontrol:authenticationcontext:))*