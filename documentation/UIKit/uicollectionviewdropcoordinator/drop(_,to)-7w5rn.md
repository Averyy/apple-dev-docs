# drop(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Animates the item to an arbitrary location in your view hierarchy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func drop(_ dragItem: UIDragItem, to target: UIDragPreviewTarget) -> any UIDragAnimating
```

```objc
- (id<UIDragAnimating>) dropItem:(UIDragItem *) dragItem toTarget:(UIDragPreviewTarget *) target;
```

#### Discussion

Use this method to animate drops to any view in your app. For example, you might use this method to drop items onto a tab bar or toolbar that’s part of your interface.

## Parameters

- `dragItem`: The item that you want to drop.
- `target`: The location at which to drop the item, specified as a point in a view. You can also use the [`UIDragPreviewTarget`](../uidragpreviewtarget.md) object to specify a final transform to apply to the content.

## See Also

### Animating Items to Their Destination
- [func drop(UIDragItem, toItemAt: IndexPath) -> any UIDragAnimating](./drop%28_,toitemat%29.md)
  Animates the item to the specified index path in the collection view.
- [func drop(UIDragItem, intoItemAt: IndexPath, rect: CGRect) -> any UIDragAnimating](./drop%28_,intoitemat,rect%29.md)
  Animates the item to the specified rectangle in the collection view.
- [func drop(UIDragItem, to: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext](./drop%28_,to%29-l5tg.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-7w5rn)*