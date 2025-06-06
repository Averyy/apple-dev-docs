# indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to focus an element to handle text edits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, focusElementIfNeeded elementIdentifier: Self.ElementIdentifier, referencePoint focusReferencePoint: CGPoint, completion: @escaping ((any UIResponder & UITextInput)?) -> Void)
```

#### Return Value

In response to this callback, the implementation should make this element the currently focused one, and make the corresponding [`UITextInput`](uitextinput.md) become first responder.

If the element isn’t focused already, set the text selection to the character location closest to `focusReferencePoint` to avoid any scrolling or shifting of content.

If the element is already focused, make no changes to the selection. Before returning you must still call the completion handler with a reference to [`UITextInput`](uitextinput.md).

## Parameters

- `interaction`: The interaction requesting to focus an element.
- `elementIdentifier`: The identifier of the element that should receive focus.
- `focusReferencePoint`: A   inside the element’s view.
- `completion`: A completion handler that you must call, either synchronously or asynchronously. On success, the first parameter should be the text input that became first responder and that handles text operations for this element. On failure, call the completion with a   parameter.

## See Also

- [func indirectScribbleInteraction(any UIInteraction, isElementFocused: Self.ElementIdentifier) -> Bool](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:iselementfocused:).md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [func indirectScribbleInteraction(any UIInteraction, shouldDelayFocusForElement: Self.ElementIdentifier) -> Bool](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:).md)
  Allow the delegate to delay focusing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:completion:))*