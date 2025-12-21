# indirectScribbleInteraction(_:shouldDelayFocusForElement:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Allow the delegate to delay focusing an element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, shouldDelayFocusForElement elementIdentifier: Self.ElementIdentifier) -> Bool
```

#### Return Value

Return [`true`](https://developer.apple.com/documentation/Swift/true) to delay focusing the element; the default is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `interaction`: The interaction asking about delaying focus.
- `elementIdentifier`: The identifier of the element the interaction is asking about.

## See Also

- [func indirectScribbleInteraction(any UIInteraction, isElementFocused: Self.ElementIdentifier) -> Bool](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:iselementfocused:).md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint, completion: ((any UIResponder & UITextInput)?) -> Void)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:completion:).md)
  Asks the delegate to focus an element to handle text edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:))*