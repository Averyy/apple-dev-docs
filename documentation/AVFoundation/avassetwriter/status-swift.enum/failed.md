# AVAssetWriter.Status.failed

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The asset writer fails to write the output file.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case failed
```

```c
AVAssetWriterStatusFailed
```

## Discussion

Query the [`error`](../error.md) property value to determine the cause of the failure.

## See Also

### Status values
- [AVAssetWriter.Status.unknown](./unknown.md)
  The asset writer’s status isn’t known.
- [AVAssetWriter.Status.writing](./writing.md)
  The asset writer is writing.
- [AVAssetWriter.Status.completed](./completed.md)
  The asset writer finishes writing successfully.
- [AVAssetWriter.Status.cancelled](./cancelled.md)
  The asset writer canceled the writing operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.enum/failed)*