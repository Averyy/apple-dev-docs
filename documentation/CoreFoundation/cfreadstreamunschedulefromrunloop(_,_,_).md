# CFReadStreamUnscheduleFromRunLoop(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a read stream from a given run loop.

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
func CFReadStreamUnscheduleFromRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

```c
extern void CFReadStreamUnscheduleFromRunLoop(CFReadStreamRef stream, CFRunLoopRef runLoop, CFRunLoopMode runLoopMode);
```

## Parameters

- `stream`: The stream to unschedule.
- `runLoop`: The run loop from which to remove `stream`.
- `runLoopMode`: The run loop mode of `runLoop` from which to remove `stream`.

## See Also

### Scheduling a Read Stream
- [func CFReadStreamScheduleWithRunLoop(CFReadStream!, CFRunLoop!, CFRunLoopMode!)](./cfreadstreamschedulewithrunloop%28_,_,_%29.md)
  Schedules a stream into a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamunschedulefromrunloop(_:_:_:))*