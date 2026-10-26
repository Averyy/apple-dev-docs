# UICornerCurve

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The corner curve to apply to a view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
enum UICornerCurve
```

```c
enum UICornerCurve : NSInteger;
```

## Topics

### Choosing a corner style
- [UICornerCurve.automatic](./uicornercurve/automatic.md)
  Selects the corner style automatically.
- [UICornerCurve.circular](./uicornercurve/circular.md)
  Always uses a circular corner style.
- [UICornerCurve.continuous](./uicornercurve/continuous.md)
  Always uses a continuous corner style.
### Initializers
- [init?(rawValue: Int)](./uicornercurve/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a hover shape
- [rectShape](./uishape-c.class/rectshape.md)
  Creates a rectangular shape.
- [capsuleShape](./uishape-c.class/capsuleshape.md)
  Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [circleShape](./uishape-c.class/circleshape.md)
  Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [+ rectShapeWithCornerRadius:](./uishape-c.class/rectshapewithcornerradius_.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius.
- [+ rectShapeWithCornerRadius:cornerCurve:](./uishape-c.class/rectshapewithcornerradius_cornercurve_.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius and corner curve.
- [+ rectShapeWithCornerRadius:cornerCurve:maskedCorners:](./uishape-c.class/rectshapewithcornerradius_cornercurve_maskedcorners_.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [+ fixedRectShapeWithRect:](./uishape-c.class/fixedrectshapewithrect_.md)
  Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [+ fixedRectShapeWithRect:cornerRadius:](./uishape-c.class/fixedrectshapewithrect_cornerradius_.md)
  Creates a fixed rectangular shape with the provided corner radius, using the provided rectangle as its shape.
- [+ fixedRectShapeWithRect:cornerRadius:cornerCurve:maskedCorners:](./uishape-c.class/fixedrectshapewithrect_cornerradius_cornercurve_maskedcorners_.md)
  Creates a fixed rectangular shape with the provided corner radius and corner curve, using the provided rectangle as its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornercurve)*