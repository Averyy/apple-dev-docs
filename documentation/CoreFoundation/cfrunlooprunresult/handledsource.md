# CFRunLoopRunResult.handledSource

**Framework**: Core Foundation  
**Kind**: case

A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case handledSource
```

## See Also

- [CFRunLoopRunResult.finished](cfrunlooprunresult/finished.md)
  The running run loop mode has no sources or timers to process.
- [CFRunLoopRunResult.stopped](cfrunlooprunresult/stopped.md)
  [`CFRunLoopStop(_:)`](cfrunloopstop(_:).md) was called on the run loop.
- [CFRunLoopRunResult.timedOut](cfrunlooprunresult/timedout.md)
  The specified time interval for running the run loop has passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/handledsource)*