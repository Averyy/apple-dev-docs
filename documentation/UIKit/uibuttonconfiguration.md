# UIButtonConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration that specifies the appearance and behavior of a button and its contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIButtonConfiguration : NSObject
```

#### Overview

You can configure and update a button with a [`UIButtonConfiguration`](./uibuttonconfiguration.md). A button configuration contains all the customization options available with other methods, such as [`setTitle(_:for:)`](./uibutton/settitle%28_,for%29.md), and can serve as a replacement for those methods. Alternatively, you can use a configuration in combination with these other methods and adopt new button behaviors and appearance without rewriting your customized [`UIButton`](./uibutton.md) code.

## Topics

### Creating configurations
- [+ plainButtonConfiguration](./uibuttonconfiguration/plainbuttonconfiguration.md)
  Creates a configuration for a button with a transparent background.
- [+ grayButtonConfiguration](./uibuttonconfiguration/graybuttonconfiguration.md)
  Creates a configuration for a button with a gray background.
- [+ tintedButtonConfiguration](./uibuttonconfiguration/tintedbuttonconfiguration.md)
  Creates a configuration for a button with a tinted background color.
- [+ filledButtonConfiguration](./uibuttonconfiguration/filledbuttonconfiguration.md)
  Creates a configuration for a button with a background filled with the button’s tint color.
- [+ borderlessButtonConfiguration](./uibuttonconfiguration/borderlessbuttonconfiguration.md)
  Creates a configuration for a button that has a borderless style.
- [+ borderedButtonConfiguration](./uibuttonconfiguration/borderedbuttonconfiguration.md)
  Creates a configuration for a button that has a bordered style.
- [+ borderedTintedButtonConfiguration](./uibuttonconfiguration/borderedtintedbuttonconfiguration.md)
  Creates a configuration for a button that has a tinted, bordered style.
- [+ borderedProminentButtonConfiguration](./uibuttonconfiguration/borderedprominentbuttonconfiguration.md)
  Creates a configuration for a button that has a prominent, bordered style.
- [+ glassButtonConfiguration](./uibuttonconfiguration/glassbuttonconfiguration.md)
  Creates a configuration for a button that has a Liquid Glass style.
- [+ prominentGlassButtonConfiguration](./uibuttonconfiguration/prominentglassbuttonconfiguration.md)
  Creates a configuration for a button that has a prominent Liquid Glass style.
- [+ clearGlassButtonConfiguration](./uibuttonconfiguration/clearglassbuttonconfiguration.md)
  Creates a configuration for a button that has a clear Liquid Glass style.
- [+ prominentClearGlassButtonConfiguration](./uibuttonconfiguration/prominentclearglassbuttonconfiguration.md)
  Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [- updatedConfigurationForButton:](./uibuttonconfiguration/updatedconfigurationforbutton_.md)
  Returns a copy of the configuration, updated for the given button.
### Configuring titles
- [title](./uibuttonconfiguration/title.md)
  The text of the title label the button displays.
- [subtitle](./uibuttonconfiguration/subtitle.md)
  The text the subtitle label of the button displays.
- [attributedTitle](./uibuttonconfiguration/attributedtitle.md)
  The text and style attributes for the button’s title label.
- [attributedSubtitle](./uibuttonconfiguration/attributedsubtitle.md)
  The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](./uibuttonconfiguration/titletextattributestransformer.md)
  A transformer to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](./uibuttonconfiguration/subtitletextattributestransformer.md)
  A transformer to update the attributed subtitle when the button state changes.
- [UIConfigurationTextAttributesTransformer](./uiconfigurationtextattributestransformer-c.typealias.md)
  Defines a text transformation that can affect the visual appearance of a string.
- [titlePadding](./uibuttonconfiguration/titlepadding.md)
  The distance between the title and subtitle labels.
- [titleAlignment](./uibuttonconfiguration/titlealignment.md)
  The text alignment the button uses to lay out the title and subtitle.
- [UIButtonConfigurationTitleAlignment](./uibuttonconfigurationtitlealignment.md)
  Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](./uibuttonconfiguration/titlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](./uibuttonconfiguration/subtitlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s subtitle.
### Configuring images
- [image](./uibuttonconfiguration/image.md)
  The foreground image the button displays.
- [imagePadding](./uibuttonconfiguration/imagepadding.md)
  The distance between the button’s image and text.
- [imagePlacement](./uibuttonconfiguration/imageplacement.md)
  The edge against which the button places the image.
- [imageColorTransformer](./uibuttonconfiguration/imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](./uibuttonconfiguration/preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.
### Configuring layout
- [buttonSize](./uibuttonconfiguration/buttonsize.md)
  A size that requests a preferred size for the button.
- [UIButtonConfigurationSize](./uibuttonconfigurationsize.md)
  A predefined size for button elements.
- [contentInsets](./uibuttonconfiguration/contentinsets.md)
  The distance from the button’s content area to its bounds.
- [- setDefaultContentInsets](./uibuttonconfiguration/setdefaultcontentinsets.md)
  Restores the default content insets.
### Configuring button colors
- [baseBackgroundColor](./uibuttonconfiguration/basebackgroundcolor.md)
  The untransformed color for background views.
- [baseForegroundColor](./uibuttonconfiguration/baseforegroundcolor.md)
  The untransformed color for foreground views.
### Configuring the button background
- [background](./uibuttonconfiguration/background.md)
  The configuration to customize the button background.
- [cornerStyle](./uibuttonconfiguration/cornerstyle.md)
  The button style that controls the display behavior of the background corner radius.
- [UIButtonConfigurationCornerStyle](./uibuttonconfigurationcornerstyle.md)
  Settings that determine the appearance of the background corner radius.
### Configuring the indicator
- [indicator](./uibuttonconfiguration/indicator.md)
  The style of the indicator that appears on the button.
- [UIButtonConfigurationIndicator](./uibuttonconfigurationindicator.md)
  Constants that determine the style of the indicator that appears on a button.
- [indicatorColorTransformer](./uibuttonconfiguration/indicatorcolortransformer.md)
  The color transformer for resolving the indicator color.
### Configuring the activity indicator
- [showsActivityIndicator](./uibuttonconfiguration/showsactivityindicator.md)
  A Boolean value that determines whether the button displays an activity indicator instead of an image.
- [activityIndicatorColorTransformer](./uibuttonconfiguration/activityindicatorcolortransformer.md)
  The color transformer for resolving the color of the activity indicator.
### Configuring selection behavior
- [automaticallyUpdateForSelection](./uibuttonconfiguration/automaticallyupdateforselection.md)
  A Boolean value that determines whether the style automatically updates when the button is in a selected state.
### Configuring the appearance on macOS
- [macIdiomStyle](./uibuttonconfiguration/macidiomstyle.md)
  The style to use when this button appears in macOS.
- [UIButtonConfigurationMacIdiomStyle](./uibuttonconfigurationmacidiomstyle.md)
  The button style your app uses when running in macOS.
### Instance Properties
- [symbolContentTransition](./uibuttonconfiguration/symbolcontenttransition.md)
  The symbol content transition to use when transitioning across symbol images. Defaults to `nil`, meaning no symbol content transition should occur.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Creating buttons from a configuration object
- [+ buttonWithConfiguration:primaryAction:](./uibutton/buttonwithconfiguration_primaryaction_.md)
  Creates a new button with the specified configuration and registers the primary action event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration)*