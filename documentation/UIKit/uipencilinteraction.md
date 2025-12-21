# UIPencilInteraction

**Framework**: UIKit  
**Kind**: class

An interaction that tells your app when a person double-taps or squeezes Apple Pencil.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- visionOS 26.2+

## Declaration

```swift
@MainActor
class UIPencilInteraction
```

#### Overview

People can interact with certain models of Apple Pencil with a double tap or squeeze. To detect the double tap or squeeze in your app, create a [`UIPencilInteraction`](uipencilinteraction.md) object with a corresponding [`delegate`](uipencilinteraction/delegate.md) object. Then, add the interaction to your app’s view. When a person double-taps or squeezes Apple Pencil, the interaction calls the delegate’s corresponding [`pencilInteraction(_:didReceiveTap:)`](uipencilinteractiondelegate/pencilinteraction(_:didreceivetap:).md) or [`pencilInteraction(_:didReceiveSqueeze:)`](uipencilinteractiondelegate/pencilinteraction(_:didreceivesqueeze:).md) method.

For more information, read [`Handling double taps from Apple Pencil`](https://developer.apple.com/documentation/ApplePencil/handling-double-taps-from-apple-pencil) and [`Handling squeezes from Apple Pencil`](https://developer.apple.com/documentation/ApplePencil/handling-squeezes-from-apple-pencil).

## Topics

### Creating interactions
- [init(delegate: any UIPencilInteractionDelegate)](uipencilinteraction/init(delegate:).md)
  Creates an interaction with the specified delegate.
### Handling interactions
- [var delegate: (any UIPencilInteractionDelegate)?](uipencilinteraction/delegate.md)
  The object that handles the double-tap or squeeze interactions a person makes on Apple Pencil.
- [protocol UIPencilInteractionDelegate](uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
### Enabling interactions
- [var isEnabled: Bool](uipencilinteraction/isenabled.md)
  A Boolean value that specifies whether the system reports double taps or squeezes on Apple Pencil to your app.
### Determining preferences for actions
- [class var preferredTapAction: UIPencilPreferredAction](uipencilinteraction/preferredtapaction.md)
  A person’s preferred double-tap action for Apple Pencil, as specified in the Settings app.
- [class var preferredSqueezeAction: UIPencilPreferredAction](uipencilinteraction/preferredsqueezeaction.md)
  A person’s preferred squeeze action for Apple Pencil, as specified in the Settings app.
- [enum UIPencilPreferredAction](uipencilpreferredaction.md)
  The actions Apple Pencil can perform after a person performs a double tap or squeeze.
### Determining input type
- [class var prefersPencilOnlyDrawing: Bool](uipencilinteraction/preferspencilonlydrawing.md)
  A person’s preference for drawing with Apple Pencil only, as specified in the Settings app or the system tool picker.
### Determining hover preview preferences
- [class var prefersHoverToolPreview: Bool](uipencilinteraction/prefershovertoolpreview.md)
  A person’s preference for whether holding a supported model of Apple Pencil close to the screen shows a preview of the current drawing tool, as specified in the Settings app.
### Supporting types
- [UIPencilInteraction.Tap](uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.

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
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UIPencilInteractionDelegate](uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [UIPencilInteraction.Tap](uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [UIPencilInteraction.Phase](uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction)*