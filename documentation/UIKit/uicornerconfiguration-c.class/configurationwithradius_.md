# configurationWithRadius:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

A configuration that applies the given radius independently to all corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
+ (instancetype) configurationWithRadius:(UICornerRadius *) radius;
```

## Discussion

When used with a container concentric radius, this allows each individual corner to resolve to different radii.

## See Also

### Configuring independent corners
- [+ configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:](./configurationwithtopleftradius_toprightradius_bottomleftradius_bottomrightradius_.md)
  A configuration with independent radii for each corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-c.class/configurationwithradius:)*