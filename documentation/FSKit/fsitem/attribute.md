# FSItem.Attribute

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

A value that indicates a set of item attributes to get or set.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct Attribute
```

```c
enum FSItemAttribute : NSInteger;
```

## Overview

This type is an option set in Swift. In Objective-C, you use the cases of this enumeration to create a bit field.

## Topics

### Working with identifier attributes
- [static var fileID: FSItem.Attribute](./attribute/fileid.md)
  The file ID attribute.
- [static var parentID: FSItem.Attribute](./attribute/parentid.md)
  The parent ID attribute.
### Working with metadata attributes
- [static var type: FSItem.Attribute](./attribute/type.md)
  The type attribute.
- [static var mode: FSItem.Attribute](./attribute/mode.md)
  The mode attribute.
- [static var linkCount: FSItem.Attribute](./attribute/linkcount.md)
  The link count attribute.
- [static var uid: FSItem.Attribute](./attribute/uid.md)
  The user ID (uid) attribute.
- [static var gid: FSItem.Attribute](./attribute/gid.md)
  The group ID (gid) attribute.
- [static var flags: FSItem.Attribute](./attribute/flags.md)
  The flags attribute.
- [static var size: FSItem.Attribute](./attribute/size.md)
  The size attribute.
- [static var allocSize: FSItem.Attribute](./attribute/allocsize.md)
  The allocated size attribute.
- [static var supportsLimitedXAttrs: FSItem.Attribute](./attribute/supportslimitedxattrs.md)
  The supports limited extended attributes attribute.
- [static var inhibitKernelOffloadedIO: FSItem.Attribute](./attribute/inhibitkerneloffloadedio.md)
  The inhibit kernel offloaded I/O attribute.
### Working with time attributes
- [static var accessTime: FSItem.Attribute](./attribute/accesstime.md)
  The last-accessed time attribute.
- [static var modifyTime: FSItem.Attribute](./attribute/modifytime.md)
  The last-modified time attribute.
- [static var changeTime: FSItem.Attribute](./attribute/changetime.md)
  The last-changed time attribute.
- [static var birthTime: FSItem.Attribute](./attribute/birthtime.md)
  The creation time attribute.
- [static var backupTime: FSItem.Attribute](./attribute/backuptime.md)
  The backup time attribute.
- [static var addedTime: FSItem.Attribute](./attribute/addedtime.md)
  The time added attribute.
### Working with raw values
- [init(rawValue: Int)](./attribute/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Inspecting requested attributes
- [var wantedAttributes: FSItem.Attribute](./getattributesrequest/wantedattributes.md)
  The attributes requested by the request.
- [func isAttributeWanted(FSItem.Attribute) -> Bool](./getattributesrequest/isattributewanted%28_%29.md)
  A method that indicates whether the request wants given attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attribute)*