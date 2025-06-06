# kSecAttrCanDerive

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean that indicates whether the cryptographic key can be used for derivation.

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
let kSecAttrCanDerive: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) and indicates whether this cryptographic key can be used to derive another key.

On key creation, if not explicitly specified, this attribute defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcanderive)*