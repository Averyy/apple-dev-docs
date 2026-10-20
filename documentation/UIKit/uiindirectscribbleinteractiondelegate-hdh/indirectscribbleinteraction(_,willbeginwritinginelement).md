# indirectScribbleInteraction(_:willBeginWritingInElement:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the delegate when the user begins writing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, willBeginWritingInElement elementIdentifier: Self.ElementIdentifier)
```

#### Discussion

Use this to hide custom placeholders or other UI elements that can interfere with writing.

## Parameters

- `interaction`: The interaction where the user started writing.
- `elementIdentifier`: The identifier of the element that should receive focus.

## Default Implementations

### UIIndirectScribbleInteractionDelegate Implementations
- [func indirectScribbleInteraction(any UIInteraction, willBeginWritingInElement: Self.ElementIdentifier)](./indirectscribbleinteraction%28_,willbeginwritinginelement%29-8qsa.md)

## See Also

### Tracking Scribble Input
- [func indirectScribbleInteraction(any UIInteraction, didFinishWritingInElement: Self.ElementIdentifier)](./indirectscribbleinteraction%28_,didfinishwritinginelement%29.md)
  Informs the delegate when the user finishes writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:willbeginwritinginelement:))*