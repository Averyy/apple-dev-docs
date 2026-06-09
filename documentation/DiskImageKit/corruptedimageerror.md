# CorruptedImageError

**Framework**: DiskImageKit  
**Kind**: struct

The disk image is corrupted or contains invalid data.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct CorruptedImageError
```

## Topics

### Instance Properties
- [let underlyingError: any Error](corruptedimageerror/underlyingerror.md)
  The underlying error with additional diagnostic details.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct IncompatibleStackingError](incompatiblestackingerror.md)
  The appended layer isn’t compatible with the existing stack.
- [struct InvalidBlockCountError](invalidblockcounterror.md)
  The block count specified for the disk image is invalid (zero or negative).
- [struct UnsupportedFormatError](unsupportedformaterror.md)
  The disk image format isn’t supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/corruptedimageerror)*