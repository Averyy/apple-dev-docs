# UICornerConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration that defines how corner radii are mapped to the corners of a rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface UICornerConfiguration : NSObject
```

## Overview

Create a `UICornerConfiguration` that expresses how you want the corners of your view to appear. Your configuration can apply to corners independently or uniformly, and can form the following types of corners:

- A squared corner
- A rounded corner
- A rounded corner that’s concentric relative to the containing view
- Corners that are rounded to form a capsule

Select a method to create a configuration that describes which corners of your view you want to be uniform and which corners you want to be independent, then provide instances of [`UICornerRadius`](./uicornerradius-c.class.md) as parameters to indicate which type you want each corner to be.

The system uses squared corners by default, so you don’t need to set a configuration to get squared corners.

### Configure a rounded corner

To configure a rounded corner with a fixed radius, provide [`fixedRadius:`](./uicornerradius-c.class/fixedradius_.md) with a value greater than zero for the radius:

```objc
[myView setCornerConfiguration:
 [UICornerConfiguration configurationWithRadius:
  [UICornerRadius fixedRadius:12.0]]];
```

### Configure a concentric rounded corner

To configure a rounded corner that’s concentric relative to the containing view, use [`containerConcentricRadius`](./uicornerradius-c.class/containerconcentricradius.md):

```objc
[myView setCornerConfiguration:
 [UICornerConfiguration configurationWithRadius:
  [UICornerRadius containerConcentricRadius]]];
```

Use [`containerConcentricRadiusWithMinimum:`](./uicornerradius-c.class/containerconcentricradiuswithminimum_.md) to indicate a minimum radius for the rounded corner.

### Configure a corner as a capsule

To configure rounded corners that form a capsule, use [`capsuleConfiguration`](./uicornerconfiguration-c.class/capsuleconfiguration.md):

```objc
[myView setCornerConfiguration:
 [UICornerConfiguration capsuleConfiguration]];
```

Use [`capsuleConfigurationWithMaximumRadius:`](./uicornerconfiguration-c.class/capsuleconfigurationwithmaximumradius_.md) to allow your view to break the capsule paradigm and stretch vertically with an edge if the radius necessary to form a capsule exceeds what you provide.

## Topics

### Configuring independent corners
- [+ configurationWithRadius:](./uicornerconfiguration-c.class/configurationwithradius_.md)
  A configuration that applies the given radius independently to all corners.
- [+ configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:](./uicornerconfiguration-c.class/configurationwithtopleftradius_toprightradius_bottomleftradius_bottomrightradius_.md)
  A configuration with independent radii for each corner.
### Configuring corners as a capsule
- [+ capsuleConfiguration](./uicornerconfiguration-c.class/capsuleconfiguration.md)
  A configuration that rounds the corners into a capsule shape, scaling with the view’s size.
- [+ capsuleConfigurationWithMaximumRadius:](./uicornerconfiguration-c.class/capsuleconfigurationwithmaximumradius_.md)
  A configuration that rounds the corners into a capsule shape, scaling with the view’s size and clamped to the `maximumRadius`.
### Configuring uniform corners
- [+ configurationWithUniformRadius:](./uicornerconfiguration-c.class/configurationwithuniformradius_.md)
  A configuration that applies the given radius uniformly to all corners.
- [+ configurationWithUniformLeftRadius:uniformRightRadius:](./uicornerconfiguration-c.class/configurationwithuniformleftradius_uniformrightradius_.md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, and the `rightRadius` uniformly to the top-right and bottom-right corners.
- [+ configurationWithUniformTopRadius:uniformBottomRadius:](./uicornerconfiguration-c.class/configurationwithuniformtopradius_uniformbottomradius_.md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, and the `bottomRadius` uniformly to the bottom-left and bottom-right corners.
- [+ configurationWithUniformBottomRadius:topLeftRadius:topRightRadius:](./uicornerconfiguration-c.class/configurationwithuniformbottomradius_topleftradius_toprightradius_.md)
  A configuration that applies the `bottomRadius` uniformly to the bottom-left and bottom-right corners, with optional independent radii for the top-left and top-right corners.
- [+ configurationWithUniformLeftRadius:topRightRadius:bottomRightRadius:](./uicornerconfiguration-c.class/configurationwithuniformleftradius_toprightradius_bottomrightradius_.md)
  A configuration that applies the `leftRadius` uniformly to the top-left and bottom-left corners, with optional independent radii for the top-right and bottom-right corners.
- [+ configurationWithUniformRightRadius:topLeftRadius:bottomLeftRadius:](./uicornerconfiguration-c.class/configurationwithuniformrightradius_topleftradius_bottomleftradius_.md)
  A configuration that applies the `rightRadius` uniformly to the top-right and bottom-right corners, with optional independent radii for the top-left and bottom-left corners.
- [+ configurationWithUniformTopRadius:bottomLeftRadius:bottomRightRadius:](./uicornerconfiguration-c.class/configurationwithuniformtopradius_bottomleftradius_bottomrightradius_.md)
  A configuration that applies the `topRadius` uniformly to the top-left and top-right corners, with optional independent radii for the bottom-left and bottom-right corners.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Configuring a view’s corners
- [cornerConfiguration](./uiview/cornerconfiguration-3m8ya.md)
  A configuration that defines the corners of the view.
- [UICornerRadius](./uicornerradius-c.class.md)
  A type that represents the radius the system uses to round a corner.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](./uiview/effectiveradius%28corner%29.md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicornerconfiguration-c.class)*