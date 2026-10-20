# AVAssetWriter.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Values that indicate the state of an asset writer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Status
```

```c
enum AVAssetWriterStatus : NSInteger;
```

## Topics

### Status values
- [AVAssetWriter.Status.unknown](./status-swift.enum/unknown.md)
  The asset writer’s status isn’t known.
- [AVAssetWriter.Status.writing](./status-swift.enum/writing.md)
  The asset writer is writing.
- [AVAssetWriter.Status.completed](./status-swift.enum/completed.md)
  The asset writer finishes writing successfully.
- [AVAssetWriter.Status.failed](./status-swift.enum/failed.md)
  The asset writer fails to write the output file.
- [AVAssetWriter.Status.cancelled](./status-swift.enum/cancelled.md)
  The asset writer canceled the writing operation.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting writing status
- [var status: AVAssetWriter.Status](./status-swift.property.md)
  The status of writing samples to the output file.
- [var error: (any Error)?](./error.md)
  An error object that describes an asset-writing failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.enum)*