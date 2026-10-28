# positionDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The block that the profile calls when the value of the switch changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var positionDidChangeHandler: ((any GCPhysicalInputElement, any GCSwitchPositionInput, Int) -> Void)? { get set }
```

```objc
@property (atomic, copy, nullable) void (^positionDidChangeHandler)(id<GCPhysicalInputElement>element, id<GCSwitchPositionInput>input, NSInteger position);
```

## Discussion

The block’s parameters are:

- **`element`**: The element whose position changes.
- **`input`**: The input object that represents the position.
- **`position`**: The new position of the element.

## See Also

### Getting the position
- [var position: Int](./position.md)
  The position of the switch.
- [var lastPositionTimestamp: TimeInterval](./lastpositiontimestamp.md)
  A timestamp for when the profile reports the last position.
- [var lastPositionLatency: TimeInterval](./lastpositionlatency.md)
  The time in seconds between the current and previous positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/positiondidchangehandler)*