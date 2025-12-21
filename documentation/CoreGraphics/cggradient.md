# CGGradient

**Framework**: Core Graphics  
**Kind**: class

A definition for a smooth transition between colors for drawing radial and axial gradient fills.

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
class CGGradient
```

#### Overview

A gradient defines a smooth transition between colors across an area. A `CGGradient` has a color space, two or more colors, and a location for each color. The color space cannot be a pattern or indexed color space, otherwise it can be any Core Graphics color space ([`CGColorSpace`](cgcolorspace.md)).

Colors can be provided as component values (such as red, green, blue) or as Core Graphics color objects ([`CGColor`](cgcolor.md)). Component values can vary from 0.0 to 1.0, designating the proportion of the component present in the color.

A location is a normalized value. When it comes time to paint the gradient, Core Graphics maps the normalized location values to the points in coordinate space that you provide.

For more precise control over gradients, see [`CGShading`](cgshading.md).

## Topics

### Creating Gradient Instances
- [init?(colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](cggradient/init(colorspace:colorcomponents:locations:count:).md)
  Creates a CGGradient object from a color space and the provided color components and locations.
- [init?(colorsSpace: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)](cggradient/init(colorsspace:colors:locations:).md)
  Creates a gradient object from a color space and the provided color objects and locations.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cggradient/typeid.md)
  Returns the Core Foundation type identifier for CGGradient objects.
### Initializers
- [init?(headroom: Float, colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](cggradient/init(headroom:colorspace:colorcomponents:locations:count:).md)
### Instance Properties
- [var contentHeadroom: Float](cggradient/contentheadroom.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CGDataConsumer](cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGDataProvider](cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGFunction](cgfunction.md)
  A general facility for defining and using callback functions.
- [class CGPattern](cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradient)*