# kSecAttrType

**Framework**: Security  
**Kind**: var

A key with a value that indicates the item’s type.

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
let kSecAttrType: CFString
```

#### Discussion

The corresponding value is of type [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) and represents the item’s type. This number is the unsigned integer representation of a four-character code (for example, ‘aTyp’).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrtype)*