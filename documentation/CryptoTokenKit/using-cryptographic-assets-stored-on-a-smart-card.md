# Using Cryptographic Assets Stored on a Smart Card

**Framework**: CryptoTokenKit

Access certificates, keys, and identities stored on a smart card as if they were part of the keychain.

#### Overview

A token is a storage repository for cryptographic items. When a token is present in the system—such as when the user physically inserts a smart card into a USB slot—the CryptoTokenKit framework exposes the token’s items to your app as standard keychain items. It does this by copying the items to the keychain when the token is inserted, and deleting them from the keychain when the token is removed.

![Diagram showing how CryptoTokenKit makes keys stored on a smart card available to apps through keychain services.](https://docs-assets.developer.apple.com/published/0bd8ebd910d1499e169937a0ebe9c042/media-2940885%402x.png)

Because the items appear to your app as standard keychain items, you use [`Keychain services`](https://developer.apple.com/documentation/Security/keychain-services) to access them. All the usual rules for building a search query and parsing the search results apply. For an example of storing and retrieving keychain items, see [`Storing Keys in the Keychain`](https://developer.apple.com/documentation/Security/storing-keys-in-the-keychain). When you work with tokens, the CryptoTokenKit framework handles the storage. You only have to perform item retrieval.

##### Narrow the Keychain Search with a Token Id

When the framework copies an item from a token to the keychain, it records the associated token’s identifier, or token ID, as part of the keychain item. If you know the token ID, you can use it to very precisely filter the keychain search. Do this by including the [`kSecAttrTokenID`](https://developer.apple.com/documentation/Security/kSecAttrTokenID) key in the query dictionary. For example, to get a reference to a key that comes from a token with token ID `com.example.piv:0123456789`, use the search query:

```swift
let getquery: [String: Any] = [kSecClass as String: kSecClassKey,
                               kSecAttrTokenID as String: "com.example.piv:0123456789",
                               kSecReturnRef as String: true]
```

To identify token IDs that are currently available in the system, use an instance of the [`TKTokenWatcher`](tktokenwatcher.md) class. This object has a [`tokenIDs`](tktokenwatcher/tokenids.md) property that’s a list of all the token IDs present in the system. You can read this at any time:

```swift
let watcher = TKTokenWatcher()
print("The following token IDs are present in the system:")
for tokenID in watcher.tokenIDs {
    print(tokenID)
}
```

Alternatively, use the [`setInsertionHandler(_:)`](tktokenwatcher/setinsertionhandler(_:).md) method to register for a callback when a token is inserted into the system. Register to be notified of a particular token’s removal using the [`addRemovalHandler(_:forTokenID:)`](tktokenwatcher/addremovalhandler(_:fortokenid:).md) method. You typically use these methods together, registering for removal at the time the insertion handler is called:

```swift
watcher.setInsertionHandler { tokenID in
    print("Token \(tokenID) inserted")
            
    watcher.addRemovalHandler( { tokenID in
        print("Token \(tokenID) removed")
    }, forTokenID: tokenID)
}
```

##### Use a Persistent Reference to Record a Token Item

When you want to keep a record of a token item or pass it to another process, you can get a persistent reference to the associated keychain item. Do this by setting the [`kSecReturnPersistentRef`](https://developer.apple.com/documentation/Security/kSecReturnPersistentRef) key’s value to [`true`](https://developer.apple.com/documentation/foundation/nsexpression/1411874-true) in the keychain search query. For example, the earlier query becomes:

```swift
let getquery: [String: Any] = [kSecClass as String: kSecClassKey,
                               kSecAttrTokenID as String: "com.example.piv:0123456789",
                               kSecReturnPersistentRef as String: true]
```

However, if you perform any operation with the persistent reference after the token is removed from the system, Keychain Services returns the [`errSecItemNotFound`](https://developer.apple.com/documentation/Security/errSecItemNotFound) status.  Handle this by prompting the user to reinsert the token, after which you can try the operation again.

## See Also

- [class TKSmartCardSlotManager](tksmartcardslotmanager.md)
  An interface to all available smart card reader slots.
- [class TKSmartCardSlot](tksmartcardslot.md)
  A single smart card reader slot in the system.
- [class TKSmartCard](tksmartcard.md)
  A representation of a smart card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/using-cryptographic-assets-stored-on-a-smart-card)*