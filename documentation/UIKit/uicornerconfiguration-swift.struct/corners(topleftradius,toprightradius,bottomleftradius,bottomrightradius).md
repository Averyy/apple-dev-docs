# corners(topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A configuration with independent radii for each corner.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func corners(topLeftRadius: UICornerRadius?, topRightRadius: UICornerRadius?, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration
```

## Parameters

- `topLeftRadius`: A [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the top-left corner.
- `topRightRadius`: A [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the top-right corner.
- `bottomLeftRadius`: A [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the bottom-left corner.
- `bottomRightRadius`: A [`UICornerRadius`](../uicornerradius-swift.struct.md) that represents the radius to use for the bottom-right corner.

## See Also

### Configuring independent corners
- [static func corners(radius: UICornerRadius) -> UICornerConfiguration](./corners%28radius%29.md)
  A configuration that applies the given radius independently to all corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:))*