# configurationWithUniformLeftRadius:uniformRightRadius:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, and the `rightRadius` uniformly to the top-right and bottom-right corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
+ (instancetype) configurationWithUniformLeftRadius:(UICornerRadius *) leftRadius uniformRightRadius:(UICornerRadius *) rightRadius;
```

## See Also

### Configuring uniform corners
- [+ configurationWithUniformRadius:](./configurationwithuniformradius_.md)
  A configuration that applies the given radius uniformly to all corners.
- [+ configurationWithUniformTopRadius:uniformBottomRadius:](./configurationwithuniformtopradius_uniformbottomradius_.md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, and the `bottomRadius` uniformly to the bottom-left and bottom-right corners.
- [+ configurationWithUniformBottomRadius:topLeftRadius:topRightRadius:](./configurationwithuniformbottomradius_topleftradius_toprightradius_.md)
  A configuration that applies the `bottomRadius` uniformly to the bottom-left and bottom-right corners, with optional independent radii for the top-left and top-right corners.
- [+ configurationWithUniformLeftRadius:topRightRadius:bottomRightRadius:](./configurationwithuniformleftradius_toprightradius_bottomrightradius_.md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, with optional independent radii for the top-right and bottom-right corners.
- [+ configurationWithUniformRightRadius:topLeftRadius:bottomLeftRadius:](./configurationwithuniformrightradius_topleftradius_bottomleftradius_.md)
  A configuration that applies the `rightRadius` uniformly to the top-right and bottom-right corners, with optional independent radii for the top-left and bottom-left corners.
- [+ configurationWithUniformTopRadius:bottomLeftRadius:bottomRightRadius:](./configurationwithuniformtopradius_bottomleftradius_bottomrightradius_.md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, with optional independent radii for the bottom-left and bottom-right corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-c.class/configurationwithuniformleftradius:uniformrightradius:)*