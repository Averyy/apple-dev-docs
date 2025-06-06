# GCPressedStateInput

**Framework**: Game Controller  
**Kind**: protocol

The common properties for an element that has press state input, such as input from a button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCPressedStateInput : NSObjectProtocol
```

## Topics

### Getting change information
- [var isPressed: Bool](gcpressedstateinput/ispressed.md)
  A Boolean value that indicates whether the user presses the button.
- [var lastPressedStateTimestamp: TimeInterval](gcpressedstateinput/lastpressedstatetimestamp.md)
  The time of the most recent press state change.
- [var lastPressedStateLatency: TimeInterval](gcpressedstateinput/lastpressedstatelatency.md)
  The time in seconds between the last press state change and the current time.
- [var pressedDidChangeHandler: ((any GCPhysicalInputElement, any GCPressedStateInput, Bool) -> Void)?](gcpressedstateinput/presseddidchangehandler.md)
  The block that the profile calls when an element’s press state changes.
### Getting user actions
- [var sources: Set<AnyHashable>](gcpressedstateinput/sources.md)
  One or more physical actions the user performs to manipulate the input.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GCTouchedStateInput](gctouchedstateinput.md)
  The common properties for an element that has touch state input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcpressedstateinput)*