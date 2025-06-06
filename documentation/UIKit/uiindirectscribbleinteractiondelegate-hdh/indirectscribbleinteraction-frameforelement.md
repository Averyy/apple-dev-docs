# indirectScribbleInteraction(_:frameForElement:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to provide the frame of an element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

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

- [func indirectScribbleInteraction(any UIInteraction, requestElementsIn: CGRect, completion: ([Self.ElementIdentifier]) -> Void)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:requestelementsin:completion:).md)
  Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:frameforelement:))*