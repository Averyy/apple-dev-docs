# kSecAttrProtocol

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the item’s protocol.

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
let kSecAttrProtocol: CFString
```

```c
extern CFStringRef const kSecAttrProtocol;
```

## Mentions

- [Adding a password to the keychain](./adding-a-password-to-the-keychain.md)

#### Discussion

The corresponding value is of type [`CFString`](../CoreFoundation/cfstring.md) and denotes the protocol for this item (see [Protocol Values](./item-attribute-keys-and-values.md#Protocol-Values)). Items of class [`kSecClassInternetPassword`](./ksecclassinternetpassword.md) have this attribute.

> **Note**:  For compatibility with earlier Keychain APIs, functions in [Keychain services](./keychain-services.md) accept a [`CFNumber`](../CoreFoundation/cfnumber.md) for the protocol. The number is a 32-bit integer that encodes the protocol value as a `FourCharCode`. In your code, use a [`CFString`](../CoreFoundation/cfstring.md) with one of the values from [Protocol Values](./item-attribute-keys-and-values.md#Protocol-Values) instead of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrprotocol)*