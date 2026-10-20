# accessControlList

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Clear the access control list.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var accessControlList: CFFileSecurityClearOptions { get }
```

```c
kCFFileSecurityClearAccessControlList
```

## See Also

### Constants
- [static var group: CFFileSecurityClearOptions](./group.md)
  Clear the (POSIX) group ID.
- [static var groupUUID: CFFileSecurityClearOptions](./groupuuid.md)
  Clear the group UUID (for the access control list).
- [static var mode: CFFileSecurityClearOptions](./mode.md)
  Clear the file’s mode (POSIX permissions).
- [static var owner: CFFileSecurityClearOptions](./owner.md)
  Clear the (POSIX) owner ID.
- [static var ownerUUID: CFFileSecurityClearOptions](./owneruuid.md)
  Clear the owner UUID (for the access control list).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/accesscontrollist)*