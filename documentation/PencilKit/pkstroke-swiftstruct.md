# PKStroke

**Framework**: PencilKit  
**Kind**: struct

A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKStroke
```

## Mentions

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)

## Topics

### Creating a stroke object
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](pkstroke-swift.struct/init(ink:path:transform:mask:)-1imp6.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)](pkstroke-swift.struct/init(ink:path:transform:mask:)-w7ti.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-10m5j.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)](pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-epus.md)
  Creates a macOS stroke with the line properties, path, transform, mask, and random seed that you specify.
### Getting the stroke properties
- [var ink: PKInk](pkstroke-swift.struct/ink.md)
  The Ink, which is a combination of a tool used to render this stroke.
- [var mask: UIBezierPath?](pkstroke-swift.struct/mask-8g6sx.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var mask: NSBezierPath?](pkstroke-swift.struct/mask-16kkz.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var maskedPathRanges: [ClosedRange<CGFloat>]](pkstroke-swift.struct/maskedpathranges.md)
  The range of points in the stroke path reference that intersect the stroke’s mask.
- [var path: PKStrokePath](pkstroke-swift.struct/path.md)
  The B-spline path that describes this stroke.
- [var renderBounds: CGRect](pkstroke-swift.struct/renderbounds.md)
  The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.
- [var transform: CGAffineTransform](pkstroke-swift.struct/transform.md)
  The affine transform of the stroke after rendering.
- [var randomSeed: UInt32](pkstroke-swift.struct/randomseed.md)
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkstroke-swift.struct/requiredcontentversion.md)
  The version of PencilKit necessary to use the stroke.
### Using reference types
- [class PKStrokeReference](pkstrokereference.md)
  A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Drawing with PencilKit](drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [class PKCanvasView](pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [struct PKDrawing](pkdrawing-swift.struct.md)
  A structure representing the drawing information captured by a canvas view.
- [struct PKStrokePath](pkstrokepath-swift.struct.md)
  A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [struct PKStrokePoint](pkstrokepoint-swift.struct.md)
  A structure that represents the properties of a specific point along a stroke’s path.
- [struct PKInk](pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct)*