# delegate

**Framework**: UIKit  
**Kind**: property

An object that configures and controls a drag interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIDragInteractionDelegate)? { get }
```

## See Also

- [var allowsSimultaneousRecognitionDuringLift: Bool](uidraginteraction/allowssimultaneousrecognitionduringlift.md)
  A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.
- [protocol UIDragInteractionDelegate](uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/delegate)*