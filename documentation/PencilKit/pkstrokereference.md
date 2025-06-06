# PKStrokeReference

**Framework**: PencilKit  
**Kind**: class

A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKStrokeReference
```

## Topics

### Creating a stroke object
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](pkstrokereference/init(ink:strokepath:transform:mask:).md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](pkstrokereference/init(ink:strokepath:transform:mask:randomseed:).md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.
### Getting the stroke properties
- [var ink: PKInk](pkstrokereference/ink.md)
  The line properties used to render this stroke.
- [var mask: UIBezierPath?](pkstrokereference/mask.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var maskedPathRanges: [__PKFloatRange]](pkstrokereference/maskedpathranges.md)
  The range of points in the stroke path reference that intersect the stroke’s mask.
- [var path: PKStrokePath](pkstrokereference/path.md)
  The B-spline path that describes this stroke.
- [var renderBounds: CGRect](pkstrokereference/renderbounds.md)
  The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.
- [var transform: CGAffineTransform](pkstrokereference/transform.md)
  The affine transform of the stroke after rendering.
- [var randomSeed: UInt32](pkstrokereference/randomseed.md)
  An unsigned 32-bit integer to use as a random seed for drawing strokes that use randomized effects.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkstrokereference/requiredcontentversion.md)
  The version of PencilKit necessary to use the stroke.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference)*