# SecAccessCopySelectedACLList

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves selected access control lists from a given access object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecAccessCopyMatchingACLList(_:_:)`](./secaccesscopymatchingacllist%28_,_%29.md) instead.

## Declaration

```c
OSStatus SecAccessCopySelectedACLList(SecAccessRef accessRef, CSSM_ACL_AUTHORIZATION_TAG action, CFArrayRef*aclList);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecAccessCopyMatchingACLList(_:_:)`](./secaccesscopymatchingacllist%28_,_%29.md) instead.

An access object can have any number of access control list (ACL) entries for specific operations or sets of operations. To retrieve all the ACL entries for an access object, use the [`SecAccessCopyACLList(_:_:)`](./secaccesscopyacllist%28_,_%29.md) function.

##### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecAccessCopyMatchingACLList(_:_:)`](./secaccesscopymatchingacllist%28_,_%29.md) instead.

## Parameters

- `accessRef`: The access object from which to retrieve the information.
- `action`: An access control list authorization tag; the function returns only those access control list entries that apply to the operation indicated by this tag.
- `aclList`: On return, a pointer to the selected access control lists. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscopyselectedacllist)*