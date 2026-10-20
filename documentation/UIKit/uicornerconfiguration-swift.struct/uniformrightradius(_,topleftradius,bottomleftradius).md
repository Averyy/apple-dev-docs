# uniformRightRadius(_:topLeftRadius:bottomLeftRadius:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A configuration that applies the right radius you provide to the right corners, with optional independent radii for the left corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func uniformRightRadius(_ rightRadius: UICornerRadius, topLeftRadius: UICornerRadius? = nil, bottomLeftRadius: UICornerRadius? = nil) -> UICornerConfiguration
```

## Parameters

- `rightRadius`: A [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the top-right and bottom-right corners.
- `topLeftRadius`: An optional [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the top-left corner.
- `bottomLeftRadius`: An optional [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the bottom-left corner.

## See Also

### Configuring uniform corners
- [static func uniformCorners(radius: UICornerRadius) -> UICornerConfiguration](./uniformcorners%28radius%29.md)
  A configuration that applies the given radius uniformly to all corners.
- [static func uniformEdges(leftRadius: UICornerRadius, rightRadius: UICornerRadius) -> UICornerConfiguration](./uniformedges%28leftradius,rightradius%29.md)
  A configuration that applies the left radius you provide to the left corners, and the right radius you provide to the right corners.
- [static func uniformEdges(topRadius: UICornerRadius, bottomRadius: UICornerRadius) -> UICornerConfiguration](./uniformedges%28topradius,bottomradius%29.md)
  A configuration that applies the top radius to the top corners, and the bottom radius you provide to the bottom corners.
- [static func uniformBottomRadius(UICornerRadius, topLeftRadius: UICornerRadius?, topRightRadius: UICornerRadius?) -> UICornerConfiguration](./uniformbottomradius%28_,topleftradius,toprightradius%29.md)
  A configuration that applies the radius you provide to the bottom corners, with optional independent radii for the top corners.
- [static func uniformLeftRadius(UICornerRadius, topRightRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](./uniformleftradius%28_,toprightradius,bottomrightradius%29.md)
  A configuration that applies the left radius to the left corners, with optional independent radii for the right corners.
- [static func uniformTopRadius(UICornerRadius, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](./uniformtopradius%28_,bottomleftradius,bottomrightradius%29.md)
  A configuration that applies the top radius you provide to the top corners, with optional independent radii for the bottom corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/uniformrightradius(_:topleftradius:bottomleftradius:))*