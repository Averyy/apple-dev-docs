# kSecAttrGeneric

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s user-defined attributes.

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
let kSecAttrGeneric: CFString
```

#### Discussion

The corresponding value is of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) and contains a user-defined attribute. Items of class [`kSecClassGenericPassword`](ksecclassgenericpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrgeneric)*