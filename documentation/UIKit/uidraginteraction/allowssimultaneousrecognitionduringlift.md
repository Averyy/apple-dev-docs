# allowsSimultaneousRecognitionDuringLift

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsSimultaneousRecognitionDuringLift: Bool { get set }
```

#### Discussion

If you set the [`allowsSimultaneousRecognitionDuringLift`](uidraginteraction/allowssimultaneousrecognitionduringlift.md) property to [`true`](https://developer.apple.com/documentation/swift/true), the interaction is canceled when another gesture is recognized. If you set this property to [`false`](https://developer.apple.com/documentation/swift/false) (the default value), competing gesture recognizers fail.

> **Note**:  [`UILongPressGestureRecognizer`](uilongpressgesturerecognizer.md) instances are always delayed and happen simultaneously during the lift activity.

 [`UILongPressGestureRecognizer`](uilongpressgesturerecognizer.md) instances are always delayed and happen simultaneously during the lift activity.

## See Also

- [var delegate: (any UIDragInteractionDelegate)?](uidraginteraction/delegate.md)
  An object that configures and controls a drag interaction.
- [protocol UIDragInteractionDelegate](uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/allowssimultaneousrecognitionduringlift)*