# SecItemAdd(_:_:)

**Framework**: Security  
**Kind**: func

Adds one or more items to a keychain.

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
func SecItemAdd(_ attributes: CFDictionary, _ result: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus
```

## Mentions

- [Adding a password to the keychain](adding-a-password-to-the-keychain.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)
- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)
- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

To add multiple items to a keychain at once use the [`kSecUseItemList`](ksecuseitemlist.md) key in the `attributes` dictionary with an array of dictionaries (each corresponding to one of the items) as its value. This is only supported for non-password items.

When you use Xcode to create an application, Xcode adds an `application-identifier` entitlement to the application bundle. Keychain Services uses this entitlement to grant the application access to its own keychain items. To share the new keychain item to among multiple apps, include the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) key in the `attributes` dictionary. The value of this key must be the name of a keychain access group to which all the programs that share this item belong.

##### Performance Considerations

`SecItemAdd` blocks the calling thread, so it can cause your app’s UI to hang if called from the main thread. Instead, call `SecItemAdd` from a background dispatch queue or `async` function:

## Parameters

- `attributes`: A dictionary that describes the item to add. A typical   dictionary consists of:
- `result`: On return, a reference to the newly added items. The exact type of the result is based on the values supplied in  , as discussed in  . Pass   if you don’t need the result. Otherwise, your app becomes responsible for releasing the referenced object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemadd(_:_:))*