# CFRunLoopRunResult.finished

**Framework**: Core Foundation  
**Kind**: case

The running run loop mode has no sources or timers to process.

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
case finished
```

## See Also

- [CFRunLoopRunResult.stopped](cfrunlooprunresult/stopped.md)
  [`CFRunLoopStop(_:)`](cfrunloopstop(_:).md) was called on the run loop.
- [CFRunLoopRunResult.timedOut](cfrunlooprunresult/timedout.md)
  The specified time interval for running the run loop has passed.
- [CFRunLoopRunResult.handledSource](cfrunlooprunresult/handledsource.md)
  A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/finished)*