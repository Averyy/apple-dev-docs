# gid

**Framework**: FSKit  
**Kind**: property

The group identifier.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var gid: UInt32 { get set }
```

## See Also

- [var type: FSItem.ItemType](fsitem/attributes/type.md)
  The item type, such as a regular file, directory, or symbolic link.
- [var mode: UInt32](fsitem/attributes/mode.md)
  The mode of the item.
- [var linkCount: UInt32](fsitem/attributes/linkcount.md)
  The number of hard links to the item.
- [var uid: UInt32](fsitem/attributes/uid.md)
  The user identifier.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/gid)*