# valueDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The block that the input object calls when the value changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxisInput, Float) -> Void)? { get set }
```

#### Discussion

The block’s parameters are:

## See Also

- [var value: Float](gcaxisinput/value.md)
  The value along the axis, in unit coordinates.
- [var lastValueTimestamp: TimeInterval](gcaxisinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gcaxisinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxisinput/valuedidchangehandler)*