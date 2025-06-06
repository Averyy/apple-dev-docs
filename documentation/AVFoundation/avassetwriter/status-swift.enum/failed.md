# AVAssetWriter.Status.failed

**Framework**: AVFoundation  
**Kind**: case

The asset writer fails to write the output file.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case failed
```

#### Discussion

Query the [`error`](avassetwriter/error.md) property value to determine the cause of the failure.

## See Also

- [AVAssetWriter.Status.unknown](avassetwriter/status-swift.enum/unknown.md)
  The asset writer’s status isn’t known.
- [AVAssetWriter.Status.writing](avassetwriter/status-swift.enum/writing.md)
  The asset writer is writing.
- [AVAssetWriter.Status.completed](avassetwriter/status-swift.enum/completed.md)
  The asset writer finishes writing successfully.
- [AVAssetWriter.Status.cancelled](avassetwriter/status-swift.enum/cancelled.md)
  The asset writer canceled the writing operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.enum/failed)*