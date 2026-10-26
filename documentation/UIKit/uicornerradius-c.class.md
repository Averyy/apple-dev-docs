# UICornerRadius

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A type that represents the radius the system uses to round a corner.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface UICornerRadius : NSObject
```

## Topics

### Defining a radius
- [+ containerConcentricRadius](./uicornerradius-c.class/containerconcentricradius.md)
  A dynamic corner radius calculated using the geometry of the view and its container.
- [+ containerConcentricRadiusWithMinimum:](./uicornerradius-c.class/containerconcentricradiuswithminimum_.md)
  A dynamic corner radius calculated using the geometry of the view and its container limited to a minimum radius.
- [+ fixedRadius:](./uicornerradius-c.class/fixedradius_.md)
  A fixed corner radius in points.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Configuring a view’s corners
- [cornerConfiguration](./uiview/cornerconfiguration-3m8ya.md)
  A configuration that defines the corners of the view.
- [UICornerConfiguration](./uicornerconfiguration-c.class.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](./uiview/effectiveradius%28corner%29.md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerradius-c.class)*