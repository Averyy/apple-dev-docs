# isDraggable

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the annotation view is draggable.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isDraggable: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) makes an annotation draggable by the user. If [`true`](https://developer.apple.com/documentation/swift/true), the associated annotation object needs to also implement the [`setCoordinate:`](mkannotation/setcoordinate:.md) method. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) lets the map view know that the annotation is draggable. You can’t conditionalize drag operations by attempting to stop an operation the user initiates. Doing so can lead to undefined behavior. After it begins, the drag operation needs to continue to completion.

## See Also

- [func setDragState(MKAnnotationView.DragState, animated: Bool)](mkannotationview/setdragstate(_:animated:).md)
  Sets the drag state for the annotation view.
- [var dragState: MKAnnotationView.DragState](mkannotationview/dragstate-swift.property.md)
  The drag state of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/isdraggable)*