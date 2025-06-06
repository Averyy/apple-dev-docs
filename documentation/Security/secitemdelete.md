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

- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)
- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)

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

## Parameters

- `query`: A dictionary that describes the search for the keychain items you want to delete. A typical   dictionary consists of:


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemdelete(_:))*