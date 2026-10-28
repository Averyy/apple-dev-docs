# UIColor

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that stores color data and sometimes opacity.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class UIColor
```

```objc
@interface UIColor : NSObject
```

## Mentions

- [Customizing drawings](./customizing-drawings.md)
- [Determining color values with color spaces](./determining-color-values-with-color-spaces.md)
- [Understanding a drag item as a promise](./understanding-a-drag-item-as-a-promise.md)

## Overview

Use color to customize your app’s appearance, communicate status, and help people visualize data. To learn more about using color in your apps, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/foundations/color/).

[`UIColor`](./uicolor.md) provides a list of class properties that create adaptable and fixed colors such as blue, green, purple, and more. [`UIColor`](./uicolor.md) also offers properties to specify system-provided colors for UI elements such as labels, text, and buttons. You can create color objects by specifying color component values such as RGB, hue, and saturation. You can also create colors from other color objects and even create a pattern-based color from an image.

> ❗ **Important**:  Most developers have no need to subclass [`UIColor`](./uicolor.md). The only time subclassing might be necessary is if you require support for additional color spaces or color models. If you do subclass, the properties and methods you add must be safe to use from multiple threads.

## Topics

### Getting existing colors
- [UI element colors](./ui-element-colors.md)
  Choose colors for UI elements such as labels, text, backgrounds, and links.
- [Standard colors](./standard-colors.md)
  Define standard color objects for specific shades, such as red, blue, green, black, white, and more.
- [Color creation](./color-creation.md)
  Load colors from asset catalogs and create colors from raw component values.
### Applying the color to the drawing environment
- [Customizing drawings](./customizing-drawings.md)
  Create custom colors and patterns for drawing in your app.
- [func set()](./uicolor/set%28%29.md)
  Sets the color of subsequent stroke and fill operations to the color that the receiver represents.
- [func setFill()](./uicolor/setfill%28%29.md)
  Sets the color of subsequent fill operations to the color that the receiver represents.
- [func setStroke()](./uicolor/setstroke%28%29.md)
  Sets the color of subsequent stroke operations to the color that the receiver represents.
### Getting the color information
- [Determining color values with color spaces](./determining-color-values-with-color-spaces.md)
  Change the system’s interpretation of a color value for display by selecting a color space.
- [var cgColor: CGColor](./uicolor/cgcolor.md)
  The Quartz color that corresponds to the color object.
- [var ciColor: CIColor](./uicolor/cicolor.md)
  The Core Image color that corresponds to the color object.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./uicolor/gethue%28_,saturation,brightness,alpha%29.md)
  Returns the components that form the color in the HSB color space.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./uicolor/getred%28_,green,blue,alpha%29.md)
  Returns the components that form the color in the RGB color space.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?) -> Bool](./uicolor/getwhite%28_,alpha%29.md)
  Returns the grayscale components of the color.
- [var linearExposure: CGFloat](./uicolor/linearexposure.md)
  The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [var accessibilityName: String](./uicolor/accessibilityname.md)
  A localized description of the color for accessibility attributes.
### Resolving a dynamically generated color
- [func resolvedColor(with: UITraitCollection) -> UIColor](./uicolor/resolvedcolor%28with%29.md)
  Returns the version of the current color that results from the specified traits.
### Working with color prominence
- [var prominence: UIColor.Prominence](./uicolor/prominence-swift.property.md)
- [func withProminence(UIColor.Prominence) -> UIColor](./uicolor/withprominence%28_%29.md)
  Returns the version of the current color that results from applying the specified prominence.
- [UIColor.Prominence](./uicolor/prominence-swift.enum.md)
  A type that indicates the prominence of a color in the interface.
### Working with high dynamic range (HDR) colors
- [func applyingContentHeadroom(CGFloat) -> UIColor](./uicolor/applyingcontentheadroom%28_%29.md)
  Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` >= 1.0.
- [var standardDynamicRange: UIColor](./uicolor/standarddynamicrange.md)
  In some cases it is useful to recover the color that was base SDR color that was exposed to generate the given HDR color. If a color’s `linearExposure` is >1, then this will return the base SDR color.
### Initializers
- [init(CGColor: CGColor)](./uicolor/init%28cgcolor%29-58l83.md)
- [init(CGColor: CGColor)](./uicolor/init%28cgcolor%29-9d9vs.md)
- [init(CIColor: CIColor)](./uicolor/init%28cicolor%29-2b5ik.md)
- [init(CIColor: CIColor)](./uicolor/init%28cicolor%29-5fqhu.md)
- [init?(coder: NSCoder)](./uicolor/init%28coder%29.md)
- [init?(named: String, in: Bundle?, compatibleWith: UITraitCollection?)](./uicolor/init%28named,in,compatiblewith%29.md)
### Default Implementations
- [UIColor Implementations](./uicolor/uicolor-implementations.md)
### Type Methods
- [+ colorWithRed:green:blue:alpha:exposure:](./uicolor/colorwithred_green_blue_alpha_exposure_.md)
- [+ colorWithRed:green:blue:alpha:linearExposure:](./uicolor/colorwithred_green_blue_alpha_linearexposure_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSItemProviderReading](../Foundation/nsitemproviderreading.md)
- [NSItemProviderWriting](../Foundation/nsitemproviderwriting.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor)*