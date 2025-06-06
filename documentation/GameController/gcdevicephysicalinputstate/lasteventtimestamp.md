# lastEventTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time of the most recent event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastEventTimestamp: TimeInterval { get }
```

#### Discussion

This property isn’t relative to any specific date and time. To determine the time between events, subtract a previous value of this property from the current value. You can also compare [`lastEventTimestamp`](gcdevicephysicalinputstate/lasteventtimestamp.md) properties of two different devices to determine which event occurs first.

## See Also

- [var lastEventLatency: TimeInterval](gcdevicephysicalinputstate/lasteventlatency.md)
  The time in seconds between the last event and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate/lasteventtimestamp)*