# drop(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Animates the item to an arbitrary location in your view hierarchy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drop(_ dragItem: UIDragItem, to target: UIDragPreviewTarget) -> any UIDragAnimating
```

#### Discussion

Use this method to animate drops to any view in your app. For example, you might use this method to drop items onto a tab bar or toolbar that’s part of your interface.

## Parameters

- `dragItem`: The item that you want to drop.
- `target`: The location at which to drop the item, specified as a point in a view. You can also use the   object to specify a final transform to apply to the content.

## See Also

- [func drop(UIDragItem, toItemAt: IndexPath) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:toitemat:).md)
  Animates the item to the specified index path in the collection view.
- [func drop(UIDragItem, intoItemAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:intoitemat:rect:).md)
  Animates the item to the specified rectangle in the collection view.
- [func drop(UIDragItem, to: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext](uicollectionviewdropcoordinator/drop(_:to:)-l5tg.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-7w5rn)*