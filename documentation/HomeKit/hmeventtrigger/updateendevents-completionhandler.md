# updateEndEvents(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the set of end events associated with the event trigger.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateEndEvents(_ endEvents: [HMEvent]) async throws
```

## Parameters

- `endEvents`: An array of events that replaces the end events on the trigger.
- `completion`: The block takes the following parameter:

## See Also

- [var endEvents: [HMEvent]](hmeventtrigger/endevents.md)
  The events associated with the end of scene represented by this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/updateendevents(_:completionhandler:))*