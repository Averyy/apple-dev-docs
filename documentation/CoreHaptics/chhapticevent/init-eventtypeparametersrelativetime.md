# init(eventType:parameters:relativeTime:)

**Framework**: Core Haptics  
**Kind**: init

Initializes a haptic event of the specified type, parameters, and start time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(eventType type: CHHapticEvent.EventType, parameters eventParams: [CHHapticEventParameter], relativeTime time: TimeInterval)
```

## Parameters

- `type`: The type of the haptic event: transient or continuous.
- `eventParams`: An array of event parameters to characterize the haptic event.
- `time`: The start time of the haptic event, in seconds.

## See Also

- [init(audioResourceID: CHHapticAudioResourceID, parameters: [CHHapticEventParameter], relativeTime: TimeInterval)](chhapticevent/init(audioresourceid:parameters:relativetime:).md)
  Initializes a haptic event from a previously loaded audio resource, specifying event parameters and start time.
- [init(audioResourceID: CHHapticAudioResourceID, parameters: [CHHapticEventParameter], relativeTime: TimeInterval, duration: TimeInterval)](chhapticevent/init(audioresourceid:parameters:relativetime:duration:).md)
  Initializes a haptic event from a previously loaded audio resource, specifying event parameters, start time, and duration.
- [init(eventType: CHHapticEvent.EventType, parameters: [CHHapticEventParameter], relativeTime: TimeInterval, duration: TimeInterval)](chhapticevent/init(eventtype:parameters:relativetime:duration:).md)
  Initializes a haptic event of the specified type, parameters, start time, and duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/init(eventtype:parameters:relativetime:))*