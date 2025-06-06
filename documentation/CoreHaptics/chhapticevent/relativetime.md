# relativeTime

**Framework**: Core Haptics  
**Kind**: property

The start time of the event, relative to other events in the same pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var relativeTime: TimeInterval { get set }
```

#### Discussion

A [`relativeTime`](chhapticparametercurve/relativetime.md) of zero indicates immediate playback. Another haptic event starting one second later would have a [`relativeTime`](chhapticevent/relativetime.md) of `1`.

## See Also

- [var eventParameters: [CHHapticEventParameter]](chhapticevent/eventparameters.md)
  An array of event parameters, possibly empty.
- [CHHapticEvent.ParameterID](chhapticevent/parameterid.md)
  An identifier for an event parameter.
- [var duration: TimeInterval](chhapticevent/duration.md)
  The duration of the haptic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/relativetime)*