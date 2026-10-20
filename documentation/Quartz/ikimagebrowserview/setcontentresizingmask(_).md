# setContentResizingMask(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Determines how the receiver resizes its content when zooming.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setContentResizingMask(_ mask: Int)
```

```objc
- (void) setContentResizingMask:(NSUInteger) mask;
```

## Parameters

- `mask`: A resizing mask. You specify a mask by combining any of the following options using the C bitwise `OR` operator: [`width`](../../AppKit/nsview/autoresizingmask-swift.struct/width.md), [`height`](../../AppKit/nsview/autoresizingmask-swift.struct/height.md). Other values are ignored.

## See Also

### Zooming and Resizing
- [func setZoomValue(Float)](./setzoomvalue%28_%29.md)
  Sets the zoom value.
- [func zoomValue() -> Float](./zoomvalue%28%29.md)
  Returns the current zoom value.
- [func contentResizingMask() -> Int](./contentresizingmask%28%29.md)
  Returns the receiver’s content resizing mask, which determines how its content is resized while zooming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcontentresizingmask(_:))*