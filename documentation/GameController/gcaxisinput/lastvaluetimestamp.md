# lastValueTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time of the most recent value change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastValueTimestamp: TimeInterval { get }
```

#### Discussion

This property isn’t a specific date and time. To determine the time between value changes, subtract a previous time from the current time.

## See Also

- [var value: Float](gcaxisinput/value.md)
  The value along the axis, in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxisInput, Float) -> Void)?](gcaxisinput/valuedidchangehandler.md)
  The block that the input object calls when the value changes.
- [var lastValueLatency: TimeInterval](gcaxisinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxisinput/lastvaluetimestamp)*