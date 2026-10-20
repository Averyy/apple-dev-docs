# mode

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Clear the file’s mode (POSIX permissions).

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
static var mode: CFFileSecurityClearOptions { get }
```

```c
kCFFileSecurityClearMode
```

## See Also

### Constants
- [static var accessControlList: CFFileSecurityClearOptions](./accesscontrollist.md)
  Clear the access control list.
- [static var group: CFFileSecurityClearOptions](./group.md)
  Clear the (POSIX) group ID.
- [static var groupUUID: CFFileSecurityClearOptions](./groupuuid.md)
  Clear the group UUID (for the access control list).
- [static var owner: CFFileSecurityClearOptions](./owner.md)
  Clear the (POSIX) owner ID.
- [static var ownerUUID: CFFileSecurityClearOptions](./owneruuid.md)
  Clear the owner UUID (for the access control list).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/mode)*