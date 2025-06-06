# kSecUseItemList

**Framework**: Security  
**Kind**: var

A key whose value is an array of items to search.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
let kSecUseItemList: CFString
```

#### Discussion

The corresponding value is of type [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray), where the array contains either [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), [`SecIdentity`](secidentity.md), or  (for persistent item references) [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) items. The items in the array must all be of the same type.

When this attribute is provided, no keychains are searched. Instead, the specified array is treated as the set of all possible items to search (or to add if the function being called is [`SecItemAdd(_:_:)`](secitemadd(_:_:).md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseitemlist)*