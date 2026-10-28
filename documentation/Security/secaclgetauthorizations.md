# SecACLGetAuthorizations

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the CSSM authorization tags of a given access control list entry.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecACLCopyAuthorizations(_:)`](./secaclcopyauthorizations%28_%29.md) instead.

## Declaration

```c
OSStatus SecACLGetAuthorizations(SecACLRef acl, CSSM_ACL_AUTHORIZATION_TAG *tags, uint32 *tagCount);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecACLCopyAuthorizations(_:)`](./secaclcopyauthorizations%28_%29.md) instead.

An ACL object includes a list of trusted applications (see [`SecTrustedApplicationCreateFromPath(_:_:)`](./sectrustedapplicationcreatefrompath%28_,_%29.md)), the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL object applies. Use this function to retrieve the list of operations for an ACL object. Use the [`SecACLCopySimpleContents`](./secaclcopysimplecontents.md) function to retrieve the other information.

The `SecACLGetAuthorizations` function returns an error if there are more tags to return than the number of elements you allocated in the `tags` array. A 20-element array should suffice for most purposes; however, you can test for the `errSecBufferTooSmall` error and increase the size of the array before calling the function again if necessary. Alternatively, you can call the function with a tag count of `0`, read the value returned in the `tagCount` parameter, and then call the function again using that value.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecACLCopyAuthorizations(_:)`](./secaclcopyauthorizations%28_%29.md) instead.

## Parameters

- `acl`: An ACL object that identifies the access control list entry from which you wish to retrieve the authorization tags.
- `tags`: A pointer to an array of CSSM authorization tags. You must allocate this array before calling the function. On return, this array contains the authorization tags of the specified ACL entry.
- `tagCount`: On entry, points to the number of elements in the array you passed in the `tags` parameter. On return, points to the number of tags actually returned or, in the case of an overflow, the number of tags required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclgetauthorizations)*