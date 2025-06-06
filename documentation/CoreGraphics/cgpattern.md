# CGPattern

**Framework**: Core Graphics  
**Kind**: class

A 2D pattern to be used for drawing graphics paths.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGPattern
```

#### Overview

Core Graphics tiles the pattern cell for you, based on parameters you specify when you call [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md).

To create a dashed line, see [`CGContextSetLineDash`](cgcontextsetlinedash.md).

## Topics

### Creating a Pattern
- [init?(info: UnsafeMutableRawPointer?, bounds: CGRect, matrix: CGAffineTransform, xStep: CGFloat, yStep: CGFloat, tiling: CGPatternTiling, isColored: Bool, callbacks: UnsafePointer<CGPatternCallbacks>)](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md)
  Creates a pattern object.
### Callbacks
- [struct CGPatternCallbacks](cgpatterncallbacks.md)
  A structure that holds a version and two callback functions for drawing a custom pattern.
- [typealias CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md)
  Draws a pattern cell.
- [typealias CGPatternReleaseInfoCallback](cgpatternreleaseinfocallback.md)
  Release private data or resources associated with the pattern.
### Constants
- [enum CGPatternTiling](cgpatterntiling.md)
  Different methods for rendering a tiled pattern.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgpattern/typeid.md)
  Returns the type identifier for Core Graphics patterns.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGDataConsumer](cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGDataProvider](cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGGradient](cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGFunction](cgfunction.md)
  A general facility for defining and using callback functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpattern)*