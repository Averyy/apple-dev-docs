# dragInteractionEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the collection view supports dragging content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dragInteractionEnabled: Bool { get set }
```

#### Discussion

To support dragging content from the collection view to a view in your app or another app, set this property value to [`true`](https://developer.apple.com/documentation/Swift/true). To disable this behavior, set the value to [`false`](https://developer.apple.com/documentation/Swift/false). The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

In iOS 14 and earlier, the default value is [`true`](https://developer.apple.com/documentation/Swift/true) for iPad and [`false`](https://developer.apple.com/documentation/Swift/false) for iPhone. Setting the value to [`true`](https://developer.apple.com/documentation/Swift/true) on iPhone enables dragging within your app only. Dragging content to other apps isn’t possible on iPhone prior to iOS 15.

## See Also

- [var dragDelegate: (any UICollectionViewDragDelegate)?](uicollectionview/dragdelegate.md)
  The delegate object that manages the dragging of items from the collection view.
- [protocol UICollectionViewDragDelegate](uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [var hasActiveDrag: Bool](uicollectionview/hasactivedrag.md)
  A Boolean value that indicates whether items were lifted from the collection view and have not yet been dropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/draginteractionenabled)*