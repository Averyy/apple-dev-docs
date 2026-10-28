# lastPressedStateLatency

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The time in seconds between the last press state change and the current time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastPressedStateLatency: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval lastPressedStateLatency;
```

## Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

### Getting change information
- [var isPressed: Bool](./ispressed.md)
  A Boolean value that indicates whether the user presses the button.
- [var lastPressedStateTimestamp: TimeInterval](./lastpressedstatetimestamp.md)
  The time of the most recent press state change.
- [var pressedDidChangeHandler: ((any GCPhysicalInputElement, any GCPressedStateInput, Bool) -> Void)?](./presseddidchangehandler.md)
  The block that the profile calls when an element’s press state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcpressedstateinput/lastpressedstatelatency)*