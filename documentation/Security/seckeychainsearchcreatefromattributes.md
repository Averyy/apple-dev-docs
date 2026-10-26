# SecKeychainSearchCreateFromAttributes

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a search object matching a list of zero or more attributes.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md) instead.

## Declaration

```c
OSStatus SecKeychainSearchCreateFromAttributes(CFTypeRef keychainOrArray, SecItemClass itemClass, const SecKeychainAttributeList *attrList, SecKeychainSearchRef*searchRef);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md) instead.

Each item stored in the keychain contains data (such as a certificate), which is indexed by the item’s attributes. You look up an item in a keychain by its attributes. If you find a match, you can then retrieve the item’s data. Use the search object created by this function as input to the [`SecKeychainSearchCopyNext`](./seckeychainsearchcopynext.md) function to find a keychain item and the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](./seckeychainitemcopyattributesanddata%28_,_,_,_,_,_%29.md) function to retrieve the item’s data.

To find and obtain data from a password keychain item, use the [`SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](./seckeychainfindinternetpassword%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md) or [`SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)`](./seckeychainfindgenericpassword%28_,_,_,_,_,_,_,_%29.md) function.

## Parameters

- `keychainOrArray`: A reference to an array of keychains to search, a single keychain, or `NULL` to search the user’s current keychain search list. Use the function [`SecKeychainCopySearchList(_:)`](./seckeychaincopysearchlist%28_%29.md) to retrieve the user’s default search list.
- `itemClass`: The keychain item class. See [`SecItemClass`](./secitemclass.md) for valid constants.
- `attrList`: A pointer to a list of zero or more keychain attribute records to match. Pass `NULL` to match any keychain attribute.
- `searchRef`: On return, a pointer to the current search object. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsearchcreatefromattributes)*