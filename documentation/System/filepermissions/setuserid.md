# setUserID

**Framework**: System  
**Kind**: property

Indicates that the file is executed as the owner.

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
static var setUserID: FilePermissions { get }
```

#### Discussion

For more information, see the `setuid(2)` man page.

## See Also

- [static var setGroupID: FilePermissions](filepermissions/setgroupid.md)
  Indicates that the file is executed as the group.
- [static var saveText: FilePermissions](filepermissions/savetext.md)
  Indicates that executable’s text segment should be kept in swap space even after it exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions/setuserid)*