# SecAccessCreateFromOwnerAndACL

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a new access object using the owner and access control list you provide.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecAccessCreateWithOwnerAndACL(_:_:_:_:_:)`](./secaccesscreatewithownerandacl%28_,_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecAccessCreateFromOwnerAndACL(const CSSM_ACL_OWNER_PROTOTYPE *owner, uint32 aclCount, const CSSM_ACL_ENTRY_INFO *acls, SecAccessRef*accessRef);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecAccessCreateWithOwnerAndACL(_:_:_:_:_:)`](./secaccesscreatewithownerandacl%28_,_,_,_,_%29.md) instead.

This function creates an access object from CSSM structures. You can use this function to create an access object for use with other Certificate, Key, and Trust API functions if you want to use CSSM to create the access control list. CSSM allows more complex access controls than you can construct with the Certificate, Key, and Trust API. For more information about the CSSM API, see *Common Security: CDSA and CSSM, version 2 (with corrigenda)* from The Open Group ([http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm)).

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecAccessCreateWithOwnerAndACL(_:_:_:_:_:)`](./secaccesscreatewithownerandacl%28_,_,_,_,_%29.md) instead.

## Parameters

- `owner`: A pointer to a CSSM access control list owner.
- `aclCount`: An unsigned 32-bit integer representing the number of items in the access control list.
- `acls`: A pointer to the CSSM access control list.
- `accessRef`: On return, points to the new access object. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscreatefromownerandacl)*