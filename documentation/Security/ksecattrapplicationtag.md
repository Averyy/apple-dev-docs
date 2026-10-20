# kSecAttrApplicationTag

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the item’s private tag.

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
let kSecAttrApplicationTag: CFString
```

```c
extern CFStringRef const kSecAttrApplicationTag;
```

## Mentions

- [Generating New Cryptographic Keys](./generating-new-cryptographic-keys.md)

#### Discussion

The corresponding value is of type [`CFData`](../CoreFoundation/cfdata.md) and contains private tag data.

On key creation, if not explicitly specified, this attribute defaults to `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrapplicationtag)*