# kSecAttrCanDecrypt

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean that indicates whether the cryptographic key can be used for decryption.

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
let kSecAttrCanDecrypt: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) and indicates whether this cryptographic key can be used to decrypt data.

On key creation, if not explicitly specified, this attribute defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for private keys and [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for public keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcandecrypt)*