# indirectScribbleInteraction(_:isElementFocused:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, isElementFocused elementIdentifier: Self.ElementIdentifier) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the element is the one currently focused.

## Parameters

- `interaction`: The interaction asking for the focused state.
- `elementIdentifier`: The identifier of the element the interaction is asking about.

## See Also

- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint, completion: ((any UIResponder & UITextInput)?) -> Void)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:completion:).md)
  Asks the delegate to focus an element to handle text edits.
- [func indirectScribbleInteraction(any UIInteraction, shouldDelayFocusForElement: Self.ElementIdentifier) -> Bool](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:).md)
  Allow the delegate to delay focusing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:iselementfocused:))*