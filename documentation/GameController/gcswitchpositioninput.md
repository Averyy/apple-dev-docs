# GCSwitchPositionInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties of inputs that switch between two or more positions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCSwitchPositionInput : NSObjectProtocol
```

## Topics

### Getting the characteristics
- [var positionRange: NSRange](gcswitchpositioninput/positionrange.md)
  The range of possible values for the switch.
- [var isSequential: Bool](gcswitchpositioninput/issequential.md)
  A Boolean value that indicates whether the position change is sequential.
- [var canWrap: Bool](gcswitchpositioninput/canwrap.md)
  A Boolean value that indicates whether the position value wraps when it reaches the range’s minimum or maximum value.
### Getting the position
- [var position: Int](gcswitchpositioninput/position.md)
  The position of the switch.
- [var positionDidChangeHandler: ((any GCPhysicalInputElement, any GCSwitchPositionInput, Int) -> Void)?](gcswitchpositioninput/positiondidchangehandler.md)
  The block that the profile calls when the value of the switch changes.
- [var lastPositionTimestamp: TimeInterval](gcswitchpositioninput/lastpositiontimestamp.md)
  A timestamp for when the profile reports the last position.
- [var lastPositionLatency: TimeInterval](gcswitchpositioninput/lastpositionlatency.md)
  The time in seconds between the current and previous positions.
### Getting user actions
- [var sources: Set<AnyHashable>](gcswitchpositioninput/sources.md)
  One or more physical actions the user performs to manipulate the input.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCSteeringWheelElement](gcsteeringwheelelement.md)
  The element that represents the wheel of a racing wheel controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput)*