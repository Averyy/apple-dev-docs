# kSecMatchItemList

**Framework**: Security  
**Kind**: var

A key whose value indicates a list of items to search.

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
let kSecMatchItemList: CFString
```

## Mentions

- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Discussion

To provide your own set of items to be filtered by a search query rather than searching the keychain, specify this search key in a call to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function with a value that consists of an object of type [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) where the array contains either [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), [`SecIdentity`](secidentity.md), or [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) items. The objects in the provided array must all be of the same type.

To convert from persistent item references to normal item references, specify this search key in a call to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function with a value of type [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) where the array contains one or more [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) elements (the persistent references), and a return-type key of [`kSecReturnRef`](ksecreturnref.md) whose value is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).

To delete an item identified by a transient reference, specify the [`kSecMatchItemList`](ksecmatchitemlist.md) search key in a call to the [`SecItemDelete(_:)`](secitemdelete(_:).md) function with a reference returned by using the [`kSecReturnRef`](ksecreturnref.md) return type key in a previous call to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) or [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) functions.

To delete an item identified by a persistent reference, specify the [`kSecMatchItemList`](ksecmatchitemlist.md) search key in a call to the [`SecItemDelete(_:)`](secitemdelete(_:).md) function with a persistent reference returned by using the [`kSecReturnPersistentRef`](ksecreturnpersistentref.md) return type key to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) or [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchitemlist)*