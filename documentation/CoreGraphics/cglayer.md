# CGLayer

**Framework**: Core Graphics  
**Kind**: class

An offscreen context for reusing content drawn with Core Graphics.

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
class CGLayer
```

## Topics

### Creating Layer Objects
- [init?(CGContext, size: CGSize, auxiliaryInfo: CFDictionary?)](cglayer/init(_:size:auxiliaryinfo:).md)
  Creates a layer object that is associated with a graphics context.
### Examining a Layer
- [var context: CGContext?](cglayer/context.md)
  Returns the graphics context associated with a layer object.
- [var size: CGSize](cglayer/size.md)
  Returns the width and height of a layer object.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cglayer/typeid.md)
  Returns the unique type identifier used for [`CGLayer`](cglayer.md) objects.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CGContext](cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](cgimage.md)
  A bitmap image or image mask.
- [class CGPath](cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGMutablePath](cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayer)*