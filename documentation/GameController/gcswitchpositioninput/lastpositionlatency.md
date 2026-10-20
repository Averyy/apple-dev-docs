# lastPositionLatency

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) NSTimeInterval lastPositionLatency;
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

### Getting the position
- [var position: Int](./position.md)
  The position of the switch.
- [var positionDidChangeHandler: ((any GCPhysicalInputElement, any GCSwitchPositionInput, Int) -> Void)?](./positiondidchangehandler.md)
  The block that the profile calls when the value of the switch changes.
- [var lastPositionTimestamp: TimeInterval](./lastpositiontimestamp.md)
  A timestamp for when the profile reports the last position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/lastpositionlatency)*