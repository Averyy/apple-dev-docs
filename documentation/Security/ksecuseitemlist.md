# kSecUseItemList

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is an array of items to search.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- macOS 10.6+
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 5.0

> **Deprecated**: Not implemented on this platform

## Declaration

```swift
let kSecUseItemList: CFString
```

```c
extern CFStringRef const kSecUseItemList;
```

## Discussion

The corresponding value is of type [`CFArray`](../CoreFoundation/cfarray.md), where the array contains either [`SecKeychainItem`](./seckeychainitem.md), [`SecKey`](./seckey.md), [`SecCertificate`](./seccertificate.md), [`SecIdentity`](./secidentity.md), or  (for persistent item references) [`CFData`](../CoreFoundation/cfdata.md) items. The items in the array must all be of the same type.

When this attribute is provided, no keychains are searched. Instead, the specified array is treated as the set of all possible items to search (or to add if the function being called is [`SecItemAdd(_:_:)`](./secitemadd%28_,_%29.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseitemlist)*