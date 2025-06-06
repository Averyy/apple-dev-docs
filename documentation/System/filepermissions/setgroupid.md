# setGroupID

**Framework**: System  
**Kind**: property

Indicates that the file is executed as the group.

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
static var setGroupID: FilePermissions { get }
```

#### Discussion

For more information, see the `setgid(2)` man page.

## See Also

- [static var setUserID: FilePermissions](filepermissions/setuserid.md)
  Indicates that the file is executed as the owner.
- [static var saveText: FilePermissions](filepermissions/savetext.md)
  Indicates that executable’s text segment should be kept in swap space even after it exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions/setgroupid)*