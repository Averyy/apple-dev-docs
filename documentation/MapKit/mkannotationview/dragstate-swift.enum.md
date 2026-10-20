# MKAnnotationView.DragState

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the drag state of an annotation view.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
enum DragState
```

```c
enum MKAnnotationViewDragState : NSUInteger;
```

## Topics

### Constants
- [MKAnnotationView.DragState.none](./dragstate-swift.enum/none.md)
  An annotation view that doesn’t have a drag operation.
- [MKAnnotationView.DragState.starting](./dragstate-swift.enum/starting.md)
  An annotation view begins dragging.
- [MKAnnotationView.DragState.dragging](./dragstate-swift.enum/dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.canceling](./dragstate-swift.enum/canceling.md)
  An annotation view cancels drag operation.
- [MKAnnotationView.DragState.ending](./dragstate-swift.enum/ending.md)
  An annotation view ends dragging.
### Initializers
- [init?(rawValue: UInt)](./dragstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum)*