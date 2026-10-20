# collectionView(_:dragSessionAllowsMoveOperation:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that determines whether a move operation is allowed for a drag session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, dragSessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

```objc
- (BOOL) collectionView:(UICollectionView *) collectionView dragSessionAllowsMoveOperation:(id<UIDragSession>) session;
```

#### Return Value

[`false`](../../Swift/false.md) to cancel the drag session if move is not allowed; otherwise, [`true`](../../Swift/true.md).

#### Discussion

If you don’t implement this method, the default return value is [`true`](../../Swift/true.md).

## Parameters

- `collectionView`: The collection view from which the drag operation originated.
- `session`: The drag session that’s active.

## See Also

### Controlling the drag session
- [func collectionView(UICollectionView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](./collectionview%28_,dragsessionisrestrictedtodraggingapplication%29.md)
  Returns a Boolean value that determines whether the source app and destination app must be the same for a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionallowsmoveoperation:))*