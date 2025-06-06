# value

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The value along the axis, in unit coordinates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var value: Float { get }
```

## See Also

- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxisInput, Float) -> Void)?](gcaxisinput/valuedidchangehandler.md)
  The block that the input object calls when the value changes.
- [var lastValueTimestamp: TimeInterval](gcaxisinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gcaxisinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxisinput/value)*