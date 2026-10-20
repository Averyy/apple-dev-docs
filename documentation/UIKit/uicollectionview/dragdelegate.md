# dragDelegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate object that manages the dragging of items from the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var dragDelegate: (any UICollectionViewDragDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UICollectionViewDragDelegate> dragDelegate;
```

## Mentions

- [Supporting Drag and Drop in Collection Views](../supporting-drag-and-drop-in-collection-views.md)

## See Also

### Managing drag interactions
- [protocol UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [var hasActiveDrag: Bool](./hasactivedrag.md)
  A Boolean value that indicates whether items were lifted from the collection view and have not yet been dropped.
- [var dragInteractionEnabled: Bool](./draginteractionenabled.md)
  A Boolean value that indicates whether the collection view supports dragging content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dragdelegate)*