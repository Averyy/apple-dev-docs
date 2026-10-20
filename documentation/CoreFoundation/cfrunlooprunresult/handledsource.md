# CFRunLoopRunResult.handledSource

**Framework**: Core Foundation  
**Kind**: case  
**Role**: Case

A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case handledSource
```

```c
kCFRunLoopRunHandledSource
```

## See Also

### Constants
- [CFRunLoopRunResult.finished](./finished.md)
  The running run loop mode has no sources or timers to process.
- [CFRunLoopRunResult.stopped](./stopped.md)
  [`CFRunLoopStop(_:)`](../cfrunloopstop%28_%29.md) was called on the run loop.
- [CFRunLoopRunResult.timedOut](./timedout.md)
  The specified time interval for running the run loop has passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/handledsource)*