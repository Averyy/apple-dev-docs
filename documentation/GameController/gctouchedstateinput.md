# GCTouchedStateInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties for an element that has touch state input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCTouchedStateInput : NSObjectProtocol
```

## Topics

### Getting change information
- [var isTouched: Bool](gctouchedstateinput/istouched.md)
  A Boolean value that indicates whether the user touches the button.
- [var lastTouchedStateTimestamp: TimeInterval](gctouchedstateinput/lasttouchedstatetimestamp.md)
  The time of the most recent touch state change.
- [var lastTouchedStateLatency: TimeInterval](gctouchedstateinput/lasttouchedstatelatency.md)
  The time in seconds between the last touch state change and the current time.
- [var touchedDidChangeHandler: ((any GCPhysicalInputElement, any GCTouchedStateInput, Bool) -> Void)?](gctouchedstateinput/toucheddidchangehandler.md)
  A block that the element calls when its touch value changes.
### Getting user actions
- [var sources: Set<AnyHashable>](gctouchedstateinput/sources.md)
  One or more physical actions the user performs to manipulate the input.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GCPressedStateInput](gcpressedstateinput.md)
  The common properties for an element that has press state input, such as input from a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput)*