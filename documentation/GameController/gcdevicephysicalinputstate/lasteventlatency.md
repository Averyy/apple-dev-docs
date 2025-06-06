# lastEventLatency

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time in seconds between the last event and the current time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastEventLatency: TimeInterval { get }
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event. If the host goes to sleep between when the event occurs and when you get this property, the value may not be accurate.

## See Also

- [var lastEventTimestamp: TimeInterval](gcdevicephysicalinputstate/lasteventtimestamp.md)
  The time of the most recent event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate/lasteventlatency)*