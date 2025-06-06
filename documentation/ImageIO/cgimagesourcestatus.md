# CGImageSourceStatus

**Framework**: Image I/O  
**Kind**: enum

The set of status values for images and image sources.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CGImageSourceStatus
```

#### Overview

The [`CGImageSourceGetStatus(_:)`](cgimagesourcegetstatus(_:).md) and [`CGImageSourceGetStatusAtIndex(_:_:)`](cgimagesourcegetstatusatindex(_:_:).md) functions return these values.

## Topics

### Status Values
- [CGImageSourceStatus.statusUnexpectedEOF](cgimagesourcestatus/statusunexpectedeof.md)
  The end of the file occurred unexpectedly.
- [CGImageSourceStatus.statusInvalidData](cgimagesourcestatus/statusinvaliddata.md)
  The data is not valid.
- [CGImageSourceStatus.statusUnknownType](cgimagesourcestatus/statusunknowntype.md)
  The image is an unknown type.
- [CGImageSourceStatus.statusReadingHeader](cgimagesourcestatus/statusreadingheader.md)
  The image source is reading the header.
- [CGImageSourceStatus.statusIncomplete](cgimagesourcestatus/statusincomplete.md)
  The operation is not complete
- [CGImageSourceStatus.statusComplete](cgimagesourcestatus/statuscomplete.md)
  The operation is complete.
### Initializers
- [init?(rawValue: Int32)](cgimagesourcestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func CGImageSourceGetStatus(CGImageSource) -> CGImageSourceStatus](cgimagesourcegetstatus(_:).md)
  Return the status of an image source.
- [func CGImageSourceGetStatusAtIndex(CGImageSource, Int) -> CGImageSourceStatus](cgimagesourcegetstatusatindex(_:_:).md)
  Returns the current status of an image at the specified location in the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcestatus)*