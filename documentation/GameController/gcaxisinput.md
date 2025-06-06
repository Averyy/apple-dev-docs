# GCAxisInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties of inputs that provide absolute values along an axis with a fixed origin.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCAxisInput : NSObjectProtocol
```

## Topics

### Getting the characteristics
- [var canWrap: Bool](gcaxisinput/canwrap.md)
  A Boolean value that indicates whether the value wraps when it reaches the range’s minimum or maximum value.
- [var isAnalog: Bool](gcaxisinput/isanalog.md)
  A Boolean value that indicates whether the input provides analog values.
### Getting the value
- [var value: Float](gcaxisinput/value.md)
  The value along the axis, in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxisInput, Float) -> Void)?](gcaxisinput/valuedidchangehandler.md)
  The block that the input object calls when the value changes.
- [var lastValueTimestamp: TimeInterval](gcaxisinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gcaxisinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.
### Getting user actions
- [var sources: Set<AnyHashable>](gcaxisinput/sources.md)
  One or more physical actions the user performs to manipulate the input.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCGearShifterElement](gcgearshifterelement.md)
  An element that represents either a pattern or a sequential gear shift.
- [protocol GCRelativeInput](gcrelativeinput.md)
  The common properties of inputs that provide positions along an axis that are relative to the previous position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxisinput)*