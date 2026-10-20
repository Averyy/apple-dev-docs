# kSecPrivateKeyAttrs

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a dictionary of cryptographic key attributes specific to a private key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
let kSecPrivateKeyAttrs: CFString
```

```c
extern CFStringRef const kSecPrivateKeyAttrs;
```

## Mentions

- [Generating New Cryptographic Keys](./generating-new-cryptographic-keys.md)

#### Discussion

The corresponding value is a [`CFDictionary`](../CoreFoundation/cfdictionary.md) containing key-value pairs for attributes specific to the private key to be generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecprivatekeyattrs)*