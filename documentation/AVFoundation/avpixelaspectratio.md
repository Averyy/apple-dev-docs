# AVPixelAspectRatio

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines a pixel aspect ratio for a rendering context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVPixelAspectRatio
```

```c
typedef struct { ... } AVPixelAspectRatio;
```

## Topics

### Spacing
- [var horizontalSpacing: Int](./avpixelaspectratio/horizontalspacing.md)
  The pixel aspect ratio’s horizontal spacing value.
- [var verticalSpacing: Int](./avpixelaspectratio/verticalspacing.md)
  The pixel aspect ratio’s vertical spacing value.
### Initializers
- [init()](./avpixelaspectratio/init%28%29.md)
  Creates an empty pixel aspect ratio.
- [init(horizontalSpacing: Int, verticalSpacing: Int)](./avpixelaspectratio/init%28horizontalspacing,verticalspacing%29.md)
  Creates a pixel aspect ratio with horizontal and vertical spacing values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Getting pixel and edge width information
- [var edgeWidths: AVEdgeWidths](./avvideocompositionrendercontext/edgewidths.md)
  The width of the edge processing region on the left, top, right, and bottom edges, in pixels.
- [struct AVEdgeWidths](./avedgewidths.md)
  A structure that defines edge processing region widths.
- [var pixelAspectRatio: AVPixelAspectRatio](./avvideocompositionrendercontext/pixelaspectratio.md)
  The pixel aspect ratio for rendered frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpixelaspectratio)*