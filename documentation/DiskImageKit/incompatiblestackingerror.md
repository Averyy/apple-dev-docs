# IncompatibleStackingError

**Framework**: DiskImageKit  
**Kind**: struct

The appended layer isn’t compatible with the existing stack.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct IncompatibleStackingError
```

## Topics

### Instance Properties
- [let reason: String](incompatiblestackingerror/reason.md)
  A description of why the stacking operation failed.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct InvalidBlockCountError](invalidblockcounterror.md)
  The block count specified for the disk image is invalid (zero or negative).
- [struct CorruptedImageError](corruptedimageerror.md)
  The disk image is corrupted or contains invalid data.
- [struct UnsupportedFormatError](unsupportedformaterror.md)
  The disk image format isn’t supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/incompatiblestackingerror)*