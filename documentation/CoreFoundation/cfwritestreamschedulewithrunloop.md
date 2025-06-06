# CFWriteStreamScheduleWithRunLoop(_:_:_:)

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
func CFWriteStreamScheduleWithRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

#### Discussion

After scheduling `stream` into a run loop, its client (set with [`CFWriteStreamSetClient(_:_:_:_:)`](cfwritestreamsetclient(_:_:_:_:).md)) is notified when various events happen with the stream, such as when it finishes opening, when it can accept new bytes, and when an error occurs. A stream can be scheduled into multiple run loops and run loop modes. Use [`CFWriteStreamUnscheduleFromRunLoop(_:_:_:)`](cfwritestreamunschedulefromrunloop(_:_:_:).md) to later remove `stream` from the run loop.

## Parameters

- `stream`: The stream to schedule.
- `runLoop`: The run loop in which to schedule  .
- `runLoopMode`: The run loop mode of   in which to schedule  .

## See Also

- [func CFWriteStreamUnscheduleFromRunLoop(CFWriteStream!, CFRunLoop!, CFRunLoopMode!)](cfwritestreamunschedulefromrunloop(_:_:_:).md)
  Removes a stream from a particular run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamschedulewithrunloop(_:_:_:))*