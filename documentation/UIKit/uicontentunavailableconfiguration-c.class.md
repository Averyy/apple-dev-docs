# UIContentUnavailableConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A content configuration for a content-unavailable view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIContentUnavailableConfiguration : NSObject
```

## Overview

A content-unavailable configuration is a composable description of a view that indicates that your app can’t display content. Using a content-unavailable configuration, you can obtain system default styling for a variety of different empty states. Fill the configuration with placeholder content, and then assign it to a view controller’s [`contentUnavailableConfiguration`](./uiviewcontroller/contentunavailableconfiguration-6kqfk.md), or to a [`UIContentUnavailableView`](./uicontentunavailableview.md).

The following screenshot shows an example of a content-unavailable view configured by setting the [`image`](./uicontentunavailableconfiguration-c.class/image.md), [`text`](./uicontentunavailableconfiguration-c.class/text.md), and [`secondaryText`](./uicontentunavailableconfiguration-c.class/secondarytext.md) properties.

![A screenshot of a content-unavailable view indicating that there are no reminders in the Work folder.](https://developer.apple.com/tutorials/images/com.apple.uikit/uicontentunavailableconfiguration@2x.png)

## Topics

### Instance Properties
- [alignment](./uicontentunavailableconfiguration-c.class/alignment.md)
  The alignment of the image, text, and buttons.
- [attributedText](./uicontentunavailableconfiguration-c.class/attributedtext.md)
  An attributed variant of the primary text.
- [axesPreservingSuperviewLayoutMargins](./uicontentunavailableconfiguration-c.class/axespreservingsuperviewlayoutmargins.md)
  Configures which margins use the layout margins inherited from the superview.
- [background](./uicontentunavailableconfiguration-c.class/background.md)
  The configuration for the background.
- [button](./uicontentunavailableconfiguration-c.class/button.md)
  The configuration for the primary button.
- [buttonProperties](./uicontentunavailableconfiguration-c.class/buttonproperties.md)
  Additional configuration for the primary button.
- [buttonToSecondaryButtonPadding](./uicontentunavailableconfiguration-c.class/buttontosecondarybuttonpadding.md)
  The padding between the primary button and secondary button.
- [directionalLayoutMargins](./uicontentunavailableconfiguration-c.class/directionallayoutmargins.md)
  The margins between the content and the edges of the content view.
- [image](./uicontentunavailableconfiguration-c.class/image.md)
  The image to display.
- [imageProperties](./uicontentunavailableconfiguration-c.class/imageproperties.md)
  The configuration for the image.
- [imageToTextPadding](./uicontentunavailableconfiguration-c.class/imagetotextpadding.md)
  The padding between the image and the primary text.
- [secondaryAttributedText](./uicontentunavailableconfiguration-c.class/secondaryattributedtext.md)
  An attributed variant of the secondary text.
- [secondaryButton](./uicontentunavailableconfiguration-c.class/secondarybutton.md)
  The configuration for the secondary button.
- [secondaryButtonProperties](./uicontentunavailableconfiguration-c.class/secondarybuttonproperties.md)
  Additional configuration for the secondary button.
- [secondaryText](./uicontentunavailableconfiguration-c.class/secondarytext.md)
  The secondary text to display.
- [secondaryTextProperties](./uicontentunavailableconfiguration-c.class/secondarytextproperties.md)
  Properties for configuring the secondary text.
- [text](./uicontentunavailableconfiguration-c.class/text.md)
  The primary text to display.
- [textProperties](./uicontentunavailableconfiguration-c.class/textproperties.md)
  Properties for configuring the primary text.
- [textToButtonPadding](./uicontentunavailableconfiguration-c.class/texttobuttonpadding.md)
  The padding between the text and buttons.
- [textToSecondaryTextPadding](./uicontentunavailableconfiguration-c.class/texttosecondarytextpadding.md)
  The padding between the primary and secondary text.
### Type Methods
- [+ emptyConfiguration](./uicontentunavailableconfiguration-c.class/emptyconfiguration.md)
  Creates a configuration ready to customize.
- [+ loadingConfiguration](./uicontentunavailableconfiguration-c.class/loadingconfiguration.md)
  Creates a configuration appropriate for indicating a view is waiting on content to load.
- [+ searchConfiguration](./uicontentunavailableconfiguration-c.class/searchconfiguration.md)
  Creates a configuration appropriate for indicating an empty search result.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [UIContentConfiguration](./uicontentconfiguration-2raci.md)

## See Also

### Unavailable content configurations
- [UIContentUnavailableConfigurationState](./uicontentunavailableconfigurationstate-c.class.md)
  An object that encapsulates state for a content-unavailable view.
- [UIContentUnavailableButtonProperties](./uicontentunavailablebuttonproperties.md)
  Properties configuring the appearance and behavior of a button in a content-unavailable view.
- [UIContentUnavailableImageProperties](./uicontentunavailableimageproperties.md)
  Properties configuring the appearance of images in a content-unavailable view.
- [UIContentUnavailableTextProperties](./uicontentunavailabletextproperties.md)
  Properties configuring the appearance of text in a content-unavailable view.
- [UIContentUnavailableAlignment](./uicontentunavailablealignment.md)
  Defines the alignment of views in a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-c.class)*