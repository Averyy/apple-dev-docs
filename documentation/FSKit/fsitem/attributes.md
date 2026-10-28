# FSItem.Attributes

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

Attributes of an item, such as size, creation and modification times, and user and group identifiers.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class Attributes
```

```objc
@interface FSItemAttributes : NSObject
```

## Overview

> ❗ **Important**: FSKit internally maintains a unique sequence number for each set of attributes to determine the most up-to-date set of attributes of a given [`FSItem`](../fsitem.md). To prevent an older set of attributes from having a newer sequence number, all attributes of a given [`FSItem.Attributes`](./attributes.md) object should be populated within the same synchronization context. This synchronization context should prevent any other thread from populating another [`FSItem.Attributes`](./attributes.md) object of the given [`FSItem`](../fsitem.md).

## Topics

### Validating and invalidating attributes
- [func isValid(FSItem.Attribute) -> Bool](./attributes/isvalid%28_%29.md)
  Returns a Boolean value that indicates whether the attribute is valid.
- [func invalidateAllProperties()](./attributes/invalidateallproperties%28%29.md)
  Marks all attributes inactive.
### Working with identifier attributes
- [var fileID: FSItem.Identifier](./attributes/fileid.md)
  The item’s file identifier.
- [var parentID: FSItem.Identifier](./attributes/parentid.md)
  The identifier of the item’s parent.
### Working with metadata attributes
- [var type: FSItem.ItemType](./attributes/type.md)
  The item type, such as a regular file, directory, or symbolic link.
- [var mode: UInt32](./attributes/mode.md)
  The mode of the item.
- [var linkCount: UInt32](./attributes/linkcount.md)
  The number of hard links to the item.
- [var uid: UInt32](./attributes/uid.md)
  The user identifier.
- [var gid: UInt32](./attributes/gid.md)
  The group identifier.
- [var flags: UInt32](./attributes/flags.md)
  The item’s behavior flags.
- [var size: UInt64](./attributes/size.md)
  The item’s size.
- [var allocSize: UInt64](./attributes/allocsize.md)
  The item’s allocated size.
- [var supportsLimitedXAttrs: Bool](./attributes/supportslimitedxattrs.md)
  A Boolean value that indicates whether the item supports a limited set of extended attributes.
- [var inhibitKernelOffloadedIO: Bool](./attributes/inhibitkerneloffloadedio.md)
  A Boolean value that indicates whether the file system overrides the per-volume settings for kernel offloaded I/O for a specific file. FSKit reads this value the first time the module reports attributes for a given file; It then sets the file’s kernel-offloaded-I/O routing accordingly. The routing stays in effect for the item’s lifetime; later changes are ignored.
### Working with time attributes
- [var accessTime: timespec](./attributes/accesstime.md)
  The item’s last-accessed time.
- [var modifyTime: timespec](./attributes/modifytime.md)
  The item’s last-modified time.
- [var changeTime: timespec](./attributes/changetime.md)
  The item’s last-changed time.
- [var birthTime: timespec](./attributes/birthtime.md)
  The item’s creation time.
- [var backupTime: timespec](./attributes/backuptime.md)
  The item’s last-backup time.
- [var addedTime: timespec](./attributes/addedtime.md)
  The item’s added time.
### Initializers
- [init?(coder: NSCoder)](./attributes/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [FSItem.SetAttributesRequest](./setattributesrequest.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Working with attributes
- [FSItem.GetAttributesRequest](./getattributesrequest.md)
  A request to get attributes from an item.
- [FSItem.SetAttributesRequest](./setattributesrequest.md)
  A request to set attributes on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes)*