# kSecAttrPort

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s port.

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
let kSecAttrPort: CFString
```

#### Discussion

The corresponding value is of type [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) and represents an Internet port number. Items of class [`kSecClassInternetPassword`](ksecclassinternetpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrport)*