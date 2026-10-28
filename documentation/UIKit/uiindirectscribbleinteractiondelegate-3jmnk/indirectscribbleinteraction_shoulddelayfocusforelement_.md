# indirectScribbleInteraction:shouldDelayFocusForElement:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to delay focusing an element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (BOOL) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction shouldDelayFocusForElement:(UIScribbleElementIdentifier) elementIdentifier;
```

## Return Value

Return [`true`](../../Swift/true.md) to delay focusing the element; the default is [`false`](../../Swift/false.md).

## Discussion

Normally, Scribble focuses the target input as soon as the user begins writing. If you return `true` from this callback, it waits until the user pauses briefly. This is useful in cases where the view shifts or transforms when becoming first responder, which can be disruptive to a user trying to write into the field.

It’s preferable to adjust the UI behavior to avoid the layout changes. Only use delayed focus as a last resort, since transcription happens all at once instead of incrementally.

## Parameters

- `interaction`: The interaction asking about delaying focus.
- `elementIdentifier`: The identifier of the element the interaction is asking about.

## See Also

### Managing focus
- [- indirectScribbleInteraction:isElementFocused:](./indirectscribbleinteraction_iselementfocused_.md)
  Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [- indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:](./indirectscribbleinteraction_focuselementifneeded_referencepoint_completion_.md)
  Asks the delegate to focus an element to handle text edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:shoulddelayfocusforelement:)*