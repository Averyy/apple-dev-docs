# IncompatibleStackingError

**Framework**: DiskImageKit  
**Kind**: struct  
**Role**: Structure

The appended layer isn’t compatible with the existing stack.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct IncompatibleStackingError
```

## Topics

### Instance Properties
- [let reason: String](./incompatiblestackingerror/reason.md)
  A description of why the stacking operation failed.

## Relationships

### Conforms To
- [Error](../Swift/error.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct InvalidBlockCountError](./invalidblockcounterror.md)
  The block count specified for the disk image is invalid (zero or negative).
- [struct CorruptedImageError](./corruptedimageerror.md)
  The disk image is corrupted or contains invalid data.
- [struct UnsupportedFormatError](./unsupportedformaterror.md)
  The disk image format isn’t supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/incompatiblestackingerror)*