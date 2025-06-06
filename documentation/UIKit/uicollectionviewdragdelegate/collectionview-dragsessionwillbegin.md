# collectionView(_:dragSessionWillBegin:)

**Framework**: UIKit  
**Kind**: method

Notifies you that a drag session is about to begin for the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, dragSessionWillBegin session: any UIDragSession)
```

#### Discussion

This method is called after it has been determined that a drag will begin and after any lift animations have occurred, but before the position of the drag changes. Use this method to perform any tasks related to the management of the drag session in your app.

Each call to this method is always balanced by a call to the [`collectionView(_:dragSessionDidEnd:)`](uicollectionviewdragdelegate/collectionview(_:dragsessiondidend:).md) method.

## Parameters

- `collectionView`: The collection view from which the drag operation originated.
- `session`: The drag session that’s beginning.

## See Also

- [func collectionView(UICollectionView, dragSessionDidEnd: any UIDragSession)](uicollectionviewdragdelegate/collectionview(_:dragsessiondidend:).md)
  Notifies you that a drag session ended for the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionwillbegin:))*