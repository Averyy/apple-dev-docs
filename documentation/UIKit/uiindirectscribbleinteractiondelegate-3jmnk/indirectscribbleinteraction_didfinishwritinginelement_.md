# indirectScribbleInteraction:didFinishWritingInElement:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the user finishes writing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction didFinishWritingInElement:(UIScribbleElementIdentifier) elementIdentifier;
```

## Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## Parameters

- `interaction`: The interaction where the user finished writing.
- `elementIdentifier`: The identifier of the element that should receive focus.

## See Also

### Tracking Scribble input
- [- indirectScribbleInteraction:willBeginWritingInElement:](./indirectscribbleinteraction_willbeginwritinginelement_.md)
  Informs the delegate when the user begins writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:didfinishwritinginelement:)*