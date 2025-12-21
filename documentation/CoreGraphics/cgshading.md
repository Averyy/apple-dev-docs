# CGShading

**Framework**: Core Graphics  
**Kind**: class

A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.

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
class CGShading
```

#### Overview

Shading means to fill using a smooth transition between colors across an area. You create a shading using a custom function with a [`CGFunction`](cgfunction.md) instance. To paint with a Core Graphics shading, you call [`drawShading(_:)`](cgcontext/drawshading(_:).md). This function fills the current clipping path using the specified color gradient, calling your parametric function repeatedly as it draws.

An alternative to using a `CGShading` instance is to use the [`CGGradient`](cggradient.md) type. For applications that run in macOS 10.5 and later, `CGGradient` objects are much simpler to use.

## Topics

### Creating Shading Objects
- [init?(axialSpace: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)](cgshading/init(axialspace:start:end:function:extendstart:extendend:).md)
  Creates a shading object to use for axial shading.
- [init?(radialSpace: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)](cgshading/init(radialspace:start:startradius:end:endradius:function:extendstart:extendend:).md)
  Creates a shading object to use for radial shading.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgshading/typeid.md)
  Returns the Core Foundation type identifier for Core Graphics shading objects.
### Initializers
- [init?(axialHeadroom: Float, space: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)](cgshading/init(axialheadroom:space:start:end:function:extendstart:extendend:).md)
- [init?(radialHeadroom: Float, space: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)](cgshading/init(radialheadroom:space:start:startradius:end:endradius:function:extendstart:extendend:).md)
### Instance Properties
- [var contentHeadroom: Float](cgshading/contentheadroom.md)

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
- [class CGGradient](cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGFunction](cgfunction.md)
  A general facility for defining and using callback functions.
- [class CGPattern](cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgshading)*