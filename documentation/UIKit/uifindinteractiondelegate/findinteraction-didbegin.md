# findInteraction(_:didBegin:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when the interaction is about to present the find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func findInteraction(_ interaction: UIFindInteraction, didBegin session: UIFindSession)
```

#### Discussion

Use this method to decorate your view to indicate that a search operation is about to occur. For example, apply a dimming view around the unhighlighted search results.

## Parameters

- `interaction`: The interaction object triggering the find panel.
- `session`: The session object you provided for the interaction.

## See Also

- [func findInteraction(UIFindInteraction, didEnd: UIFindSession)](uifindinteractiondelegate/findinteraction(_:didend:).md)
  Informs the delegate when the interaction is about to dismiss the find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteractiondelegate/findinteraction(_:didbegin:))*