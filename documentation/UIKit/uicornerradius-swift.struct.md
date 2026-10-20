# UICornerRadius

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A type that represents the radius the system uses to round a corner.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct UICornerRadius
```

## Topics

### Defining a radius
- [static func containerConcentric(minimum: CGFloat?) -> UICornerRadius](./uicornerradius-swift.struct/containerconcentric%28minimum%29.md)
  A dynamic corner radius calculated using the geometry of the view and its container limited to a minimum radius.
- [static func fixed(Double) -> UICornerRadius](./uicornerradius-swift.struct/fixed%28_%29.md)
  Creates a radius that represents a fixed corner radius in points.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Configuring a view’s corners
- [var cornerConfiguration: UICornerConfiguration](./uiview/cornerconfiguration-7l0ja.md)
  A configuration that defines the corners of the view.
- [struct UICornerConfiguration](./uicornerconfiguration-swift.struct.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](./uiview/effectiveradius%28corner%29.md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerradius-swift.struct)*