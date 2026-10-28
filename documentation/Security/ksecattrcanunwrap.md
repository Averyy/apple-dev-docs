# kSecAttrCanUnwrap

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean that indicates whether the cryptographic key can be used for unwrapping.

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
let kSecAttrCanUnwrap: CFString
```

```c
extern CFStringRef const kSecAttrCanUnwrap;
```

## Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md) and indicates whether this cryptographic key can be used to unwrap another key.

On key creation, if not explicitly specified, this attribute defaults to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for private keys and [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for public keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcanunwrap)*