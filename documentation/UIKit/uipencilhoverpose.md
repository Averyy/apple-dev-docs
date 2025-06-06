# UIPencilHoverPose

**Framework**: UIKit  
**Kind**: class

An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+

## Declaration

```swift
@MainActor
class UIPencilHoverPose
```

#### Overview

Use the hover pose of Apple Pencil to support more complex interactions in response to a double tap or squeeze. Information about the hover pose — such as azimuth, altitude, and hover distance — is available when a person holds a supported model of Apple Pencil close to the screen during a double tap or squeeze.

The following code example shows how to use the [`location`](uipencilhoverpose/location.md) of a hover pose to present a contextual palette near the tip of Apple Pencil.

```swift
func pencilInteraction(_ interaction: UIPencilInteraction,
                       didReceiveSqueeze squeeze: UIPencilInteraction.Squeeze) {
    let preferredAction = UIPencilInteraction.preferredSqueezeAction
    
    if preferredAction == .showContextualPalette, squeeze.phase == .ended {
        if let anchorPoint = squeeze.hoverPose?.location {
            presentContextualPalette(atLocation: anchorPoint)
        }
    }
}
```

## Topics

### Getting the hover characteristics
- [var location: CGPoint](uipencilhoverpose/location.md)
  The location of an Apple Pencil above the view’s bounds, in view’s coordinate space.
- [var altitudeAngle: CGFloat](uipencilhoverpose/altitudeangle.md)
  A value that represents the altitude angle of Apple Pencil.
- [var azimuthAngle: CGFloat](uipencilhoverpose/azimuthangle.md)
  A value that represents the azimuth angle of Apple Pencil.
- [var azimuthUnitVector: CGVector](uipencilhoverpose/azimuthunitvector.md)
  A value that represents the azimuth unit vector of Apple Pencil in the specified view.
- [var rollAngle: CGFloat](uipencilhoverpose/rollangle.md)
  A value that represents the barrel-roll angle of Apple Pencil.
- [var zOffset: CGFloat](uipencilhoverpose/zoffset.md)
  A value that represents the normalized distance between the screen and Apple Pencil.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPencilInteraction](uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [protocol UIPencilInteractionDelegate](uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [UIPencilInteraction.Tap](uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [UIPencilInteraction.Phase](uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilhoverpose)*