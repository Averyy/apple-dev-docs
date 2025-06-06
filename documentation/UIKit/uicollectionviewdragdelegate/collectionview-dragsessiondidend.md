# collectionView(_:dragSessionDidEnd:)

**Framework**: UIKit  
**Kind**: method

Notifies you that a drag session ended for the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, dragSessionDidEnd session: any UIDragSession)
```

#### Discussion

This method is called after the drag session ended, usually because the content was dropped but possibly because the drag was terminated. Use this method to close out any tasks related to the management of the drag session in your app.

Each call to this method is always balanced by a call to the [`collectionView(_:dragSessionWillBegin:)`](uicollectionviewdragdelegate/collectionview(_:dragsessionwillbegin:).md) method.

## Parameters

- `collectionView`: The collection view from which the drag operation originated.
- `session`: The drag session that ended.

## See Also

- [func collectionView(UICollectionView, dragSessionWillBegin: any UIDragSession)](uicollectionviewdragdelegate/collectionview(_:dragsessionwillbegin:).md)
  Notifies you that a drag session is about to begin for the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessiondidend:))*