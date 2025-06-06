# kSecAttrSecurityDomain

**Framework**: Security  
**Kind**: var

A key whose value is a string indicating the item’s security domain.

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
let kSecAttrSecurityDomain: CFString
```

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and represents the Internet security domain. Items of class [`kSecClassInternetPassword`](ksecclassinternetpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrsecuritydomain)*