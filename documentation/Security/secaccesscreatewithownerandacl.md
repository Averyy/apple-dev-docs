# SecAccessCreateWithOwnerAndACL(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a new access instance using the owner and ACL entries you provide.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccess?
```

#### Return Value

The new access instance. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to release it when you are finished using it.

#### Discussion

Use this method to create a customized access instance from [`SecACL`](secacl.md) instances that you’ve created with the [`SecACLCreateWithSimpleContents(_:_:_:_:_:)`](secaclcreatewithsimplecontents(_:_:_:_:_:).md) method. If you want a default access instance, use the [`SecAccessCreate(_:_:_:)`](secaccesscreate(_:_:_:).md) method instead.

## Parameters

- `userId`: The user ID that owns this ACL.
- `groupId`: The group ID that owns this ACL.
- `ownerType`: Flags that control whether the specified user ID or group ID owns the resulting ACL. See   for details.
- `acls`: An array of ACL entries to associate with the access instance.
- `error`: The address of an error instance. On error, the return value is  , and the variable referenced by this parameter is overwritten with a   instance that provides more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscreatewithownerandacl(_:_:_:_:_:))*