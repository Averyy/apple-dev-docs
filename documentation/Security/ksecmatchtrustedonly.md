# kSecMatchTrustedOnly

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean indicating whether untrusted certificates should be returned.

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
let kSecMatchTrustedOnly: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). If this attribute is provided with a value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), only certificates that can be verified back to a trusted anchor are returned. If this value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) or the attribute is not provided, then both trusted and untrusted certificates may be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchtrustedonly)*