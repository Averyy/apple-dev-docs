# kSecAttrAuthenticationType

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the item’s authentication scheme.

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
let kSecAttrAuthenticationType: CFString
```

```c
extern CFStringRef const kSecAttrAuthenticationType;
```

## Discussion

The corresponding value is of type [`CFString`](../CoreFoundation/cfstring.md) and denotes the authentication scheme for this item (see [Authentication Type Values](./item-attribute-keys-and-values.md#Authentication-Type-Values)).

> **Note**:  For compatibility with earlier Keychain APIs, functions in [Keychain services](./keychain-services.md) accept a [`CFNumber`](../CoreFoundation/cfnumber.md) for the authentication scheme. The number is a 32-bit integer that encodes the authentication scheme as a `FourCharCode`. In your code, use a [`CFString`](../CoreFoundation/cfstring.md) with one of the values from [Authentication Type Values](./item-attribute-keys-and-values.md#Authentication-Type-Values) instead of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrauthenticationtype)*