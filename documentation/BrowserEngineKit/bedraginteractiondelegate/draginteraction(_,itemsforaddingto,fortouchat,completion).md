# dragInteraction(_:itemsForAddingTo:forTouchAt:completion:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Requests items to add to a drag session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
optional func dragInteraction(_ dragInteraction: BEDragInteraction, itemsForAddingTo session: any UIDragSession, forTouchAt point: CGPoint, completion: @escaping ([UIDragItem]) -> Bool)
```

```objc
- (void) dragInteraction:(BEDragInteraction *) dragInteraction itemsForAddingToSession:(id<UIDragSession>) session forTouchAtPoint:(CGPoint) point completion:(BOOL (^)(NSArray<UIDragItem *> *)) completion;
```

#### Discussion

This method is the asynchronous variant of [`dragInteraction(_:itemsForAddingTo:withTouchAt:)`](../../UIKit/uidraginteractiondelegate/draginteraction%28_,itemsforaddingto,withtouchat%29.md). If your delegate implements this method, the system calls this method instead of the synchronous version.

Call the completion handler as soon you prepare its arguments. The system times out the completion handler if a long delay occurs before you call the handler.

The completion block returns `true` if the drag session added the items you supplied, and `false` otherwise.

## Parameters

- `dragInteraction`: The drag interaction that invokes this method.
- `session`: An in-progress drag session to which to add items.
- `point`: The touch location in the view’s coordinate system.
- `completion`: A completion handler that you call to add items to the drag session.

## See Also

### Participating in drag gestures
- [func dragInteraction(BEDragInteraction, prepare: any UIDragSession, completion: () -> Bool)](./draginteraction%28_,prepare,completion%29.md)
  Prepares the delegate for a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate/draginteraction(_:itemsforaddingto:fortouchat:completion:))*