# indirectScribbleInteraction:isElementFocused:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (BOOL) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction isElementFocused:(UIScribbleElementIdentifier) elementIdentifier;
```

## Return Value

Returns `true` if the element is the one currently focused.

## Parameters

- `interaction`: The interaction asking for the focused state.
- `elementIdentifier`: The identifier of the element the interaction is asking about.

## See Also

### Managing focus
- [- indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:](./indirectscribbleinteraction_focuselementifneeded_referencepoint_completion_.md)
  Asks the delegate to focus an element to handle text edits.
- [- indirectScribbleInteraction:shouldDelayFocusForElement:](./indirectscribbleinteraction_shoulddelayfocusforelement_.md)
  Allows the delegate to delay focusing an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:iselementfocused:)*