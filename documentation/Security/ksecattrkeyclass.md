# kSecAttrKeyClass

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s cryptographic key class.

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
let kSecAttrKeyClass: CFString
```

#### Discussion

The corresponding value is of type [`CFTypeRef`](https://developer.apple.com/documentation/CoreFoundation/CFTypeRef) and specifies a type of cryptographic key. Possible values are listed in [`Key Class Values`](item-attribute-keys-and-values#Key-Class-Values.md). Read only.

> **Note**:  Don’t confuse this attribute with the more general [`kSecClass`](ksecclass.md) attribute that indicates an item’s class (for example password, certificate, or cryptographic key). The [`kSecAttrKeyClass`](ksecattrkeyclass.md) attribute described here applies only to items of class [`kSecClassKey`](ksecclasskey.md), indicating what category a cryptographic key fits into (for example, public, private, or symmetric).

 Don’t confuse this attribute with the more general [`kSecClass`](ksecclass.md) attribute that indicates an item’s class (for example password, certificate, or cryptographic key). The [`kSecAttrKeyClass`](ksecattrkeyclass.md) attribute described here applies only to items of class [`kSecClassKey`](ksecclasskey.md), indicating what category a cryptographic key fits into (for example, public, private, or symmetric).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrkeyclass)*