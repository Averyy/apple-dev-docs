# flags

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The item’s behavior flags.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var flags: UInt32 { get set }
```

```objc
@property (nonatomic) uint32_t flags;
```

#### Discussion

See `st_flags` in `stat.h` for flag definitions.

## See Also

### Working with metadata attributes
- [var type: FSItem.ItemType](./type.md)
  The item type, such as a regular file, directory, or symbolic link.
- [var mode: UInt32](./mode.md)
  The mode of the item.
- [var linkCount: UInt32](./linkcount.md)
  The number of hard links to the item.
- [var uid: UInt32](./uid.md)
  The user identifier.
- [var gid: UInt32](./gid.md)
  The group identifier.
- [var size: UInt64](./size.md)
  The item’s size.
- [var allocSize: UInt64](./allocsize.md)
  The item’s allocated size.
- [var supportsLimitedXAttrs: Bool](./supportslimitedxattrs.md)
  A Boolean value that indicates whether the item supports a limited set of extended attributes.
- [var inhibitKernelOffloadedIO: Bool](./inhibitkerneloffloadedio.md)
  A Boolean value that indicates whether the file system overrides the per-volume settings for kernel offloaded I/O for a specific file. FSKit reads this value the first time the module reports attributes for a given file; It then sets the file’s kernel-offloaded-I/O routing accordingly. The routing stays in effect for the item’s lifetime; later changes are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/flags)*