# kSecAttrApplicationLabel

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s application label.

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
let kSecAttrApplicationLabel: CFString
```

#### Discussion

The corresponding value is of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) and contains a label for this item. This attribute is different from the [`kSecAttrLabel`](ksecattrlabel.md) attribute, which is intended to be human-readable. Instead, this attribute is used to look up a key programmatically; in particular, for keys of class [`kSecAttrKeyClassPublic`](ksecattrkeyclasspublic.md) and [`kSecAttrKeyClassPrivate`](ksecattrkeyclassprivate.md), the value of this attribute is the hash of the public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrapplicationlabel)*