# kSecAttrLabel

**Framework**: Security  
**Kind**: var

A key with a value that’s a string indicating the item’s label.

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
let kSecAttrLabel: CFString
```

## Mentions

- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)
- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and contains the user-visible label for this item.

On key creation, if not explicitly specified, this attribute defaults to `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrlabel)*