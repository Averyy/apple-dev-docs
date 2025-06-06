# kSecAttrIsPermanent

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s permanence.

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
let kSecAttrIsPermanent: CFString
```

## Mentions

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) and indicates whether or not this cryptographic key or key pair should be stored in the default keychain at creation time.

On key creation, if not explicitly specified, this attribute defaults to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrispermanent)*