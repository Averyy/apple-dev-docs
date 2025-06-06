# indirectScribbleInteraction(_:didFinishWritingInElement:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the delegate when the user finishes writing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, didFinishWritingInElement elementIdentifier: Self.ElementIdentifier)
```

#### Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## Parameters

- `interaction`: The interaction where the user finished writing.
- `elementIdentifier`: The identifier of the element that should receive focus.

## See Also

- [func indirectScribbleInteraction(any UIInteraction, willBeginWritingInElement: Self.ElementIdentifier)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:willbeginwritinginelement:).md)
  Informs the delegate when the user begins writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:didfinishwritinginelement:))*