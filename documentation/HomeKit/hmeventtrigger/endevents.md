# endEvents

**Framework**: HomeKit  
**Kind**: property

The events associated with the end of scene represented by this trigger.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var endEvents: [HMEvent] { get }
```

#### Discussion

HomeKit restores the previously active scene when the events in this array trigger. For example, you can use end events to execute a scene for 10 minutes by specifying an [`HMDurationEvent`](hmdurationevent.md) in the list of [`endEvents`](hmeventtrigger/endevents.md). This restores the previous scene when the duration event triggers.

You can also use [`HMCharacteristicEvent`](hmcharacteristicevent.md) and [`HMCharacteristicThresholdRangeEvent`](hmcharacteristicthresholdrangeevent.md) objects as end events.

## See Also

- [func updateEndEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateendevents(_:completionhandler:).md)
  Updates the set of end events associated with the event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/endevents)*