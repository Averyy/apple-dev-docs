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

- [Searching for keychain items](searching-for-keychain-items.md)
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)
- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)
- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

By default, this function returns only the first match found. To obtain more than one matching item at a time, specify the search key [`kSecMatchLimit`](ksecmatchlimit.md) with a value greater than `1`. The `result` is a [`CFArray`](https://developer.apple.com/documentation/corefoundation/cfarray) containing up to that number of matching items.

> **Note**:  You can’t combine the [`kSecReturnData`](ksecreturndata.md) and [`kSecMatchLimitAll`](ksecmatchlimitall.md) options when copying password items (items of class [`SecItemClass.internetPasswordItemClass`](secitemclass/internetpassworditemclass.md) or [`SecItemClass.genericPasswordItemClass`](secitemclass/genericpassworditemclass.md)), because copying each password item could require additional authentication. Instead, request a reference or persistent reference to the items, then request the data for only the specific passwords that you actually require.

By default, this function searches for items in the keychain. To instead provide your own set of items to filter with the `query`, specify the search key [`kSecMatchItemList`](ksecmatchitemlist.md) and provide as its value a [`CFArray`](https://developer.apple.com/documentation/corefoundation/cfarray) object containing items of type [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), or [`SecIdentity`](secidentity.md). The objects in the provided array must all be of the same type.

To limit a keychain search to a particular keychain or keychains, specify the search key [`kSecMatchSearchList`](ksecmatchsearchlist.md) and provide as its value a [`CFArray`](https://developer.apple.com/documentation/corefoundation/cfarray) object containing items of type [`SecKeychain`](seckeychain.md) items.

To convert from persistent item references to normal item references, specify the search key [`kSecMatchItemList`](ksecmatchitemlist.md) with a value that consists of an object of type [`CFArray`](https://developer.apple.com/documentation/corefoundation/cfarray) referencing an array containing one or more elements of type [`CFData`](https://developer.apple.com/documentation/corefoundation/cfdata) (the persistent references), and a return-type key of [`kSecReturnRef`](ksecreturnref.md) whose value is [`kCFBooleanTrue`](https://developer.apple.com/documentation/corefoundation/kcfbooleantrue). The objects in the provided array must all be of the same type.

When you use Xcode to create an application, Xcode adds an `application-identifier` entitlement to the application bundle. Keychain Services uses this entitlement to grant the application access to its own keychain items. You can also add a [`Keychain Access Groups Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/keychain-access-groups) to the application, specifying an array of keychain access groups to which the application belongs. When you call the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function to add an item to the keychain, you can specify the access group to which that item should belong. By default, the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function searches all the access groups to which the application belongs. However, you can add the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) key to the search dictionary to specify which access group to search for keychain items.

##### Performance Considerations

`SecItemCopyMatching` blocks the calling thread, so it can cause your app’s UI to hang if called from the main thread. Instead, call `SecItemCopyMatching` from a background dispatch queue or `async` function:

**Swift**:

```swift
func findKeychainItem(attributes attrs: CFDictionaryRef, _ completion: @escaping (OSStatus, CFTypeRef?) -> Void) {
    backgroundQueue.async {
        var item: CFTypeRef?
        let result = SecItemCopyMatching(attrs, &item)
        completion(result, item)
    }
}

```

**Objective-C**:

```objc
- (void)findKeychainItemWithAttributes:(NSDictionary *)attributes completion:(void(^)(OSStatus status, CFTypeRef item))completion {
    dispatch_async(backgroundQueue, ^{
        CFDictionaryRef attrs = (__bridge CFDictionaryRef)attributes;
        CFTypeRef item = NULL;
        OSStatus result = SecItemCopyMatching(attrs, &item);
        completion(result, item);
        CFRelease(item);
    });
}


```

## Parameters

- `query`: A dictionary that describes the search. A typical `query` dictionary consists of: - **The item’s class.** Specify the kind of item you want, for example a password, a certificate, or a cryptographic key, using one of the class values in [`Item class keys and values`](item-class-keys-and-values.md).
- **Attributes.** Narrow the search by indicating the attributes that the found item or items should have. The more attributes you specify, the more refined the results, but not all attributes apply to all item classes. For the attributes applicable to the keychain item you’re searching for, see the entry for the item’s class in [`Item class values`](item-class-keys-and-values#Item-class-values.md).
- **Search parameters.** Condition the search in a variety of ways. For example, you can limit the results to a specific number of items, control case sensitivity when matching string attributes, or search only among a particular set of items. See [`Search attribute keys and values`](search-attribute-keys-and-values.md) for the complete list of possible search parameters.
- **One or more return types.** Use the keys found in [`Item return result keys`](item-return-result-keys.md) to indicate whether you seek the item’s attributes, the item’s data, a reference to the data, a persistent reference to the data, or a combination of these. When you specify more than one return type, the search returns a dictionary containing each of the types you request. When your search allows multiple results, they’re all returned together in an array of items.
- `result`: On return, a reference to the found items. The exact type of the result depends on the return type values supplied in `query`, as discussed in [`Item return result keys`](item-return-result-keys.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemcopymatching(_:_:))*