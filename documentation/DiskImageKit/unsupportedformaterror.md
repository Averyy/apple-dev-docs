# UnsupportedFormatError

**Framework**: DiskImageKit  
**Kind**: struct

The disk image format isn’t supported.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct UnsupportedFormatError
```

## Topics

### Instance Properties
- [let underlyingError: any Error](unsupportedformaterror/underlyingerror.md)
  The underlying error with additional diagnostic details.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct IncompatibleStackingError](incompatiblestackingerror.md)
  The appended layer isn’t compatible with the existing stack.
- [struct InvalidBlockCountError](invalidblockcounterror.md)
  The block count specified for the disk image is invalid (zero or negative).
- [struct CorruptedImageError](corruptedimageerror.md)
  The disk image is corrupted or contains invalid data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/unsupportedformaterror)*