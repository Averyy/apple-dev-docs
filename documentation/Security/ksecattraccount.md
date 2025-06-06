# kSecAttrAccount

**Framework**: Security  
**Kind**: var

A key whose value is a string indicating the item’s account name.

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
let kSecAttrAccount: CFString
```

## Mentions

- [Searching for keychain items](searching-for-keychain-items.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and contains an account name. Items of class [`kSecClassGenericPassword`](ksecclassgenericpassword.md) and [`kSecClassInternetPassword`](ksecclassinternetpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccount)*