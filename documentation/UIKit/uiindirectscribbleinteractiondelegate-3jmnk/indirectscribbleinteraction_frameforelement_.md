# indirectScribbleInteraction:frameForElement:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide the frame of an element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (CGRect) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction frameForElement:(UIScribbleElementIdentifier) elementIdentifier;
```

#### Return Value

Returns the frame for the element, in the view coordinate system of the interaction.

## Parameters

- `interaction`: The interaction requesting to focus an element.
- `elementIdentifier`: The identifier of the element that should receive focus.

## See Also

### Finding elements and frames
- [- indirectScribbleInteraction:requestElementsInRect:completion:](./indirectscribbleinteraction_requestelementsinrect_completion_.md)
  Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:frameforelement:)*