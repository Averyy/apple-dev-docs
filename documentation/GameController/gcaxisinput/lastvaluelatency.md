# lastValueLatency

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time in seconds between the last value change and the current time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastValueLatency: TimeInterval { get }
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

- [var value: Float](gcaxisinput/value.md)
  The value along the axis, in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxisInput, Float) -> Void)?](gcaxisinput/valuedidchangehandler.md)
  The block that the input object calls when the value changes.
- [var lastValueTimestamp: TimeInterval](gcaxisinput/lastvaluetimestamp.md)
  The time of the most recent value change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxisinput/lastvaluelatency)*