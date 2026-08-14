# kSecAttrIsSensitive

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s sensitivity.

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
let kSecAttrIsSensitive: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/corefoundation/cfboolean). When set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/corefoundation/kcfbooleantrue), the item can only be exported in an encrypted format. Items of class [`kSecClassKey`](ksecclasskey.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrissensitive)*