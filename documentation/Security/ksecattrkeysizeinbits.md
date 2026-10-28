# kSecAttrKeySizeInBits

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the number of bits in a cryptographic key.

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
let kSecAttrKeySizeInBits: CFString
```

```c
extern CFStringRef const kSecAttrKeySizeInBits;
```

## Mentions

- [Generating New Cryptographic Keys](./generating-new-cryptographic-keys.md)

## Discussion

The corresponding value is of type [`CFNumber`](../CoreFoundation/cfnumber.md) and indicates the total number of bits in this cryptographic key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrkeysizeinbits)*