# AVCaptionPoint

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines the origin point for a caption.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```swift
struct AVCaptionPoint
```

```c
typedef struct AVCaptionPoint { ... } AVCaptionPoint;
```

## Topics

### Inspecting the point
- [var x: AVCaptionDimension](./avcaptionpoint/x.md)
  The point’s x coordinate.
- [var y: AVCaptionDimension](./avcaptionpoint/y.md)
  The point’s y coordinate.
### Initializers
- [init()](./avcaptionpoint/init%28%29.md)
  Creates a caption dimension.
- [init(x: AVCaptionDimension, y: AVCaptionDimension)](./avcaptionpoint/init%28x,y%29.md)
  Creates a caption point with x and y coordinates.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Accessing the location
- [var origin: AVCaptionPoint](./avcaptionregion/origin.md)
  The region’s top-left position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionpoint)*