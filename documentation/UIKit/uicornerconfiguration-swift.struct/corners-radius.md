# corners(radius:)

**Framework**: UIKit  
**Kind**: method

A configuration that applies the given radius independently to all corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func corners(radius: UICornerRadius) -> UICornerConfiguration
```

#### Discussion

Use a container concentric radius to allow each individual corner to resolve to different radii.

## Parameters

- `radius`: A   that represents a radius to apply to each corner.

## See Also

- [static func corners(topLeftRadius: UICornerRadius?, topRightRadius: UICornerRadius?, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration](uicornerconfiguration-swift.struct/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:).md)
  A configuration with independent radii for each corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/corners(radius:))*