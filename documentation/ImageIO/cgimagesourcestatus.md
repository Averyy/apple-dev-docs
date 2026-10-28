# CGImageSourceStatus

**Framework**: Image I/O  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CGImageSourceStatus : int32_t;
```

## Overview

The [`CGImageSourceGetStatus(_:)`](./cgimagesourcegetstatus%28_%29.md) and [`CGImageSourceGetStatusAtIndex(_:_:)`](./cgimagesourcegetstatusatindex%28_,_%29.md) functions return these values.

## Topics

### Status Values
- [CGImageSourceStatus.statusUnexpectedEOF](./cgimagesourcestatus/statusunexpectedeof.md)
  The end of the file occurred unexpectedly.
- [CGImageSourceStatus.statusInvalidData](./cgimagesourcestatus/statusinvaliddata.md)
  The data is not valid.
- [CGImageSourceStatus.statusUnknownType](./cgimagesourcestatus/statusunknowntype.md)
  The image is an unknown type.
- [CGImageSourceStatus.statusReadingHeader](./cgimagesourcestatus/statusreadingheader.md)
  The image source is reading the header.
- [CGImageSourceStatus.statusIncomplete](./cgimagesourcestatus/statusincomplete.md)
  The operation is not complete
- [CGImageSourceStatus.statusComplete](./cgimagesourcestatus/statuscomplete.md)
  The operation is complete.
### Initializers
- [init?(rawValue: Int32)](./cgimagesourcestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Image Status
- [func CGImageSourceGetStatus(CGImageSource) -> CGImageSourceStatus](./cgimagesourcegetstatus%28_%29.md)
  Return the status of an image source.
- [func CGImageSourceGetStatusAtIndex(CGImageSource, Int) -> CGImageSourceStatus](./cgimagesourcegetstatusatindex%28_,_%29.md)
  Returns the current status of an image at the specified location in the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcestatus)*