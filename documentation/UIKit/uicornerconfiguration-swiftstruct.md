# UICornerConfiguration

**Framework**: UIKit  
**Kind**: struct

A configuration that defines how corner radii are mapped to the corners of a rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct UICornerConfiguration
```

#### Overview

Create a `UICornerConfiguration` that expresses how you want the corners of your view to appear. Your configuration can apply to corners independently or uniformly, and can form the following types of corners:

- A squared corner
- A rounded corner
- A rounded corner that’s concentric relative to the containing view
- Corners that are rounded to form a capsule

Select a method to create a configuration that describes which corners of your view you want to be uniform and which corners you want to be independent, then provide instances of [`UICornerRadius`](uicornerradius-swift.struct.md) as parameters to indicate which type you want each corner to be.

The system uses squared corners by default, so you don’t need to set a configuration to get squared corners.

##### Configure a Rounded Corner

To configure a rounded corner with a fixed radius, provide [`fixed(_:)`](uicornerradius-swift.struct/fixed(_:).md) with a value greater than zero for the radius. Since `UICornerRadius` conforms to `ExpressibleByFloatLiteral` and `ExpressibleByIntegerLiteral`, you can also provide a float or integer value for the radius:

```swift
myView.cornerConfiguration = .corners(radius: 12.0)
```

##### Configure a Concentric Rounded Corner

To configure a rounded corner that’s concentric relative to the containing view, use [`containerConcentric(minimum:)`](uicornerradius-swift.struct/containerconcentric(minimum:).md):

```swift
myView.cornerConfiguration = .corners(radius: .containerConcentric())
```

Set the `minimum` parameter to indicate a minimum radius for the rounded corner.

##### Configure a Corner As a Capsule

To configure rounded corners that form a capsule, use [`capsule(maximumRadius:)`](uicornerconfiguration-swift.struct/capsule(maximumradius:).md):

```swift
myView.cornerConfiguration = .capsule()
```

Set the `maximumRadius` parameter to allow your view to break the capsule paradigm and stretch vertically with an edge if the radius necessary to form a capsule exceeds what you provide.

## Topics

### Configuring independent corners
- [static func corners(radius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/corners(radius:).md)
  A configuration that applies the given radius independently to all corners.
- [static func corners(topLeftRadius: UICornerRadius?, topRightRadius: UICornerRadius?, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:).md)
  A configuration with independent radii for each corner.
### Configuring corners as a capsule
- [static func capsule(maximumRadius: Double?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/capsule(maximumradius:).md)
  A configuration that rounds the corners into a capsule shape, scaling with the view’s size up to the maximum radius you provide.
### Configuring uniform corners
- [static func uniformCorners(radius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformcorners(radius:).md)
  A configuration that applies the given radius uniformly to all corners.
- [static func uniformEdges(leftRadius: UICornerRadius, rightRadius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformedges(leftradius:rightradius:).md)
  A configuration that applies the left radius you provide to the left corners, and the right radius you provide to the right corners.
- [static func uniformEdges(topRadius: UICornerRadius, bottomRadius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformedges(topradius:bottomradius:).md)
  A configuration that applies the top radius to the top corners, and the bottom radius you provide to the bottom corners.
- [static func uniformBottomRadius(UICornerRadius, topLeftRadius: UICornerRadius?, topRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformbottomradius(_:topleftradius:toprightradius:).md)
  A configuration that applies the radius you provide to the bottom corners, with optional independent radii for the top corners.
- [static func uniformLeftRadius(UICornerRadius, topRightRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformleftradius(_:toprightradius:bottomrightradius:).md)
  A configuration that applies the left radius to the left corners, with optional independent radii for the right corners.
- [static func uniformRightRadius(UICornerRadius, topLeftRadius: UICornerRadius?, bottomLeftRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformrightradius(_:topleftradius:bottomleftradius:).md)
  A configuration that applies the right radius you provide to the right corners, with optional independent radii for the left corners.
- [static func uniformTopRadius(UICornerRadius, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformtopradius(_:bottomleftradius:bottomrightradius:).md)
  A configuration that applies the top radius you provide to the top corners, with optional independent radii for the bottom corners.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var cornerConfiguration: UICornerConfiguration](uiview/cornerconfiguration-7l0ja.md)
  A configuration that defines the corners of the view.
- [struct UICornerRadius](uicornerradius-swift.struct.md)
  A type that represents the radius the system uses to round a corner.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](uiview/effectiveradius(corner:).md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct)*