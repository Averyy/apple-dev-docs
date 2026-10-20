# isPressed

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the user presses the button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isPressed: Bool { get }
```

```objc
@property (readonly, getter=isPressed) BOOL pressed;
```

## See Also

### Getting change information
- [var lastPressedStateTimestamp: TimeInterval](./lastpressedstatetimestamp.md)
  The time of the most recent press state change.
- [var lastPressedStateLatency: TimeInterval](./lastpressedstatelatency.md)
  The time in seconds between the last press state change and the current time.
- [var pressedDidChangeHandler: ((any GCPhysicalInputElement, any GCPressedStateInput, Bool) -> Void)?](./presseddidchangehandler.md)
  The block that the profile calls when an element’s press state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcpressedstateinput/ispressed)*