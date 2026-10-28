# isDraggable

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the annotation view is draggable.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
var isDraggable: Bool { get set }
```

```objc
@property (nonatomic, getter=isDraggable) BOOL draggable;
```

## Discussion

Setting this property to [`true`](../../Swift/true.md) makes an annotation draggable by the user. If [`true`](../../Swift/true.md), the associated annotation object needs to also implement the [`setCoordinate:`](../mkannotation/setcoordinate_.md) method. The default value of this property is [`false`](../../Swift/false.md).

Setting this property to [`true`](../../Swift/true.md) lets the map view know that the annotation is draggable. You can’t conditionalize drag operations by attempting to stop an operation the user initiates. Doing so can lead to undefined behavior. After it begins, the drag operation needs to continue to completion.

## See Also

### Supporting drag operations
- [func setDragState(MKAnnotationView.DragState, animated: Bool)](./setdragstate%28_,animated%29.md)
  Sets the drag state for the annotation view.
- [var dragState: MKAnnotationView.DragState](./dragstate-swift.property.md)
  The drag state of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/isdraggable)*