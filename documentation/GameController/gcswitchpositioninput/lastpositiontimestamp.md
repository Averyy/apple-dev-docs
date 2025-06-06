# lastPositionTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

A timestamp for when the profile reports the last position.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastPositionTimestamp: TimeInterval { get }
```

#### Discussion

This property isn’t a specific date and time. To determine the time between positions, subtract a previous value from the current value.

## See Also

- [var position: Int](gcswitchpositioninput/position.md)
  The position of the switch.
- [var positionDidChangeHandler: ((any GCPhysicalInputElement, any GCSwitchPositionInput, Int) -> Void)?](gcswitchpositioninput/positiondidchangehandler.md)
  The block that the profile calls when the value of the switch changes.
- [var lastPositionLatency: TimeInterval](gcswitchpositioninput/lastpositionlatency.md)
  The time in seconds between the current and previous positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/lastpositiontimestamp)*