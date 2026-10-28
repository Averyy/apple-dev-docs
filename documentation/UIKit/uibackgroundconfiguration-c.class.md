# UIBackgroundConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration that describes a specific background appearance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIBackgroundConfiguration : NSObject
```

## Overview

Background configurations provide a lightweight way for you to create backgrounds for your views. Using a background configuration, you can obtain system default background styling for a variety of different view states. You apply background configurations directly to [`UIButton`](./uibutton.md) or to cells, headers, and footers in [`UICollectionView`](./uicollectionview.md) and [`UITableView`](./uitableview.md).

To use a background configuration:

1. Create a background configuration with one of the default system styles.
2. Modify the configuration to match your view’s style if you need additional customization.
3. Set the view’s current background configuration to your configuration.

```objc
UIBackgroundConfiguration *backgroundConfig = [UIBackgroundConfiguration listPlainCellConfiguration];

// Set a nil background color to use the view's tint color.
[backgroundConfig setBackgroundColor:nil];

[cell setBackgroundConfiguration:backgroundConfig];
```

You can also start by creating an empty background configuration using `clearConfiguration`, which produces a transparent background.

Each of the system background styles provides system default values for different configuration states ([`UIConfigurationState`](./uiconfigurationstate-8d7pd.md)). If you apply a background configuration to a view whose [`automaticallyUpdatesBackgroundConfiguration`](./uicollectionviewcell/automaticallyupdatesbackgroundconfiguration.md) property is [`true`](../Swift/true.md), the system automatically updates the background configuration when the view’s state changes.

If you want additional customization beyond the system default values, you can choose to manually update the background configuration by overriding the view’s `updateConfigurationUsingState` method.

```objc
- (void)updateConfigurationUsingState:(UICellConfigurationState *)state {
    // Get the system default background configuration for a plain style list cell in the current state.
    UIBackgroundConfiguration *backgroundConfig = [[UIBackgroundConfiguration listPlainCellConfiguration] updatedConfigurationForState:state];
    
    if (state.isHighlighted || state.isSelected) {
        [backgroundConfig setBackgroundColor:nil];
    }
    
    // Apply the background configuration to the cell.
    [self setBackgroundConfiguration:backgroundConfig];
}
```

When you apply a configuration to a view, UIKit performs the actual drawing and rendering of the background. When you use background configurations instead of rendering your own backgrounds, the system provides automatic view hierarchy management, support for interactive and interruptible animations and transitions, and performance optimizations.

## Topics

### Creating cell background configurations
- [+ listAccompaniedSidebarCellConfiguration](./uibackgroundconfiguration-c.class/listaccompaniedsidebarcellconfiguration.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.
### Creating an empty background configuration
- [+ clearConfiguration](./uibackgroundconfiguration-c.class/clearconfiguration.md)
  Creates an empty background configuration with a transparent background and no default styling.
### Customizing the background
- [customView](./uibackgroundconfiguration-c.class/customview.md)
  A custom view for the background.
- [cornerRadius](./uibackgroundconfiguration-c.class/cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [backgroundInsets](./uibackgroundconfiguration-c.class/backgroundinsets.md)
  The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [edgesAddingLayoutMarginsToBackgroundInsets](./uibackgroundconfiguration-c.class/edgesaddinglayoutmarginstobackgroundinsets.md)
  The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [backgroundColor](./uibackgroundconfiguration-c.class/backgroundcolor.md)
  The color of the background.
- [backgroundColorTransformer](./uibackgroundconfiguration-c.class/backgroundcolortransformer.md)
  The color transformer for resolving the background color.
- [- resolvedBackgroundColorForTintColor:](./uibackgroundconfiguration-c.class/resolvedbackgroundcolorfortintcolor_.md)
  Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [visualEffect](./uibackgroundconfiguration-c.class/visualeffect.md)
  The visual effect that the configuration applies to the background.
- [shadowProperties](./uibackgroundconfiguration-c.class/shadowproperties.md)
  Describes a shadow applied by the background. Defaults to no shadow (i.e. a shadow with an opacity of 0.0).
- [UIShadowProperties](./uishadowproperties-c.class.md)
- [strokeColor](./uibackgroundconfiguration-c.class/strokecolor.md)
  The color of the stroke.
- [strokeColorTransformer](./uibackgroundconfiguration-c.class/strokecolortransformer.md)
  The color transformer for resolving the stroke color.
- [- resolvedStrokeColorForTintColor:](./uibackgroundconfiguration-c.class/resolvedstrokecolorfortintcolor_.md)
  Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [strokeWidth](./uibackgroundconfiguration-c.class/strokewidth.md)
  The width of the stroke.
- [strokeOutset](./uibackgroundconfiguration-c.class/strokeoutset.md)
  The outset (or inset, if negative) for the stroke.
- [image](./uibackgroundconfiguration-c.class/image.md)
  The image displayed in the view’s background.
- [imageContentMode](./uibackgroundconfiguration-c.class/imagecontentmode.md)
  A property that determines the layout of a background image in a view when its bounds change.
### Updating background configurations
- [- updatedConfigurationForState:](./uibackgroundconfiguration-c.class/updatedconfigurationforstate_.md)
  Generates a configuration for the specified state by applying the configuration’s default values for that state to any properties that you haven’t customized.
### Deprecated
- [Deprecated symbols](./uibackgroundconfiguration-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Type Methods
- [+ listCellConfiguration](./uibackgroundconfiguration-c.class/listcellconfiguration.md)
  Represents a generic cell background configuration that automatically adopts the style of a containing list when updated for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the background configuration for a cell in a plain-style list.
- [+ listFooterConfiguration](./uibackgroundconfiguration-c.class/listfooterconfiguration.md)
  Represents a generic footer background configuration that automatically adopts the style of a containing list when updated for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the background configuration for a footer in a plain-style list.
- [+ listHeaderConfiguration](./uibackgroundconfiguration-c.class/listheaderconfiguration.md)
  Represents a generic header background configuration that automatically adopts the style of a containing list when updated for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the background configuration for a header in a plain-style list.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class)*