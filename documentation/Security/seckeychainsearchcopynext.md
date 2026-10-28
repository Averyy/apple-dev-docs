# SecKeychainSearchCopyNext

**Framework**: Security  
**Kind**: func  
**Role**: Function

Finds the next keychain item matching the given search criteria.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md) to conduct keychain item searches.

## Declaration

```c
OSStatus SecKeychainSearchCopyNext(SecKeychainSearchRef searchRef, SecKeychainItemRef*itemRef);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. The common security services manager module is no longer used.

Each item stored in the keychain contains data (such as a certificate), which is indexed by the item’s attributes. Use the [`SecKeychainSearchCreateFromAttributes`](./seckeychainsearchcreatefromattributes.md) function to specify attributes to search for. If the `SecKeychainSearchCopyNext` function finds a match, you can use the [`SecKeychainItemCopyAttributesAndData(_:_:_:_:_:_:)`](./seckeychainitemcopyattributesanddata%28_,_,_,_,_,_%29.md) function to retrieve the item’s data.

A [`SecKeychainItem`](./seckeychainitem.md) object for a certificate that is stored in a keychain can be safely cast to a [`SecCertificate`](./seccertificate.md) for use with the Certificate, Key, and Trust API.

To find and obtain data from a password keychain item, use the [`SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](./seckeychainfindinternetpassword%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md) or [`SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)`](./seckeychainfindgenericpassword%28_,_,_,_,_,_,_,_%29.md) function.

## Parameters

- `searchRef`: A reference to the current search criteria. The search object is created in the [`SecKeychainSearchCreateFromAttributes`](./seckeychainsearchcreatefromattributes.md) function and must be released by calling the `CFRelease` function when you are done with it.
- `itemRef`: On return, a pointer to a keychain item object of the next matching keychain item, if any. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsearchcopynext)*