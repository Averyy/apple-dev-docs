# GCLinearInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties of inputs that provide values in unit coordinates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCLinearInput : NSObjectProtocol
```

## Topics

### Getting the characteristics
- [var canWrap: Bool](gclinearinput/canwrap.md)
  A Boolean value that indicates whether the input value wraps when it reaches the range’s minimum or maximum value.
- [var isAnalog: Bool](gclinearinput/isanalog.md)
  A Boolean value that indicates whether the input provides analog values.
### Getting the value
- [var value: Float](gclinearinput/value.md)
  The value in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCLinearInput, Float) -> Void)?](gclinearinput/valuedidchangehandler.md)
  The block that the profile calls when an element’s value changes.
- [var lastValueTimestamp: TimeInterval](gclinearinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gclinearinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.
### Getting user actions
- [var sources: Set<AnyHashable>](gclinearinput/sources.md)
  One or more physical actions the user performs to manipulate the input.
### Instance Properties
- [var physicalExtents: (any GCPhysicalInputExtents)?](gclinearinput/physicalextents.md)
  An object describing the physical extents of the input, if the input represents a physical unit of measurement.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gclinearinput)*