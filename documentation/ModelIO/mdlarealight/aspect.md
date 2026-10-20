# aspect

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The aspect ratio of the light’s shape.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var aspect: Float { get set }
```

```objc
@property (nonatomic, readwrite) float aspect;
```

#### Discussion

If the light’s type is [`MDLLightType.discArea`](../mdllighttype/discarea.md),  [`MDLLightType.rectangularArea`](../mdllighttype/rectangulararea.md), or [`MDLLightType.superElliptical`](../mdllighttype/superelliptical.md), this property determines the lengths of the shape’s major and minor axes (longer and shorter dimensions) relative to the [`areaRadius`](./arearadius.md) property’s value.

## See Also

### Managing a Light’s Shape
- [var areaRadius: Float](./arearadius.md)
  The radius, in units of local coordinate space, of the area from which light emanates.
- [var superEllipticPower: vector_float2](./superellipticpower.md)
  A vector that controls the roundness of a superelliptical light in the x- and y-axis directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlarealight/aspect)*