# kSecAttrCreator

**Framework**: Security  
**Kind**: var

A key with a value that indicates the item’s creator.

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
let kSecAttrCreator: CFString
```

#### Discussion

The corresponding value is of type [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) and represents the item’s creator. This number is the unsigned integer representation of a four-character code (for example, `'aCrt'`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcreator)*