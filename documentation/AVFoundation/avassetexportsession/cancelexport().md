# cancelExport()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels the execution of an export session.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Task.cancel() instead

## Declaration

```swift
func cancelExport()
```

```objc
- (void) cancelExport;
```

## Discussion

Apple discourages the use of this symbol. Use [`cancel()`](../../Swift/task/cancel%28%29.md) on the [`Task`](../../Swift/task.md) or parent task that initiated the export instead.

## See Also

### Exporting media
- [- exportAsynchronouslyWithCompletionHandler:](./exportasynchronously%28completionhandler%29.md)
  Starts the asynchronous execution of an export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/cancelexport())*