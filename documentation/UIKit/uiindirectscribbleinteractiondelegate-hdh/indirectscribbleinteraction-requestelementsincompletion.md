# indirectScribbleInteraction(_:requestElementsIn:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, requestElementsIn rect: CGRect, completion: @escaping ([Self.ElementIdentifier]) -> Void)
```

#### Discussion

Each rectangle returned by the completion handler represents an area where the user can start writing even if it’s not a text input field itself.

## Parameters

- `interaction`: The interaction where the user finished writing.
- `rect`: The rect around the area where the user is trying to write, in the interaction’s view coordinate system. Return only the elements intersecting this rect.
- `completion`: A completion handler that you must call, either synchronously or asynchronously. Pass an array of identifiers of the available elements, or an empty array if there are no elements.

## See Also

- [func indirectScribbleInteraction(any UIInteraction, frameForElement: Self.ElementIdentifier) -> CGRect](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:frameforelement:).md)
  Asks the delegate to provide the frame of an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:requestelementsin:completion:))*