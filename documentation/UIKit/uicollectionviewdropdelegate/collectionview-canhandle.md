# collectionView(_:canHandle:)

**Framework**: UIKit  
**Kind**: method

Asks your delegate whether the collection view can accept a drop with the specified type of data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, canHandle session: any UIDropSession) -> Bool
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the collection view can accept the dragged data or [`false`](https://developer.apple.com/documentation/swift/false) if it cannot.

#### Discussion

Implement this method when you want to dynamically determine whether to accept dropped data in your collection view. In your implementation, check the type of the dragged data and return a Boolean value indicating whether you can accept the drop. For example, you might call the [`hasItemsConforming(toTypeIdentifiers:)`](uidragdropsession/hasitemsconforming(totypeidentifiers:).md) method of the session object to determine whether it contains data that your app can accept.

If you don’t implement this method, the collection view assumes a return value of [`true`](https://developer.apple.com/documentation/swift/true). If you return [`false`](https://developer.apple.com/documentation/swift/false) from this method, the collection view doesn’t call any more methods of your drop delegate for the given session.

## Parameters

- `collectionView`: The collection view that’s attempting to handle the drop.
- `session`: The drop session object containing information about the type of data being dragged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:canhandle:))*