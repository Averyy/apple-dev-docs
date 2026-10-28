# indirectScribbleInteraction:requestElementsInRect:completion:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction requestElementsInRect:(CGRect) rect completion:(void (^)(NSArray<id<NSCopying,NSObject>> *elements)) completion;
```

## Discussion

Each rectangle returned by the completion handler represents an area where the user can start writing even if it’s not a text input field itself.

## Parameters

- `interaction`: The interaction requesting to focus an element.
- `rect`: The rect around the area where the user is trying to write, in the interaction’s view coordinate system. Return only the elements intersecting this rect.
- `completion`: A completion handler that you must call, either synchronously or asynchronously. Pass an array of identifiers of the available elements, or an empty array if there are no elements.

## See Also

### Finding elements and frames
- [- indirectScribbleInteraction:frameForElement:](./indirectscribbleinteraction_frameforelement_.md)
  Asks the delegate to provide the frame of an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:requestelementsinrect:completion:)*