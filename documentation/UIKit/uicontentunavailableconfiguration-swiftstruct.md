# UIContentUnavailableConfiguration

**Framework**: UIKit  
**Kind**: struct

A content configuration for a content-unavailable view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
struct UIContentUnavailableConfiguration
```

#### Overview

A content-unavailable configuration is a composable description of a view that indicates your app can’t display content. Using a content-unavailable configuration, you can obtain system default styling for a variety of different empty states. Fill the configuration with placeholder content, and then assign it to a view controller’s [`contentUnavailableConfiguration`](uiviewcontroller/contentunavailableconfiguration-4b95e.md), or to a [`UIContentUnavailableView`](uicontentunavailableview.md).

The following screenshot shows an example of a content-unavailable view configured by setting the [`image`](uicontentunavailableconfiguration-swift.struct/image.md), [`text`](uicontentunavailableconfiguration-swift.struct/text.md), and [`secondaryText`](uicontentunavailableconfiguration-swift.struct/secondarytext.md) properties.

![A screenshot of a content-unavailable view indicating that a user has no files in the iCloud Drive Downloads folder.](https://docs-assets.developer.apple.com/published/7c656513bf8e80dc345aa2d89f317248/media-4274239%402x.png)

## Topics

### Structures
- [UIContentUnavailableConfiguration.ButtonProperties](uicontentunavailableconfiguration-swift.struct/buttonproperties-swift.struct.md)
  Properties to configure buttons for a content-unavailable view.
- [UIContentUnavailableConfiguration.ImageProperties](uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct.md)
  Properties to configure the image for a content-unavailable view.
- [UIContentUnavailableConfiguration.TextProperties](uicontentunavailableconfiguration-swift.struct/textproperties-swift.struct.md)
  Properties to configure text for a content-unavailable view.
### Instance Properties
- [var alignment: UIContentUnavailableConfiguration.Alignment](uicontentunavailableconfiguration-swift.struct/alignment-swift.property.md)
  The alignment of the image, text, and buttons.
- [var attributedText: NSAttributedString?](uicontentunavailableconfiguration-swift.struct/attributedtext.md)
  An attributed variant of the primary text.
- [var axesPreservingSuperviewLayoutMargins: UIAxis](uicontentunavailableconfiguration-swift.struct/axespreservingsuperviewlayoutmargins.md)
  Configures which margins use the layout margins inherited from the superview.
- [var background: UIBackgroundConfiguration](uicontentunavailableconfiguration-swift.struct/background.md)
  The configuration for the background.
- [var button: UIButton.Configuration](uicontentunavailableconfiguration-swift.struct/button.md)
  The configuration for the primary button.
- [var buttonProperties: UIContentUnavailableConfiguration.ButtonProperties](uicontentunavailableconfiguration-swift.struct/buttonproperties-swift.property.md)
  Additional configuration for the primary button.
- [var buttonToSecondaryButtonPadding: CGFloat](uicontentunavailableconfiguration-swift.struct/buttontosecondarybuttonpadding.md)
  The padding between the primary button and secondary button.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uicontentunavailableconfiguration-swift.struct/directionallayoutmargins.md)
  The margins between the content and the edges of the content view.
- [var image: UIImage?](uicontentunavailableconfiguration-swift.struct/image.md)
  The image to display.
- [var imageProperties: UIContentUnavailableConfiguration.ImageProperties](uicontentunavailableconfiguration-swift.struct/imageproperties-swift.property.md)
  The configuration for the image.
- [var imageToTextPadding: CGFloat](uicontentunavailableconfiguration-swift.struct/imagetotextpadding.md)
  The padding between the image and the primary text.
- [var secondaryAttributedText: NSAttributedString?](uicontentunavailableconfiguration-swift.struct/secondaryattributedtext.md)
  An attributed variant of the secondary text.
- [var secondaryButton: UIButton.Configuration](uicontentunavailableconfiguration-swift.struct/secondarybutton.md)
  The configuration for the secondary button.
- [var secondaryButtonProperties: UIContentUnavailableConfiguration.ButtonProperties](uicontentunavailableconfiguration-swift.struct/secondarybuttonproperties.md)
  Additional configuration for the secondary button.
- [var secondaryText: String?](uicontentunavailableconfiguration-swift.struct/secondarytext.md)
  The secondary text to display.
- [var secondaryTextProperties: UIContentUnavailableConfiguration.TextProperties](uicontentunavailableconfiguration-swift.struct/secondarytextproperties.md)
  Properties for configuring the secondary text.
- [var text: String?](uicontentunavailableconfiguration-swift.struct/text.md)
  The primary text to display.
- [var textProperties: UIContentUnavailableConfiguration.TextProperties](uicontentunavailableconfiguration-swift.struct/textproperties-swift.property.md)
  Properties for configuring the primary text.
- [var textToButtonPadding: CGFloat](uicontentunavailableconfiguration-swift.struct/texttobuttonpadding.md)
  The padding between the text and buttons.
- [var textToSecondaryTextPadding: CGFloat](uicontentunavailableconfiguration-swift.struct/texttosecondarytextpadding.md)
  The padding between the primary and secondary text.
### Type Methods
- [static func empty() -> UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct/empty.md)
  Creates the default configuration for unavailable content.
- [static func loading() -> UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct/loading.md)
  Creates the default configuration for content that’s loading.
- [static func search() -> UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct/search.md)
  Creates the default configuration for searches that return no results.
### Enumerations
- [UIContentUnavailableConfiguration.Alignment](uicontentunavailableconfiguration-swift.struct/alignment-swift.enum.md)
  Constants to define the alignment of views in a content-unavailable view.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [UIContentConfiguration](uicontentconfiguration-9eib5.md)

## See Also

- [struct UIContentUnavailableConfigurationState](uicontentunavailableconfigurationstate-swift.struct.md)
  A structure that encapsulates state for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-swift.struct)*