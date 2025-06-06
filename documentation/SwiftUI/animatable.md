# Animatable

**Framework**: SwiftUI  
**Kind**: protocol

A type that describes how to animate a property of a view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol Animatable
```

## Topics

### Animating data
- [var animatableData: Self.AnimatableData](animatable/animatabledata-6nydg.md)
  The data to animate.
- [associatedtype AnimatableData : VectorArithmetic](animatable/animatabledata-swift.associatedtype.md)
  The type defining the data to animate.

## Relationships

### Inherited By
- [AnimatableModifier](animatablemodifier.md)
- [GeometryEffect](geometryeffect.md)
- [InsettableShape](insettableshape.md)
- [Layout](layout.md)
- [Shape](shape.md)
- [TextRenderer](textrenderer.md)
- [VisualEffect](visualeffect.md)
### Conforming Types
- [Angle](angle.md)
- [AnyLayout](anylayout.md)
- [AnyShape](anyshape.md)
- [ButtonBorderShape](buttonbordershape.md)
- [Capsule](capsule.md)
- [Circle](circle.md)
- [Color.Resolved](color/resolved.md)
- [ContainerRelativeShape](containerrelativeshape.md)
- [EdgeInsets](edgeinsets.md)
- [EdgeInsets3D](edgeinsets3d.md)
- [Ellipse](ellipse.md)
- [EmptyVisualEffect](emptyvisualeffect.md)
- [GridLayout](gridlayout.md)
- [HStackLayout](hstacklayout.md)
- [OffsetShape](offsetshape.md)
- [Path](path.md)
- [Rectangle](rectangle.md)
- [RectangleCornerRadii](rectanglecornerradii.md)
- [RotatedShape](rotatedshape.md)
- [RoundedRectangle](roundedrectangle.md)
- [ScaledShape](scaledshape.md)
- [StrokeStyle](strokestyle.md)
- [TransformedShape](transformedshape.md)
- [UnevenRoundedRectangle](unevenroundedrectangle.md)
- [UnitPoint](unitpoint.md)
- [UnitPoint3D](unitpoint3d.md)
- [VStackLayout](vstacklayout.md)
- [ZStackLayout](zstacklayout.md)

## See Also

- [struct AnimatablePair](animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [protocol VectorArithmetic](vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.
- [struct EmptyAnimatableData](emptyanimatabledata.md)
  An empty type for animatable data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatable)*