# FSItem.Attributes

**Framework**: FSKit  
**Kind**: class

Attributes of an item, such as size, creation and modification times, and user and group identifiers.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class Attributes
```

## Topics

### Validating and invalidating attributes
- [func isValid(FSItem.Attribute) -> Bool](fsitem/attributes/isvalid(_:).md)
  Returns a Boolean value that indicates whether the attribute is valid.
- [func invalidateAllProperties()](fsitem/attributes/invalidateallproperties.md)
  Marks all attributes inactive.
### Working with identifier attributes
- [var fileID: FSItem.Identifier](fsitem/attributes/fileid.md)
  The item’s file identifier.
- [var parentID: FSItem.Identifier](fsitem/attributes/parentid.md)
  The identifier of the item’s parent.
### Working with metadata attributes
- [var type: FSItem.ItemType](fsitem/attributes/type.md)
  The item type, such as a regular file, directory, or symbolic link.
- [var mode: UInt32](fsitem/attributes/mode.md)
  The mode of the item.
- [var linkCount: UInt32](fsitem/attributes/linkcount.md)
  The number of hard links to the item.
- [var uid: UInt32](fsitem/attributes/uid.md)
  The user identifier.
- [var gid: UInt32](fsitem/attributes/gid.md)
  The group identifier.
- [var flags: UInt32](fsitem/attributes/flags.md)
  The item’s behavior flags.
- [var size: UInt64](fsitem/attributes/size.md)
  The item’s size.
- [var allocSize: UInt64](fsitem/attributes/allocsize.md)
  The item’s allocated size.
- [var supportsLimitedXAttrs: Bool](fsitem/attributes/supportslimitedxattrs.md)
  A Boolean value that indicates whether the item supports a limited set of extended attributes.
- [var inhibitKernelOffloadedIO: Bool](fsitem/attributes/inhibitkerneloffloadedio.md)
  A Boolean value that indicates whether the file system overrides the per-volume settings for kernel offloaded I/O for a specific file.
### Working with time attributes
- [var accessTime: timespec](fsitem/attributes/accesstime.md)
  The item’s last-accessed time.
- [var modifyTime: timespec](fsitem/attributes/modifytime.md)
  The item’s last-modified time.
- [var changeTime: timespec](fsitem/attributes/changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](fsitem/attributes/birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](fsitem/attributes/backuptime.md)
  The item’s last-backup time.
- [var addedTime: timespec](fsitem/attributes/addedtime.md)
  The item’s added time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [FSItem.GetAttributesRequest](fsitem/getattributesrequest.md)
  A request to get attributes from an item.
- [FSItem.SetAttributesRequest](fsitem/setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes)*