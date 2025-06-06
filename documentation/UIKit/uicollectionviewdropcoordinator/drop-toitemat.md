# drop(_:toItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Animates the item to the specified index path in the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drop(_ dragItem: UIDragItem, toItemAt indexPath: IndexPath) -> any UIDragAnimating
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Discussion

Use this method to animate the dragged item to the specific location in the collection view. Typically, you use this method for content that originated in the collection view and is moving to a new location.

## Parameters

- `dragItem`: The dragged item that you want to animate into position.
- `indexPath`: The index path to use as the destination for the animation.

## See Also

- [func drop(UIDragItem, intoItemAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:intoitemat:rect:).md)
  Animates the item to the specified rectangle in the collection view.
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:to:)-7w5rn.md)
  Animates the item to an arbitrary location in your view hierarchy.
- [func drop(UIDragItem, to: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext](uicollectionviewdropcoordinator/drop(_:to:)-l5tg.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:toitemat:))*