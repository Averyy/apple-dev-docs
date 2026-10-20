# drop(_:intoItemAt:rect:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Animates the item to the specified rectangle in the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drop(_ dragItem: UIDragItem, intoItemAt indexPath: IndexPath, rect: CGRect) -> any UIDragAnimating
```

```objc
- (id<UIDragAnimating>) dropItem:(UIDragItem *) dragItem intoItemAtIndexPath:(NSIndexPath *) indexPath rect:(CGRect) rect;
```

#### Discussion

Use this method to animate drops where you incorporate the dragged items into another item of your collection view. For example, when incorporating items into a folder, you’d use this method to animate the items in a way that makes it look like they were placed into the folder.

## Parameters

- `dragItem`: The dragged item that you want to animate into position.
- `indexPath`: The index path in the collection view at which to incorporate the item.
- `rect`: The destination rectangle to use for the animation. Specify the rectangle in the coordinate system of the cell at the specified `indexPath`. UIKit animates the drag item to the specified rectangle.

## See Also

### Animating Items to Their Destination
- [func drop(UIDragItem, toItemAt: IndexPath) -> any UIDragAnimating](./drop%28_,toitemat%29.md)
  Animates the item to the specified index path in the collection view.
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](./drop%28_,to%29-7w5rn.md)
  Animates the item to an arbitrary location in your view hierarchy.
- [func drop(UIDragItem, to: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext](./drop%28_,to%29-l5tg.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:intoitemat:rect:))*