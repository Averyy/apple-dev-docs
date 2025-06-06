# indirectScribbleInteraction(_:willBeginWritingInElement:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the delegate when the user begins writing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, willBeginWritingInElement elementIdentifier: Self.ElementIdentifier)
```

#### Discussion

Use this to hide custom placeholders or other UI elements that can interfere with writing.

## Parameters

- `interaction`: The interaction where the user started writing.
- `elementIdentifier`: The identifier of the element that should receive focus.

## See Also

- [func indirectScribbleInteraction(any UIInteraction, didFinishWritingInElement: Self.ElementIdentifier)](uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:didfinishwritinginelement:).md)
  Informs the delegate when the user finishes writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:willbeginwritinginelement:))*