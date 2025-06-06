# pressedDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The block that the profile calls when an element’s press state changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var pressedDidChangeHandler: ((any GCPhysicalInputElement, any GCPressedStateInput, Bool) -> Void)? { get set }
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Discussion

The block’s parameters are:

## See Also

- [var isPressed: Bool](gcpressedstateinput/ispressed.md)
  A Boolean value that indicates whether the user presses the button.
- [var lastPressedStateTimestamp: TimeInterval](gcpressedstateinput/lastpressedstatetimestamp.md)
  The time of the most recent press state change.
- [var lastPressedStateLatency: TimeInterval](gcpressedstateinput/lastpressedstatelatency.md)
  The time in seconds between the last press state change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcpressedstateinput/presseddidchangehandler)*