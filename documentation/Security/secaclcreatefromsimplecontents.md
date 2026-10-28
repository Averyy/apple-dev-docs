# SecACLCreateFromSimpleContents

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a new access control list entry from the application list, description, and prompt selector provided and adds it to an item’s access object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecACLCreateWithSimpleContents(_:_:_:_:_:)`](./secaclcreatewithsimplecontents%28_,_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecACLCreateFromSimpleContents(SecAccessRef access, CFArrayRef applicationList, CFStringRef description, const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector, SecACLRef*newAcl);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecACLCreateWithSimpleContents(_:_:_:_:_:)`](./secaclcreatewithsimplecontents%28_,_,_,_,_%29.md) instead.

The ACL object returned by this function is a reference to an access control list (ACL) entry. The ACL entry includes a list of trusted applications (see [`SecTrustedApplicationCreateFromPath(_:_:)`](./sectrustedapplicationcreatefrompath%28_,_%29.md)), the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies. By default, a new ACL entry applies to all operations (the CSSM authorization tag is set to `CSSM_ACL_AUTHORIZATION_ANY`). Use the [`SecACLSetAuthorizations`](./secaclsetauthorizations.md) function to set the list of operations for an ACL object.

The system allows exactly one owner ACL entry in each access object. The `SecACLCreateFromSimpleContents` function fails if you attempt to add a second owner ACL. To change owner access controls, use the [`SecAccessCopySelectedACLList`](./secaccesscopyselectedacllist.md) function to find the owner ACL (that is, the only ACL with a CSSM authorization tag of `CSSM_ACL_AUTHORIZATION_CHANGE_ACL`) and the [`SecACLSetSimpleContents`](./secaclsetsimplecontents.md) function to change it as needed.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecACLCreateWithSimpleContents(_:_:_:_:_:)`](./secaclcreatewithsimplecontents%28_,_,_,_,_%29.md) instead.

## Parameters

- `access`: The access object to which to add the information.
- `applicationList`: An array of trusted application objects (that is, [`SecTrustedApplication`](./sectrustedapplication.md) instances) identifying applications that are allowed access to the keychain item without user confirmation. Use the [`SecTrustedApplicationCreateFromPath(_:_:)`](./sectrustedapplicationcreatefrompath%28_,_%29.md) function to create trusted application objects. If you set this parameter to `NULL`, then any application can use this item. If you pass an empty array, then there are no trusted applications. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.
- `description`: The human readable name to be used to refer to this item when the user is prompted.
- `promptSelector`: A pointer to a prompt selector. If you set the `CSSM_ACL_KEYCHAIN_PROMPT_REQUIRE_PASSPHRASE` bit, the user is prompted for the keychain password each time a non-trusted application attempts to access this item, even if the keychain is already unlocked.
- `newAcl`: On return, points to an access control list object, which is a reference to the new access control list entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclcreatefromsimplecontents)*