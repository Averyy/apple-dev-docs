# GCRelativeInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties of inputs that provide positions along an axis that are relative to the previous position.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCRelativeInput : NSObjectProtocol
```

## Topics

### Getting the characteristics
- [var isAnalog: Bool](gcrelativeinput/isanalog.md)
  A Boolean value that indicates whether the input provides analog values.
### Getting the delta value and timestamp
- [var delta: Float](gcrelativeinput/delta.md)
  The most recent amount of change in values that the profile records.
- [var deltaDidChangeHandler: ((any GCPhysicalInputElement, any GCRelativeInput, Float) -> Void)?](gcrelativeinput/deltadidchangehandler.md)
  The block that the profile calls when the element’s input changes.
- [var lastDeltaTimestamp: TimeInterval](gcrelativeinput/lastdeltatimestamp.md)
  A timestamp for when the profile reports the delta value.
- [var lastDeltaLatency: TimeInterval](gcrelativeinput/lastdeltalatency.md)
  The time in seconds between the current and the previous delta values.
### Getting user actions
- [var sources: Set<AnyHashable>](gcrelativeinput/sources.md)
  One or more physical actions the user performs to manipulate the input.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GCAxisInput](gcaxisinput.md)
  The common properties of inputs that provide absolute values along an axis with a fixed origin.
- [class GCGearShifterElement](gcgearshifterelement.md)
  An element that represents either a pattern or a sequential gear shift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrelativeinput)*