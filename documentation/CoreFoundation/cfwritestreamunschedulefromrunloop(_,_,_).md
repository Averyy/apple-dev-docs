# CFWriteStreamUnscheduleFromRunLoop(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a stream from a particular run loop.

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
func CFWriteStreamUnscheduleFromRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

```c
extern void CFWriteStreamUnscheduleFromRunLoop(CFWriteStreamRef stream, CFRunLoopRef runLoop, CFRunLoopMode runLoopMode);
```

## Parameters

- `stream`: The stream to remove.
- `runLoop`: The run loop from which to remove `stream`.
- `runLoopMode`: The run loop mode of `runLoop` from which to remove `stream`.

## See Also

### Scheduling a Write Stream
- [func CFWriteStreamScheduleWithRunLoop(CFWriteStream!, CFRunLoop!, CFRunLoopMode!)](./cfwritestreamschedulewithrunloop%28_,_,_%29.md)
  Schedules a stream into a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamunschedulefromrunloop(_:_:_:))*