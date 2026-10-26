# UIIndirectScribbleInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

Methods that customize behavior on views that aren’t formally text input views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
@protocol UIIndirectScribbleInteractionDelegate <NSObject>
```

## Topics

### Managing focus
- [- indirectScribbleInteraction:isElementFocused:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_iselementfocused_.md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [- indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_focuselementifneeded_referencepoint_completion_.md)
  Asks the delegate to focus an element to handle text edits.
- [- indirectScribbleInteraction:shouldDelayFocusForElement:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_shoulddelayfocusforelement_.md)
  Allows the delegate to delay focusing an element.
### Tracking Scribble input
- [- indirectScribbleInteraction:willBeginWritingInElement:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_willbeginwritinginelement_.md)
  Informs the delegate when the user begins writing.
- [- indirectScribbleInteraction:didFinishWritingInElement:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_didfinishwritinginelement_.md)
  Informs the delegate when the user finishes writing.
### Finding elements and frames
- [- indirectScribbleInteraction:frameForElement:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_frameforelement_.md)
  Asks the delegate to provide the frame of an element.
- [- indirectScribbleInteraction:requestElementsInRect:completion:](./uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_requestelementsinrect_completion_.md)
  Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom views
- [UIIndirectScribbleInteraction](./uiindirectscribbleinteraction-2dap8.md)
  An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.
- [UIScribbleElementIdentifier](./uiscribbleelementidentifier.md)
  The element’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk)*