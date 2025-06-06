# kSecAttrAccessGroup

**Framework**: Security  
**Kind**: var

A key with a value that’s a string indicating the access group the item is in.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrAccessGroup: CFString
```

## Mentions

- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
- [Searching for keychain items](searching-for-keychain-items.md)

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and indicates the item’s one and only access group.

For an app to access a keychain item, one of the groups to which the app belongs must be the item’s group. The list of an app’s access groups consists of the following string identifiers, in this order:

- The strings in the app’s [`Keychain Access Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/keychain-access-groups)
- The app ID string
- The strings in the [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups)

Two or more apps that are in the same access group can share keychain items. For more details, see [`Sharing access to keychain items among a collection of apps`](sharing-access-to-keychain-items-among-a-collection-of-apps.md).

Specify which access group a keychain item belongs to when you create it by setting the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) attribute in the query you send to the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) method. Naming a group that’s not among the creating app’s access groups—including the empty string, which is always an invalid group—generates an error. If you don’t explicitly set a group, keychain services defaults to the app’s first access group, which is either the first keychain access group, or the app ID when the app has no keychain groups. In the latter case, the item is only accessible to the app creating the item, since no other app can be in that group.

By default, the [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md), [`SecItemDelete(_:)`](secitemdelete(_:).md), and [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) methods search all the app’s access groups. Add the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) attribute to the query to limit the search to a particular group.

> ❗ **Important**:  This attribute applies to macOS keychain items only if you also set a value of `true` for the [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) key, the [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) key, or both.

 This attribute applies to macOS keychain items only if you also set a value of `true` for the [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) key, the [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) key, or both.

## See Also

- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)
  Enable apps to share keychain items with each other by adding the apps to an access group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccessgroup)*