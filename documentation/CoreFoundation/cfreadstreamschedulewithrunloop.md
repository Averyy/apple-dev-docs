# CFReadStreamScheduleWithRunLoop(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Schedules a stream into a run loop.

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
func CFReadStreamScheduleWithRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

#### Discussion

After scheduling `stream` with a run loop, its client (set with [`CFReadStreamSetClient(_:_:_:_:)`](cfreadstreamsetclient(_:_:_:_:).md)) is notified when various events happen with the stream, such as when it finishes opening, when it has bytes available, and when an error occurs. A stream can be scheduled with multiple run loops and run loop modes. Use [`CFReadStreamUnscheduleFromRunLoop(_:_:_:)`](cfreadstreamunschedulefromrunloop(_:_:_:).md) to later remove `stream` from the run loop.

## Parameters

- `stream`: The stream to schedule.
- `runLoop`: The run loop with which to schedule  .
- `runLoopMode`: The run loop mode of   in which to schedule  .

## See Also

- [func CFReadStreamUnscheduleFromRunLoop(CFReadStream!, CFRunLoop!, CFRunLoopMode!)](cfreadstreamunschedulefromrunloop(_:_:_:).md)
  Removes a read stream from a given run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamschedulewithrunloop(_:_:_:))*