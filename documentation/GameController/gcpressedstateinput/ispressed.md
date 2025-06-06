# isPressed

**Framework**: Game Controller  
**Kind**: property  
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

## See Also

- [var lastPressedStateTimestamp: TimeInterval](gcpressedstateinput/lastpressedstatetimestamp.md)
  The time of the most recent press state change.
- [var lastPressedStateLatency: TimeInterval](gcpressedstateinput/lastpressedstatelatency.md)
  The time in seconds between the last press state change and the current time.
- [var pressedDidChangeHandler: ((any GCPhysicalInputElement, any GCPressedStateInput, Bool) -> Void)?](gcpressedstateinput/presseddidchangehandler.md)
  The block that the profile calls when an element’s press state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcpressedstateinput/ispressed)*