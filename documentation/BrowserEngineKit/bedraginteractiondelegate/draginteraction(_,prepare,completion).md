# dragInteraction(_:prepare:completion:)

**Framework**: BrowserEngineKit  
**Kind**: method

Prepares the delegate for a drag session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
optional func dragInteraction(_ dragInteraction: BEDragInteraction, prepare session: any UIDragSession, completion: @escaping () -> Bool)
```

#### Discussion

Call the completion handler when your app finishes preparing for the drag session. Call the handler as soon as possible to maintain a responsive interaction experience.

> ❗ **Important**:  The system expects your app to call the completion handler right away after drag session preparation, otherwise the system cancels the drag interaction.

Pass `true` in the completion handler to indicate successful preparations; otherwise, pass `false`.

## Parameters

- `dragInteraction`: The drag interaction that invokes this method.
- `session`: The drag session for which to prepare.
- `completion`: A completion handler you call after finishing drag session preparations.

## See Also

- [func dragInteraction(BEDragInteraction, itemsForAddingTo: any UIDragSession, forTouchAt: CGPoint, completion: ([UIDragItem]) -> Bool)](bedraginteractiondelegate/draginteraction(_:itemsforaddingto:fortouchat:completion:).md)
  Requests items to add to a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate/draginteraction(_:prepare:completion:))*