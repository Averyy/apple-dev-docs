# uniformBottomRadius(_:topLeftRadius:topRightRadius:)

**Framework**: UIKit  
**Kind**: method

A configuration that applies the radius you provide to the bottom corners, with optional independent radii for the top corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func uniformBottomRadius(_ bottomRadius: UICornerRadius, topLeftRadius: UICornerRadius? = nil, topRightRadius: UICornerRadius? = nil) -> UICornerConfiguration
```

## Parameters

- `bottomRadius`: A   that represents the radius to use for the bottom-left and bottom-right corners.
- `topLeftRadius`: An optional   that represents the radius to use for the top-left corner.
- `topRightRadius`: An optional   that represents the radius to use for the top-right corner.

## See Also

- [static func uniformCorners(radius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformcorners(radius:).md)
  A configuration that applies the given radius uniformly to all corners.
- [static func uniformEdges(leftRadius: UICornerRadius, rightRadius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformedges(leftradius:rightradius:).md)
  A configuration that applies the left radius you provide to the left corners, and the right radius you provide to the right corners.
- [static func uniformEdges(topRadius: UICornerRadius, bottomRadius: UICornerRadius) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformedges(topradius:bottomradius:).md)
  A configuration that applies the top radius to the top corners, and the bottom radius you provide to the bottom corners.
- [static func uniformLeftRadius(UICornerRadius, topRightRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformleftradius(_:toprightradius:bottomrightradius:).md)
  A configuration that applies the left radius to the left corners, with optional independent radii for the right corners.
- [static func uniformRightRadius(UICornerRadius, topLeftRadius: UICornerRadius?, bottomLeftRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformrightradius(_:topleftradius:bottomleftradius:).md)
  A configuration that applies the right radius you provide to the right corners, with optional independent radii for the left corners.
- [static func uniformTopRadius(UICornerRadius, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/uniformtopradius(_:bottomleftradius:bottomrightradius:).md)
  A configuration that applies the top radius you provide to the top corners, with optional independent radii for the bottom corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/uniformbottomradius(_:topleftradius:toprightradius:))*