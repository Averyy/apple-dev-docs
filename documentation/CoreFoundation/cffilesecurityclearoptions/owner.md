# owner

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Clear the (POSIX) owner ID.

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
static var owner: CFFileSecurityClearOptions { get }
```

```c
kCFFileSecurityClearOwner
```

## See Also

### Constants
- [static var accessControlList: CFFileSecurityClearOptions](./accesscontrollist.md)
  Clear the access control list.
- [static var group: CFFileSecurityClearOptions](./group.md)
  Clear the (POSIX) group ID.
- [static var groupUUID: CFFileSecurityClearOptions](./groupuuid.md)
  Clear the group UUID (for the access control list).
- [static var mode: CFFileSecurityClearOptions](./mode.md)
  Clear the file’s mode (POSIX permissions).
- [static var ownerUUID: CFFileSecurityClearOptions](./owneruuid.md)
  Clear the owner UUID (for the access control list).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/owner)*