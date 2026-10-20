# UIIndirectScribbleInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

Methods that customize behavior on views that aren’t formally text input views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
protocol UIIndirectScribbleInteractionDelegate : NSObjectProtocol
```

## Topics

### Identifying Elements
- [associatedtype ElementIdentifier : Hashable = String](./uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md)
  A unique identifier for a control that isn’t a text field in a Scribble interaction.
### Managing Focus
- [func indirectScribbleInteraction(any UIInteraction, isElementFocused: Self.ElementIdentifier) -> Bool](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,iselementfocused%29.md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint, completion: ((any UIResponder & UITextInput)?) -> Void)](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,focuselementifneeded,referencepoint,completion%29.md)
  Asks the delegate to focus an element to handle text edits.
- [func indirectScribbleInteraction(any UIInteraction, shouldDelayFocusForElement: Self.ElementIdentifier) -> Bool](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,shoulddelayfocusforelement%29.md)
  Allow the delegate to delay focusing an element.
### Tracking Scribble Input
- [func indirectScribbleInteraction(any UIInteraction, willBeginWritingInElement: Self.ElementIdentifier)](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,willbeginwritinginelement%29.md)
  Informs the delegate when the user begins writing.
- [func indirectScribbleInteraction(any UIInteraction, didFinishWritingInElement: Self.ElementIdentifier)](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,didfinishwritinginelement%29.md)
  Informs the delegate when the user finishes writing.
### Finding Elements and Frames
- [func indirectScribbleInteraction(any UIInteraction, frameForElement: Self.ElementIdentifier) -> CGRect](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,frameforelement%29.md)
  Asks the delegate to provide the frame of an element.
- [func indirectScribbleInteraction(any UIInteraction, requestElementsIn: CGRect, completion: ([Self.ElementIdentifier]) -> Void)](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,requestelementsin,completion%29.md)
  Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.
### Instance Methods
- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint) async -> (any UIResponder & UITextInput)?](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,focuselementifneeded,referencepoint%29.md)
- [func indirectScribbleInteraction(any UIInteraction, requestElementsIn: CGRect) async -> [Self.ElementIdentifier]](./uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_,requestelementsin%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom views
- [class UIIndirectScribbleInteraction](./uiindirectscribbleinteraction-1nfjm.md)
  An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.
- [associatedtype ElementIdentifier : Hashable = String](./uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md)
  A unique identifier for a control that isn’t a text field in a Scribble interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh)*