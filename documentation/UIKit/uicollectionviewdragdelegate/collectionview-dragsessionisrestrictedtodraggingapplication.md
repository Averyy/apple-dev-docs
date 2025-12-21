# collectionView(_:dragSessionIsRestrictedToDraggingApplication:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that determines whether the source app and destination app must be the same for a drag session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, dragSessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when the source app and destination app should be the same — that is, the user is not allowed to drop the item on another app.

#### Discussion

If you don’t implement this method, the default return value is [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `collectionView`: The collection view from which the drag operation originated.
- `session`: The drag session that’s active.

## See Also

- [func collectionView(UICollectionView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](uicollectionviewdragdelegate/collectionview(_:dragsessionallowsmoveoperation:).md)
  Returns a Boolean value that determines whether a move operation is allowed for a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionisrestrictedtodraggingapplication:))*