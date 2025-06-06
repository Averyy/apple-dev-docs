# saveText

**Framework**: System  
**Kind**: property

Indicates that executable’s text segment should be kept in swap space even after it exits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var saveText: FilePermissions { get }
```

#### Discussion

For more information, see the `chmod(2)` man page’s discussion of `S_ISVTX` (the sticky bit).

## See Also

- [static var setUserID: FilePermissions](filepermissions/setuserid.md)
  Indicates that the file is executed as the owner.
- [static var setGroupID: FilePermissions](filepermissions/setgroupid.md)
  Indicates that the file is executed as the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions/savetext)*