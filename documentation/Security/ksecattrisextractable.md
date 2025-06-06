# kSecAttrIsExtractable

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s extractability.

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
let kSecAttrIsExtractable: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) and indicates whether the item can be exported from its keychain. Items of class [`kSecClassKey`](ksecclasskey.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrisextractable)*