# UIIndirectScribbleInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

Methods that customize behavior on views that aren’t formally text input views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
protocol UIIndirectScribbleInteractionDelegate : NSObjectProtocol
```

## Topics

### Identifying Elements
- [associatedtype ElementIdentifier : Hashable = String](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md)
  A unique identifier for a control that isn’t a text field in a Scribble interaction.
### Managing Focus
- [func indirectScribbleInteraction(any UIInteraction, isElementFocused: Self.ElementIdentifier) -> Bool](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:iselementfocused:).md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint, completion: ((any UIResponder & UITextInput)?) -> Void)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:completion:).md)
  Asks the delegate to focus an element to handle text edits.
- [func indirectScribbleInteraction(any UIInteraction, shouldDelayFocusForElement: Self.ElementIdentifier) -> Bool](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:).md)
  Allow the delegate to delay focusing an element.
### Tracking Scribble Input
- [func indirectScribbleInteraction(any UIInteraction, willBeginWritingInElement: Self.ElementIdentifier)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:willbeginwritinginelement:).md)
  Informs the delegate when the user begins writing.
- [func indirectScribbleInteraction(any UIInteraction, didFinishWritingInElement: Self.ElementIdentifier)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:didfinishwritinginelement:).md)
  Informs the delegate when the user finishes writing.
### Finding Elements and Frames
- [func indirectScribbleInteraction(any UIInteraction, frameForElement: Self.ElementIdentifier) -> CGRect](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:frameforelement:).md)
  Asks the delegate to provide the frame of an element.
- [func indirectScribbleInteraction(any UIInteraction, requestElementsIn: CGRect, completion: ([Self.ElementIdentifier]) -> Void)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:requestelementsin:completion:).md)
  Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.
### Instance Methods
- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint) async -> (any UIResponder & UITextInput)?](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:).md)
- [func indirectScribbleInteraction(any UIInteraction, requestElementsIn: CGRect) async -> [Self.ElementIdentifier]](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:requestelementsin:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIIndirectScribbleInteraction](uiindirectscribbleinteraction-1nfjm.md)
  An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.
- [associatedtype ElementIdentifier : Hashable = String](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md)
  A unique identifier for a control that isn’t a text field in a Scribble interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh)*