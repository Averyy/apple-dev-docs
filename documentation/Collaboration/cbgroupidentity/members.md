# members

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns the members of the group.

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

## Declaration

```objc
@property (nonatomic, readonly, nullable) NSArray * members;
```

## Return Value

An array of `CBIdentity` objects each representing a member of the group identity.

## Discussion

This method only returns direct members of a group, it does not return members of members. Both user and group identities can be members of a group, but a group cannot be a member of itself. You also cannot have “circular” membership, i.e. a group be a member of another group that is a member of the first group.

## See Also

### Group Identity Attributes
- [var posixGID: gid_t](./posixgid.md)
  Returns the POSIX GID of the identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbgroupidentity/members)*