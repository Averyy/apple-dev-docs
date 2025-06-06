# kSecAttrServer

**Framework**: Security  
**Kind**: var

A key whose value is a string indicating the item’s server.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrServer: CFString
```

## Mentions

- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and contains the server’s domain name or IP address. Items of class [`kSecClassInternetPassword`](ksecclassinternetpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrserver)*