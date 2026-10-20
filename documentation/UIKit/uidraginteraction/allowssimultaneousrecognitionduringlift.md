# allowsSimultaneousRecognitionDuringLift

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsSimultaneousRecognitionDuringLift: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsSimultaneousRecognitionDuringLift;
```

#### Discussion

If you set the [`allowsSimultaneousRecognitionDuringLift`](./allowssimultaneousrecognitionduringlift.md) property to [`true`](../../Swift/true.md), the interaction is canceled when another gesture is recognized. If you set this property to [`false`](../../Swift/false.md) (the default value), competing gesture recognizers fail.

> **Note**:  [`UILongPressGestureRecognizer`](../uilongpressgesturerecognizer.md) instances are always delayed and happen simultaneously during the lift activity.

## See Also

### Managing drag interactions
- [var delegate: (any UIDragInteractionDelegate)?](./delegate.md)
  An object that configures and controls a drag interaction.
- [protocol UIDragInteractionDelegate](../uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/allowssimultaneousrecognitionduringlift)*