# duration

**Framework**: Core Haptics  
**Kind**: property

The duration of the haptic event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var duration: TimeInterval { get set }
```

#### Discussion

The maximum duration of a continuous haptic event is 30 seconds.

## See Also

- [var eventParameters: [CHHapticEventParameter]](chhapticevent/eventparameters.md)
  An array of event parameters, possibly empty.
- [CHHapticEvent.ParameterID](chhapticevent/parameterid.md)
  An identifier for an event parameter.
- [var relativeTime: TimeInterval](chhapticevent/relativetime.md)
  The start time of the event, relative to other events in the same pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/duration)*