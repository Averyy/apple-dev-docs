# kSecAttrKeyType

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s algorithm.

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
let kSecAttrKeyType: CFString
```

## Mentions

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)

#### Discussion

The corresponding value is of type [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) and indicates the algorithm associated with this cryptographic key. See [`Key Type Values`](item-attribute-keys-and-values#Key-Type-Values.md) for a list of valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrkeytype)*