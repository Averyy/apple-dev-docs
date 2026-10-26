# indirectScribbleInteraction:willBeginWritingInElement:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the user begins writing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction willBeginWritingInElement:(UIScribbleElementIdentifier) elementIdentifier;
```

#### Discussion

Use this to hide custom placeholders or other UI elements that can interfere with writing.

## Parameters

- `interaction`: The interaction where the user started writing.
- `elementIdentifier`: The identifier of the element that should receive focus.

## See Also

### Tracking Scribble input
- [- indirectScribbleInteraction:didFinishWritingInElement:](./indirectscribbleinteraction_didfinishwritinginelement_.md)
  Informs the delegate when the user finishes writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:willbeginwritinginelement:)*