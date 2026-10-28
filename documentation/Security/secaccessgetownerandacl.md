# SecAccessGetOwnerAndACL

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the owner and the access control list of a given access object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecAccessCopyOwnerAndACL(_:_:_:_:_:)`](./secaccesscopyownerandacl%28_,_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecAccessGetOwnerAndACL(SecAccessRef accessRef, CSSM_ACL_OWNER_PROTOTYPE_PTR*owner, uint32 *aclCount, CSSM_ACL_ENTRY_INFO_PTR*acls);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecAccessCopyOwnerAndACL(_:_:_:_:_:)`](./secaccesscopyownerandacl%28_,_,_,_,_%29.md) instead.

This function returns CSSM structures for use with CSSM API functions.

### Special Considerations

This function is deprecated in macOS 10.7 and later. Use [`SecAccessCopyOwnerAndACL(_:_:_:_:_:)`](./secaccesscopyownerandacl%28_,_,_,_,_%29.md) instead.

## Parameters

- `accessRef`: An access object from which to retrieve the owner and access control list.
- `owner`: On return, a pointer to a CSSM access control list owner.
- `aclCount`: On return, a pointer to an unsigned 32-bit integer representing the number of items in the access control list.
- `acls`: On return, a pointer to the CSSM access control list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccessgetownerandacl)*