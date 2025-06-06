# AVAssetWriter.Status

**Framework**: AVFoundation  
**Kind**: enum

Values that indicate the state of an asset writer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Status
```

## Topics

### Status Values
- [AVAssetWriter.Status.unknown](avassetwriter/status-swift.enum/unknown.md)
  The asset writer’s status isn’t known.
- [AVAssetWriter.Status.writing](avassetwriter/status-swift.enum/writing.md)
  The asset writer is writing.
- [AVAssetWriter.Status.completed](avassetwriter/status-swift.enum/completed.md)
  The asset writer finishes writing successfully.
- [AVAssetWriter.Status.failed](avassetwriter/status-swift.enum/failed.md)
  The asset writer fails to write the output file.
- [AVAssetWriter.Status.cancelled](avassetwriter/status-swift.enum/cancelled.md)
  The asset writer canceled the writing operation.
### Initializers
- [init?(rawValue: Int)](avassetwriter/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var status: AVAssetWriter.Status](avassetwriter/status-swift.property.md)
  The status of writing samples to the output file.
- [var error: (any Error)?](avassetwriter/error.md)
  An error object that describes an asset-writing failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.enum)*