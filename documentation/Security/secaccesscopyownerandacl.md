# SecAccessCopyOwnerAndACL(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the owner and the ACL entries of a given access instance.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess, _ userId: UnsafeMutablePointer<uid_t>?, _ groupId: UnsafeMutablePointer<gid_t>?, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>?, _ aclList: UnsafeMutablePointer<CFArray?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `accessRef`: An access instance from which to retrieve the owner and ACL entries.
- `userId`: On return, the user ID that owns the access instance.
- `groupId`: On return, the group ID that owns the access instance.
- `ownerType`: On return, flags that indicate whether the specified user ID or group ID owns the resulting ACL entries. See   for details.
- `aclList`: On return, an array of   instances associated with the access instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscopyownerandacl(_:_:_:_:_:))*