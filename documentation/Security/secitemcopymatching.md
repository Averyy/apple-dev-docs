# SecItemCopyMatching(_:_:)

**Framework**: Security  
**Kind**: func

Returns one or more keychain items that match a search query, or copies attributes of specific keychain items.

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
func SecItemCopyMatching(_ query: CFDictionary, _ result: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus
```

## Mentions

- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)
- [Searching for keychain items](searching-for-keychain-items.md)
- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)
- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

By default, this function returns only the first match found. To obtain more than one matching item at a time, specify the search key [`kSecMatchLimit`](ksecmatchlimit.md) with a value greater than `1`. The `result` is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) containing up to that number of matching items.

> **Note**:  You can’t combine the [`kSecReturnData`](ksecreturndata.md) and [`kSecMatchLimitAll`](ksecmatchlimitall.md) options when copying password items (items of class [`SecItemClass.internetPasswordItemClass`](secitemclass/internetpassworditemclass.md) or [`SecItemClass.genericPasswordItemClass`](secitemclass/genericpassworditemclass.md)), because copying each password item could require additional authentication. Instead, request a reference or persistent reference to the items, then request the data for only the specific passwords that you actually require.

By default, this function searches for items in the keychain. To instead provide your own set of items to filter with the `query`, specify the search key [`kSecMatchItemList`](ksecmatchitemlist.md) and provide as its value a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) object containing items of type [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), or [`SecIdentity`](secidentity.md). The objects in the provided array must all be of the same type.

To limit a keychain search to a particular keychain or keychains, specify the search key [`kSecMatchSearchList`](ksecmatchsearchlist.md) and provide as its value a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) object containing items of type [`SecKeychain`](seckeychain.md) items.

To convert from persistent item references to normal item references, specify the search key [`kSecMatchItemList`](ksecmatchitemlist.md) with a value that consists of an object of type [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) referencing an array containing one or more elements of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) (the persistent references), and a return-type key of [`kSecReturnRef`](ksecreturnref.md) whose value is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue). The objects in the provided array must all be of the same type.

When you use Xcode to create an application, Xcode adds an `application-identifier` entitlement to the application bundle. Keychain Services uses this entitlement to grant the application access to its own keychain items. You can also add a [`Keychain Access Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/keychain-access-groups) to the application, specifying an array of keychain access groups to which the application belongs. When you call the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function to add an item to the keychain, you can specify the access group to which that item should belong. By default, the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function searches all the access groups to which the application belongs. However, you can add the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) key to the search dictionary to specify which access group to search for keychain items.

##### Performance Considerations

`SecItemCopyMatching` blocks the calling thread, so it can cause your app’s UI to hang if called from the main thread. Instead, call `SecItemCopyMatching` from a background dispatch queue or `async` function:

## Parameters

- `query`: A dictionary that describes the search. A typical   dictionary consists of:
- `result`: On return, a reference to the found items. The exact type of the result depends on the return type values supplied in  , as discussed in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemcopymatching(_:_:))*