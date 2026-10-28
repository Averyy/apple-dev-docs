# SecACLSetAuthorizations

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the CSSM authorization tags for a given access control list entry.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecACLUpdateAuthorizations(_:_:)`](./secaclupdateauthorizations%28_,_%29.md) instead.

## Declaration

```c
OSStatus SecACLSetAuthorizations(SecACLRef acl, CSSM_ACL_AUTHORIZATION_TAG *tags, uint32 tagCount);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecACLUpdateAuthorizations(_:_:)`](./secaclupdateauthorizations%28_,_%29.md) instead.

An ACL object includes a list of trusted applications (see [`SecTrustedApplicationCreateFromPath(_:_:)`](./sectrustedapplicationcreatefrompath%28_,_%29.md)), the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL object applies. Use this function to set a list of operations for an ACL object, or set the `CSSM_ACL_AUTHORIZATION_ANY` tag to allow all operations. Use the [`SecACLSetSimpleContents`](./secaclsetsimplecontents.md) function to set the other information.

Because an ACL object is always associated with an access object, when you modify an ACL entry, you are modifying the access object as well. There is no need for a separate function to write a modified ACL object back into the access object.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecACLUpdateAuthorizations(_:_:)`](./secaclupdateauthorizations%28_,_%29.md) instead.

## Parameters

- `acl`: An ACL object that identifies the access control list entry for which you wish to set authorization tags.
- `tags`: An array of CSSM authorization tags.
- `tagCount`: The number of tags in the CSSM authorization tag array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclsetauthorizations)*