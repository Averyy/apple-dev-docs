# lastValueTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time of the most recent value change.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var lastValueTimestamp: TimeInterval { get }
```

#### Discussion

This property isn’t a specific date and time. To determine the time between value changes in seconds, subtract a previous time from the current time.

## See Also

- [var value: GCPoint2](gcaxis2dinput/value.md)
  The axis input represented as a normalized point in a two-dimensional coordinate system.
- [struct GCPoint2](gcpoint2.md)
  A structure that represents a normalized point in a two-dimensional coordinate system.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxis2DInput, GCPoint2) -> Void)?](gcaxis2dinput/valuedidchangehandler.md)
  The block that the axis element calls when its value changes.
- [var lastValueLatency: TimeInterval](gcaxis2dinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput/lastvaluetimestamp)*