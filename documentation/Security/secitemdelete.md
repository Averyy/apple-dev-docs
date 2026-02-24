# SecItemDelete(_:)

**Framework**: Security  
**Kind**: func

Deletes items that match a search query.

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
func SecItemDelete(_ query: CFDictionary) -> OSStatus
```

## Mentions

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The query dictionary for delete can’t contain [`Item return result keys`](item-return-result-keys.md), because [`SecItemDelete(_:)`](secitemdelete(_:).md) only returns a status.

By default, this function deletes all items matching the specified query. You can change this behavior by specifying a key, as follows:

- To delete an item identified by a transient reference, specify the [`kSecMatchItemList`](ksecmatchitemlist.md) search key with a reference returned by using the [`kSecReturnRef`](ksecreturnref.md) return type key in a previous call to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) or [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) functions.
- To delete an item identified by a persistent reference, specify the [`kSecMatchItemList`](ksecmatchitemlist.md) search key with a persistent reference returned by using the [`kSecReturnPersistentRef`](ksecreturnpersistentref.md) return type key to the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) or [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) functions.
- If more than one of these return keys is specified, the behavior is undefined.

##### Performance Considerations

`SecItemDelete` blocks the calling thread, so it can cause your app’s UI to hang if called from the main thread. Instead, call `SecItemDelete` from a background dispatch queue or `async` function:

**Swift**:

```swift
private func deleteKeychainItem(searchAttributes attrs: CFDictionary, _ completion: @escaping (OSStatus) -> Void) {
    queue.async {
        let result = SecItemDelete(attrs)
        completion(result)
    }
}
```

**Objective-C**:

```objc
- (void)deleteKeychainItemWithAttributes:(CFDictionaryRef)attrs completion:(void(^)(OSStatus status))completion {
    dispatch_async(backgroundQueue, ^{
        OSStatus deleteResult = SecItemDelete(attrs);
        completion(deleteResult);
    });
}

```

## Parameters

- `query`: A dictionary that describes the search for the keychain items you want to delete. A typical `query` dictionary consists of: - **The item’s class.** Specify the kind of item you want, for example a password, a certificate, or a cryptographic key, using one of the class values in [`Item class keys and values`](item-class-keys-and-values.md).
- **Attributes.** Narrow the search by indicating the attributes that the found item or items should have. The more attributes you specify, the more refined the results, but not all attributes apply to all item classes. For the attributes applicable to the keychain item you’re deleting, see the entry for the item’s class in [`Item class values`](item-class-keys-and-values#Item-class-values.md).
- **Search parameters.** Condition the search in a variety of ways. For example, you can limit the results to a specific number of items, control case sensitivity when matching string attributes, or search only among a particular set of items. See [`Search attribute keys and values`](search-attribute-keys-and-values.md) for the complete list of possible search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemdelete(_:))*