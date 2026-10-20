# UIPencilInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- visionOS 26.2+

## Declaration

```swift
@MainActor
protocol UIPencilInteractionDelegate : NSObjectProtocol
```

```objc
@protocol UIPencilInteractionDelegate <NSObject>
```

## Topics

### Handling double-tap interactions
- [func pencilInteraction(UIPencilInteraction, didReceiveTap: UIPencilInteraction.Tap)](./uipencilinteractiondelegate/pencilinteraction%28_,didreceivetap%29.md)
  Tells the delegate when a person double-taps Apple Pencil.
- [func pencilInteractionDidTap(UIPencilInteraction)](./uipencilinteractiondelegate/pencilinteractiondidtap%28_%29.md)
  Tells the delegate that the user double-tapped Apple Pencil.
### Handling squeeze interactions
- [func pencilInteraction(UIPencilInteraction, didReceiveSqueeze: UIPencilInteraction.Squeeze)](./uipencilinteractiondelegate/pencilinteraction%28_,didreceivesqueeze%29.md)
  Tells the delegate when a person squeezes Apple Pencil.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Apple Pencil interactions in UIKit
- [class UIPencilInteraction](./uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteraction.Tap](./uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](./uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [UIPencilInteraction.Phase](./uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](./uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate)*