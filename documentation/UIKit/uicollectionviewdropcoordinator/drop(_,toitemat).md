# drop(_:toItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Animates the item to the specified index path in the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drop(_ dragItem: UIDragItem, toItemAt indexPath: IndexPath) -> any UIDragAnimating
```

```objc
- (id<UIDragAnimating>) dropItem:(UIDragItem *) dragItem toItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Mentions

- [Supporting Drag and Drop in Collection Views](../supporting-drag-and-drop-in-collection-views.md)

#### Discussion

Use this method to animate the dragged item to the specific location in the collection view. Typically, you use this method for content that originated in the collection view and is moving to a new location.

## Parameters

- `dragItem`: The dragged item that you want to animate into position.
- `indexPath`: The index path to use as the destination for the animation.

## See Also

### Animating Items to Their Destination
- [func drop(UIDragItem, intoItemAt: IndexPath, rect: CGRect) -> any UIDragAnimating](./drop%28_,intoitemat,rect%29.md)
  Animates the item to the specified rectangle in the collection view.
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](./drop%28_,to%29-7w5rn.md)
  Animates the item to an arbitrary location in your view hierarchy.
- [func drop(UIDragItem, to: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext](./drop%28_,to%29-l5tg.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:toitemat:))*