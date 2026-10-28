# indirectScribbleInteraction(_:shouldDelayFocusForElement:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Allow the delegate to delay focusing an element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, shouldDelayFocusForElement elementIdentifier: Self.ElementIdentifier) -> Bool
```

## Return Value

Return [`true`](../../Swift/true.md) to delay focusing the element; the default is [`false`](../../Swift/false.md).

## Parameters

- `interaction`: The interaction asking about delaying focus.
- `elementIdentifier`: The identifier of the element the interaction is asking about.

## Default Implementations

### UIIndirectScribbleInteractionDelegate Implementations
- [func indirectScribbleInteraction(any UIInteraction, shouldDelayFocusForElement: Self.ElementIdentifier) -> Bool](./indirectscribbleinteraction%28_,shoulddelayfocusforelement%29-9dmtl.md)

## See Also

### Managing Focus
- [func indirectScribbleInteraction(any UIInteraction, isElementFocused: Self.ElementIdentifier) -> Bool](./indirectscribbleinteraction%28_,iselementfocused%29.md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [func indirectScribbleInteraction(any UIInteraction, focusElementIfNeeded: Self.ElementIdentifier, referencePoint: CGPoint, completion: ((any UIResponder & UITextInput)?) -> Void)](./indirectscribbleinteraction%28_,focuselementifneeded,referencepoint,completion%29.md)
  Asks the delegate to focus an element to handle text edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:))*