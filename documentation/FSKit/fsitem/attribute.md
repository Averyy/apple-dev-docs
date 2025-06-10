# FSItem.Attribute

**Framework**: FSKit  
**Kind**: struct

A value that indicates a set of item attributes to get or set.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct Attribute
```

#### Overview

This type is an option set in Swift. In Objective-C, you use the cases of this enumeration to create a bit field.

## Topics

### Working with identifier attributes
- [static var fileID: FSItem.Attribute](fsitem/attribute/fileid.md)
  The file ID attribute.
- [static var parentID: FSItem.Attribute](fsitem/attribute/parentid.md)
  The parent ID attribute.
### Working with metadata attributes
- [static var type: FSItem.Attribute](fsitem/attribute/type.md)
  The type attribute.
- [static var mode: FSItem.Attribute](fsitem/attribute/mode.md)
  The mode attribute.
- [static var linkCount: FSItem.Attribute](fsitem/attribute/linkcount.md)
  The link count attribute.
- [static var uid: FSItem.Attribute](fsitem/attribute/uid.md)
  The user ID (uid) attribute.
- [static var gid: FSItem.Attribute](fsitem/attribute/gid.md)
  The group ID (gid) attribute.
- [static var flags: FSItem.Attribute](fsitem/attribute/flags.md)
  The flags attribute.
- [static var size: FSItem.Attribute](fsitem/attribute/size.md)
  The size attribute.
- [static var allocSize: FSItem.Attribute](fsitem/attribute/allocsize.md)
  The allocated size attribute.
- [static var supportsLimitedXAttrs: FSItem.Attribute](fsitem/attribute/supportslimitedxattrs.md)
  The supports limited extended attributes attribute.
- [static var inhibitKernelOffloadedIO: FSItem.Attribute](fsitem/attribute/inhibitkerneloffloadedio.md)
  The inhibit kernel offloaded I/O attribute.
### Working with time attributes
- [static var accessTime: FSItem.Attribute](fsitem/attribute/accesstime.md)
  The last-accessed time attribute.
- [static var modifyTime: FSItem.Attribute](fsitem/attribute/modifytime.md)
  The last-modified time attribute.
- [static var changeTime: FSItem.Attribute](fsitem/attribute/changetime.md)
  The last-changed time attribute.
- [static var birthTime: FSItem.Attribute](fsitem/attribute/birthtime.md)
  The creation time attribute.
- [static var backupTime: FSItem.Attribute](fsitem/attribute/backuptime.md)
  The backup time attribute.
- [static var addedTime: FSItem.Attribute](fsitem/attribute/addedtime.md)
  The time added attribute.
### Working with raw values
- [init(rawValue: Int)](fsitem/attribute/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsitem/attribute/equatable-implementations.md)
- [OptionSet Implementations](fsitem/attribute/optionset-implementations.md)
- [SetAlgebra Implementations](fsitem/attribute/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var wantedAttributes: FSItem.Attribute](fsitem/getattributesrequest/wantedattributes.md)
  The attributes requested by the request.
- [func isAttributeWanted(FSItem.Attribute) -> Bool](fsitem/getattributesrequest/isattributewanted(_:).md)
  A method that indicates whether the request wants given attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attribute)*