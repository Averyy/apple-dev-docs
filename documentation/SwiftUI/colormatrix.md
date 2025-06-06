# ColorMatrix

**Framework**: SwiftUI  
**Kind**: struct

A matrix to use in an RGBA color transformation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
struct ColorMatrix
```

#### Overview

The matrix has five columns, each with a red, green, blue, and alpha component. You can use the matrix for tasks like creating a color transformation [`GraphicsContext.Filter`](graphicscontext/filter.md) for a [`GraphicsContext`](graphicscontext.md) using the [`colorMatrix(_:)`](graphicscontext/filter/colormatrix(_:).md) method.

## Topics

### Creating an identity matrix
- [init()](colormatrix/init.md)
  Creates the identity matrix.
### First column
- [var r1: Float](colormatrix/r1.md)
- [var g1: Float](colormatrix/g1.md)
- [var b1: Float](colormatrix/b1.md)
- [var a1: Float](colormatrix/a1.md)
### Second column
- [var r2: Float](colormatrix/r2.md)
- [var g2: Float](colormatrix/g2.md)
- [var b2: Float](colormatrix/b2.md)
- [var a2: Float](colormatrix/a2.md)
### Third column
- [var r3: Float](colormatrix/r3.md)
- [var g3: Float](colormatrix/g3.md)
- [var b3: Float](colormatrix/b3.md)
- [var a3: Float](colormatrix/a3.md)
### Fourth column
- [var r4: Float](colormatrix/r4.md)
- [var g4: Float](colormatrix/g4.md)
- [var b4: Float](colormatrix/b4.md)
- [var a4: Float](colormatrix/a4.md)
### Fifth column
- [var r5: Float](colormatrix/r5.md)
- [var g5: Float](colormatrix/g5.md)
- [var b5: Float](colormatrix/b5.md)
- [var a5: Float](colormatrix/a5.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func blur(radius: CGFloat, opaque: Bool) -> some View](view/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](view/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colormatrix)*