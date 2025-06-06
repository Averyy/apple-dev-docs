# UIPencilInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol UIPencilInteractionDelegate : NSObjectProtocol
```

## Topics

### Handling double-tap interactions
- [func pencilInteraction(UIPencilInteraction, didReceiveTap: UIPencilInteraction.Tap)](uipencilinteractiondelegate/pencilinteraction(_:didreceivetap:).md)
  Tells the delegate when a person double-taps Apple Pencil.
### Handling squeeze interactions
- [func pencilInteraction(UIPencilInteraction, didReceiveSqueeze: UIPencilInteraction.Squeeze)](uipencilinteractiondelegate/pencilinteraction(_:didreceivesqueeze:).md)
  Tells the delegate when a person squeezes Apple Pencil.
### Deprecated
- [func pencilInteractionDidTap(UIPencilInteraction)](uipencilinteractiondelegate/pencilinteractiondidtap(_:).md)
  Tells the delegate that the user double-tapped Apple Pencil.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIPencilInteraction](uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteraction.Tap](uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [UIPencilInteraction.Phase](uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate)*