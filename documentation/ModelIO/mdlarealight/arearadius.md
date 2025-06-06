# areaRadius

**Framework**: Model I/O  
**Kind**: property

The radius, in units of local coordinate space, of the area from which light emanates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var areaRadius: Float { get set }
```

#### Discussion

The effect of radius on a light’s shape depends on the value of its inherited [`lightType`](mdllight/lighttype.md) property:

- [`MDLLightType.linear`](mdllighttype/linear.md): The light is shaped like a line segment, centered on the origin of its local coordinate space and extending along the x-axis with a total length of twice the [`areaRadius`](mdlarealight/arearadius.md) value.
- [`MDLLightType.discArea`](mdllighttype/discarea.md): The light is shaped like a circle or ellipse in the xy-plane of its local coordinate space. If the [`aspect`](mdlarealight/aspect.md) value is `1.0`, the [`areaRadius`](mdlarealight/arearadius.md) value is the circle’s radius. If the [`aspect`](mdlarealight/aspect.md) value is less than one, the [`areaRadius`](mdlarealight/arearadius.md) value is the major radius of the ellipse, and the minor radius is equal to the [`areaRadius`](mdlarealight/arearadius.md) value times the [`aspect`](mdlarealight/aspect.md) value.
- [`MDLLightType.rectangularArea`](mdllighttype/rectangulararea.md): The light is shaped like a rectangle in the xy-plane of its local coordinate space. If the [`aspect`](mdlarealight/aspect.md) value is `1.0`, the light is a square and [`areaRadius`](mdlarealight/arearadius.md) value is half the square’s width or length. If the [`aspect`](mdlarealight/aspect.md) value is less than one, the [`areaRadius`](mdlarealight/arearadius.md) value is half the rectangle’s longer dimension, and the shorter dimension is the [`areaRadius`](mdlarealight/arearadius.md) value, times the [`aspect`](mdlarealight/aspect.md) value, times two.
- [`MDLLightType.superElliptical`](mdllighttype/superelliptical.md): The light is shaped like a superellipse—a two-dimensional figure in the xy-plane of its local coordinate space that can vary between shapes such as stars, diamonds, circles, and squares with rounded corners. The [`superEllipticPower`](mdlarealight/superellipticpower.md) property determines the general shape of the light, and the [`aspect`](mdlarealight/aspect.md) property controls the ratio of the longer and shorter dimensions of the shape.

## See Also

- [var aspect: Float](mdlarealight/aspect.md)
  The aspect ratio of the light’s shape.
- [var superEllipticPower: vector_float2](mdlarealight/superellipticpower.md)
  A vector that controls the roundness of a superelliptical light in the x- and y-axis directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlarealight/arearadius)*