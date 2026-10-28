# dragInteraction(_:prepare:completion:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Prepares the delegate for a drag session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
optional func dragInteraction(_ dragInteraction: BEDragInteraction, prepare session: any UIDragSession, completion: @escaping () -> Bool)
```

```objc
- (void) dragInteraction:(BEDragInteraction *) dragInteraction prepareDragSession:(id<UIDragSession>) session completion:(BOOL (^)()) completion;
```

## Discussion

Call the completion handler when your app finishes preparing for the drag session. Call the handler as soon as possible to maintain a responsive interaction experience.

> ❗ **Important**:  The system expects your app to call the completion handler right away after drag session preparation, otherwise the system cancels the drag interaction.

Pass `true` in the completion handler to indicate successful preparations; otherwise, pass `false`.

## Parameters

- `dragInteraction`: The drag interaction that invokes this method.
- `session`: The drag session for which to prepare.
- `completion`: A completion handler you call after finishing drag session preparations.

## See Also

### Participating in drag gestures
- [func dragInteraction(BEDragInteraction, itemsForAddingTo: any UIDragSession, forTouchAt: CGPoint, completion: ([UIDragItem]) -> Bool)](./draginteraction%28_,itemsforaddingto,fortouchat,completion%29.md)
  Requests items to add to a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate/draginteraction(_:prepare:completion:))*