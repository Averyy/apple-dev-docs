# position

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The position of the switch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var position: Int { get }
```

```objc
@property (readonly) NSInteger position;
```

## See Also

### Getting the position
- [var positionDidChangeHandler: ((any GCPhysicalInputElement, any GCSwitchPositionInput, Int) -> Void)?](./positiondidchangehandler.md)
  The block that the profile calls when the value of the switch changes.
- [var lastPositionTimestamp: TimeInterval](./lastpositiontimestamp.md)
  A timestamp for when the profile reports the last position.
- [var lastPositionLatency: TimeInterval](./lastpositionlatency.md)
  The time in seconds between the current and previous positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/position)*