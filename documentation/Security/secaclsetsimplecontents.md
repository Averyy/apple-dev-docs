# SecACLSetSimpleContents

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the application list, description, and prompt selector for a given access control list entry.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecACLSetContents(_:_:_:_:)`](./secaclsetcontents%28_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecACLSetSimpleContents(SecACLRef acl, CFArrayRef applicationList, CFStringRef description, const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecACLSetContents(_:_:_:_:)`](./secaclsetcontents%28_,_,_,_%29.md) instead.

Because an ACL object is always associated with an access object, when you modify an ACL entry, you are modifying the access object as well. There is no need for a separate function to write a modified ACL object back into the access object.

Use the [`SecACLGetAuthorizations`](./secaclgetauthorizations.md) function to get the list of operations for an ACL object.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecACLSetContents(_:_:_:_:)`](./secaclsetcontents%28_,_,_,_%29.md) instead.

## Parameters

- `acl`: An ACL object that identifies the access control list entry.
- `applicationList`: An array of trusted application objects (that is, [`SecTrustedApplication`](./sectrustedapplication.md) instances) identifying applications that are allowed access to the keychain item without user confirmation. Use the [`SecTrustedApplicationCreateFromPath(_:_:)`](./sectrustedapplicationcreatefrompath%28_,_%29.md) function to create trusted application objects. If you set this parameter to `NULL`, then any application can use this item. If you pass an empty array, then all applications are treated as untrusted.
- `description`: The name of the keychain item that appears in the dialog box when the user is prompted for permission to use the item. Note that this name is not necessarily the same as the one displayed for the item by the Keychain Access application.
- `promptSelector`: The prompt selector flag for the given access control list entry. Set the `CSSM_ACL_KEYCHAIN_PROMPT_REQUIRE_PASSPHRASE` bit to have the user prompted for the keychain password each time a non-trusted application attempts to access this item, even if the keychain is already unlocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclsetsimplecontents)*