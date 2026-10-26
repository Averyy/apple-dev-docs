# SecACLCopySimpleContents

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the application list, description, and CSSM prompt selector for a given access control list entry.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecACLCopyContents(_:_:_:_:)`](./secaclcopycontents%28_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecACLCopySimpleContents(SecACLRef acl, CFArrayRef*applicationList, CFStringRef*description, CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecACLCopyContents(_:_:_:_:)`](./secaclcopycontents%28_,_,_,_%29.md) instead.

An access control list entry applies to a specific use or set of uses for a specific keychain item. The ACL object includes a list of trusted applications (see [`SecTrustedApplicationCreateFromPath(_:_:)`](./sectrustedapplicationcreatefrompath%28_,_%29.md)), the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL object applies. Use the [`SecACLGetAuthorizations`](./secaclgetauthorizations.md) function to get the list of operations for an ACL object.

##### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecACLCopyContents(_:_:_:_:)`](./secaclcopycontents%28_,_,_,_%29.md) instead.

## Parameters

- `acl`: An ACL object that identifies the access control list entry from which you want information.
- `applicationList`: On return, points to an array of [`SecTrustedApplication`](./sectrustedapplication.md) instances identifying applications that are allowed access to the keychain item without user confirmation. If this parameter returns `NULL`, then any application can use this item. If this parameter returns a valid pointer but the array is empty, then there are no trusted applications. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.
- `description`: On return, the name of the keychain item that appears in the dialog box when the user is prompted for permission to use the item. Note that this name is not necessarily the same as the one displayed for the item by the Keychain Access application. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.
- `promptSelector`: On return, points to the prompt selector flag for the given access control list entry. If the `CSSM_ACL_KEYCHAIN_PROMPT_REQUIRE_PASSPHRASE` bit is set, the user is prompted for the keychain password each time a non-trusted application attempts to access this item, even if the keychain is already unlocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclcopysimplecontents)*