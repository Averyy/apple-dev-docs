# kSecAttrCanEncrypt

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean that indicates whether the cryptographic key can be used for encryption.

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
let kSecAttrCanEncrypt: CFString
```

## Mentions

- [Using Keys for Encryption](using-keys-for-encryption.md)

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) and indicates whether this cryptographic key can be used to encrypt data.

On key creation, if not explicitly specified, this attribute defaults to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for private keys and [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for public keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcanencrypt)*