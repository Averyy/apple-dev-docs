# kSecAttrService

**Framework**: Security  
**Kind**: var

A key whose value is a string indicating the item’s service.

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
let kSecAttrService: CFString
```

#### Discussion

The corresponding value is a string of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) that represents the service associated with this item. Items of class [`kSecClassGenericPassword`](ksecclassgenericpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrservice)*