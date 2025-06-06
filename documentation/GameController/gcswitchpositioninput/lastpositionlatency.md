# lastPositionLatency

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time in seconds between the current and previous positions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastPositionLatency: TimeInterval { get }
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

- [var position: Int](gcswitchpositioninput/position.md)
  The position of the switch.
- [var positionDidChangeHandler: ((any GCPhysicalInputElement, any GCSwitchPositionInput, Int) -> Void)?](gcswitchpositioninput/positiondidchangehandler.md)
  The block that the profile calls when the value of the switch changes.
- [var lastPositionTimestamp: TimeInterval](gcswitchpositioninput/lastpositiontimestamp.md)
  A timestamp for when the profile reports the last position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/lastpositionlatency)*