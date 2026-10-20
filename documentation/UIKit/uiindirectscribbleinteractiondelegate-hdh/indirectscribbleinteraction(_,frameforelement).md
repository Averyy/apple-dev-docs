# indirectScribbleInteraction(_:frameForElement:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate to provide the frame of an element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, frameForElement elementIdentifier: Self.ElementIdentifier) -> CGRect
```

#### Return Value

Returns the frame for the element, in the view coordinate system of the interaction.

## Parameters

- `interaction`: The interaction requesting to focus an element.
- `elementIdentifier`: The identifier of the element that should receive focus.

## See Also

### Finding Elements and Frames
- [func indirectScribbleInteraction(any UIInteraction, requestElementsIn: CGRect, completion: ([Self.ElementIdentifier]) -> Void)](./indirectscribbleinteraction%28_,requestelementsin,completion%29.md)
  Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:frameforelement:))*