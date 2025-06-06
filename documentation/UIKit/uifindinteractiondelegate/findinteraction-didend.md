# findInteraction(_:didEnd:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when the interaction is about to dismiss the find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func findInteraction(_ interaction: UIFindInteraction, didEnd session: UIFindSession)
```

#### Discussion

Use this method to undo decoration on your view to indicate that a search operation is complete. For example, remove a dimming view from around the unhighlighted search results.

## Parameters

- `interaction`: The interaction object triggering the find panel.
- `session`: The session object you provided for the interaction.

## See Also

- [func findInteraction(UIFindInteraction, didBegin: UIFindSession)](uifindinteractiondelegate/findinteraction(_:didbegin:).md)
  Informs the delegate when the interaction is about to present the find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteractiondelegate/findinteraction(_:didend:))*