# lastEventTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) NSTimeInterval lastEventTimestamp;
```

#### Discussion

This property isn’t relative to any specific date and time. To determine the time between events, subtract a previous value of this property from the current value. You can also compare [`lastEventTimestamp`](./lasteventtimestamp.md) properties of two different devices to determine which event occurs first.

## See Also

### Getting change information
- [var lastEventLatency: TimeInterval](./lasteventlatency.md)
  The time in seconds between the last event and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate/lasteventtimestamp)*