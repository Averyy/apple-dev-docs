# CFReadStreamUnscheduleFromRunLoop(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a read stream from a given run loop.

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
func CFReadStreamUnscheduleFromRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

## Parameters

- `stream`: The stream to unschedule.
- `runLoop`: The run loop from which to remove  .
- `runLoopMode`: The run loop mode of   from which to remove  .

## See Also

- [func CFReadStreamScheduleWithRunLoop(CFReadStream!, CFRunLoop!, CFRunLoopMode!)](cfreadstreamschedulewithrunloop(_:_:_:).md)
  Schedules a stream into a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamunschedulefromrunloop(_:_:_:))*