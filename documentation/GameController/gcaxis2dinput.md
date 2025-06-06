# GCAxis2DInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties of inputs that provide a normalized point in a two-dimensional coordinate system with a fixed origin.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol GCAxis2DInput : NSObjectProtocol
```

#### Overview

The normalized point with coordinates that range between `-1` and `1`. The origin `(0, 0)` represents the neutral state of the input.

## Topics

### Getting the characteristics
- [var canWrap: Bool](gcaxis2dinput/canwrap.md)
  A Boolean value that indicates whether the value wraps when it reaches the range’s minimum or maximum value.
- [var isAnalog: Bool](gcaxis2dinput/isanalog.md)
  A Boolean value that indicates whether the input provides analog values.
### Getting the value
- [var value: GCPoint2](gcaxis2dinput/value.md)
  The axis input represented as a normalized point in a two-dimensional coordinate system.
- [struct GCPoint2](gcpoint2.md)
  A structure that represents a normalized point in a two-dimensional coordinate system.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxis2DInput, GCPoint2) -> Void)?](gcaxis2dinput/valuedidchangehandler.md)
  The block that the axis element calls when its value changes.
- [var lastValueTimestamp: TimeInterval](gcaxis2dinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gcaxis2dinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.
### Getting user actions
- [var sources: Set<AnyHashable>](gcaxis2dinput/sources.md)
  One or more physical actions the user performs to manipulate the input.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var xAxis: any GCAxisInput](gcdirectionpadelement/xaxis.md)
  The input object that represents the x-axis on the directional pad.
- [var yAxis: any GCAxisInput](gcdirectionpadelement/yaxis.md)
  The input object that represents the y-axis on the directional pad.
- [var xyAxes: any GCAxis2DInput](gcdirectionpadelement/xyaxes.md)
  The location of the directional pad represented as a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput)*