# hasActiveDrag

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether items were lifted from the collection view and have not yet been dropped.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasActiveDrag: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasActiveDrag;
```

## See Also

### Managing drag interactions
- [var dragDelegate: (any UICollectionViewDragDelegate)?](./dragdelegate.md)
  The delegate object that manages the dragging of items from the collection view.
- [protocol UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [var dragInteractionEnabled: Bool](./draginteractionenabled.md)
  A Boolean value that indicates whether the collection view supports dragging content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/hasactivedrag)*