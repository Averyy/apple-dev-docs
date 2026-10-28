# value

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The axis input represented as a normalized point in a two-dimensional coordinate system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var value: GCPoint2 { get }
```

```objc
@property (readonly) GCPoint2 value;
```

## Discussion

The values of the coordinates range between `-1` and `1` where `(0,0)` is the fixed origin. Game Controller deadzones and saturates the values so there’s no value outside this range. A zero coordinate is inside the deadzone and any coordinate greater than or less than zero is outside the deadzone.

## See Also

### Getting the value
- [struct GCPoint2](../gcpoint2.md)
  A structure that represents a normalized point in a two-dimensional coordinate system.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxis2DInput, GCPoint2) -> Void)?](./valuedidchangehandler.md)
  The block that the axis element calls when its value changes.
- [var lastValueTimestamp: TimeInterval](./lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](./lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput/value)*