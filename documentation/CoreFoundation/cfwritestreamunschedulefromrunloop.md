# CFWriteStreamUnscheduleFromRunLoop(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a stream from a particular run loop.

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
func CFWriteStreamUnscheduleFromRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

## Parameters

- `stream`: The stream to remove.
- `runLoop`: The run loop from which to remove  .
- `runLoopMode`: The run loop mode of   from which to remove  .

## See Also

- [func CFWriteStreamScheduleWithRunLoop(CFWriteStream!, CFRunLoop!, CFRunLoopMode!)](cfwritestreamschedulewithrunloop(_:_:_:).md)
  Schedules a stream into a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamunschedulefromrunloop(_:_:_:))*