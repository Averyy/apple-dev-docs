# kSecAttrAuthenticationType

**Framework**: Security  
**Kind**: var

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

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and denotes the authentication scheme for this item (see [`Authentication Type Values`](item-attribute-keys-and-values#Authentication-Type-Values.md)).

> **Note**:  For compatibility with earlier Keychain APIs, functions in [`Keychain services`](keychain-services.md) accept a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) for the authentication scheme. The number is a 32-bit integer that encodes the authentication scheme as a `FourCharCode`. In your code, use a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) with one of the values from [`Authentication Type Values`](item-attribute-keys-and-values#Authentication-Type-Values.md) instead of a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrauthenticationtype)*