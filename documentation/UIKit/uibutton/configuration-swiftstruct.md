# UIButton.Configuration

**Framework**: UIKit  
**Kind**: struct

A configuration that specifies the appearance and behavior of a button and its contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
struct Configuration
```

#### Overview

You can configure and update a button with a [`UIButton.Configuration`](uibutton/configuration-swift.struct.md). A button configuration contains all the customization options available with other methods, such as [`setTitle(_:for:)`](uibutton/settitle(_:for:).md), and can serve as a replacement for those methods. Alternatively, you can use a configuration in combination with these other methods and adopt new button behaviors and appearance without rewriting your customized [`UIButton`](uibutton.md) code.

## Topics

### Creating configurations
- [static func plain() -> UIButton.Configuration](uibutton/configuration-swift.struct/plain.md)
  Creates a configuration for a button with a transparent background.
- [static func gray() -> UIButton.Configuration](uibutton/configuration-swift.struct/gray.md)
  Creates a configuration for a button with a gray background.
- [static func tinted() -> UIButton.Configuration](uibutton/configuration-swift.struct/tinted.md)
  Creates a configuration for a button with a tinted background color.
- [static func filled() -> UIButton.Configuration](uibutton/configuration-swift.struct/filled.md)
  Creates a configuration for a button with a background filled with the button’s tint color.
- [static func borderless() -> UIButton.Configuration](uibutton/configuration-swift.struct/borderless.md)
  Creates a configuration for a button that has a borderless style.
- [static func bordered() -> UIButton.Configuration](uibutton/configuration-swift.struct/bordered.md)
  Creates a configuration for a button that has a bordered style.
- [static func borderedTinted() -> UIButton.Configuration](uibutton/configuration-swift.struct/borderedtinted.md)
  Creates a configuration for a button that has a tinted, bordered style.
- [static func borderedProminent() -> UIButton.Configuration](uibutton/configuration-swift.struct/borderedprominent.md)
  Creates a configuration for a button that has a prominent, bordered style.
- [static func glass() -> UIButton.Configuration](uibutton/configuration-swift.struct/glass.md)
  Creates a configuration for a button that has a Liquid Glass style.
- [static func prominentGlass() -> UIButton.Configuration](uibutton/configuration-swift.struct/prominentglass.md)
  Creates a configuration for a button that has a prominent Liquid Glass style.
- [static func clearGlass() -> UIButton.Configuration](uibutton/configuration-swift.struct/clearglass.md)
  Creates a configuration for a button that has a clear Liquid Glass style.
- [static func prominentClearGlass() -> UIButton.Configuration](uibutton/configuration-swift.struct/prominentclearglass.md)
  Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [func updated(for: UIButton) -> UIButton.Configuration](uibutton/configuration-swift.struct/updated(for:).md)
  Returns a copy of the configuration, updated for the given button.
### Configuring titles
- [var title: String?](uibutton/configuration-swift.struct/title.md)
  The text of the title label the button displays.
- [var subtitle: String?](uibutton/configuration-swift.struct/subtitle.md)
  The text the subtitle label of the button displays.
- [var attributedTitle: AttributedString?](uibutton/configuration-swift.struct/attributedtitle.md)
  The text and style attributes for the button’s title label.
- [var attributedSubtitle: AttributedString?](uibutton/configuration-swift.struct/attributedsubtitle.md)
  The text and style attributes for the button’s subtitle label.
- [var titleTextAttributesTransformer: UIConfigurationTextAttributesTransformer?](uibutton/configuration-swift.struct/titletextattributestransformer.md)
  A structure to update the attributed title when the button state changes.
- [var subtitleTextAttributesTransformer: UIConfigurationTextAttributesTransformer?](uibutton/configuration-swift.struct/subtitletextattributestransformer.md)
  A structure to update the attributed subtitle when the button state changes.
- [struct UIConfigurationTextAttributesTransformer](uiconfigurationtextattributestransformer-swift.struct.md)
  Defines a text transformation that can affect the visual appearance of a string.
- [var titlePadding: CGFloat](uibutton/configuration-swift.struct/titlepadding.md)
  The distance between the title and subtitle labels.
- [var titleAlignment: UIButton.Configuration.TitleAlignment](uibutton/configuration-swift.struct/titlealignment-swift.property.md)
  The text alignment the button uses to lay out the title and subtitle.
- [UIButton.Configuration.TitleAlignment](uibutton/configuration-swift.struct/titlealignment-swift.enum.md)
  Specifies how to align a button’s title and subtitle.
- [var titleLineBreakMode: NSLineBreakMode](uibutton/configuration-swift.struct/titlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s title.
- [var subtitleLineBreakMode: NSLineBreakMode](uibutton/configuration-swift.struct/subtitlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s subtitle.
### Configuring images
- [var image: UIImage?](uibutton/configuration-swift.struct/image.md)
  The foreground image the button displays.
- [var imagePadding: CGFloat](uibutton/configuration-swift.struct/imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](uibutton/configuration-swift.struct/imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](uibutton/configuration-swift.struct/imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](uibutton/configuration-swift.struct/preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.
### Configuring layout
- [var buttonSize: UIButton.Configuration.Size](uibutton/configuration-swift.struct/buttonsize.md)
  A size that requests a preferred size for the button.
- [UIButton.Configuration.Size](uibutton/configuration-swift.struct/size.md)
  A predefined size for button elements.
- [var contentInsets: NSDirectionalEdgeInsets](uibutton/configuration-swift.struct/contentinsets.md)
  The distance from the button’s content area to its bounds.
- [func setDefaultContentInsets()](uibutton/configuration-swift.struct/setdefaultcontentinsets.md)
  Restores the default content insets.
### Configuring button colors
- [var baseBackgroundColor: UIColor?](uibutton/configuration-swift.struct/basebackgroundcolor.md)
  The untransformed color for background views.
- [var baseForegroundColor: UIColor?](uibutton/configuration-swift.struct/baseforegroundcolor.md)
  The untransformed color for foreground views.
### Configuring the button background
- [var background: UIBackgroundConfiguration](uibutton/configuration-swift.struct/background.md)
  The configuration to customize the button background.
- [var cornerStyle: UIButton.Configuration.CornerStyle](uibutton/configuration-swift.struct/cornerstyle-swift.property.md)
  The button style that controls the display behavior of the background corner radius.
- [UIButton.Configuration.CornerStyle](uibutton/configuration-swift.struct/cornerstyle-swift.enum.md)
  Settings that determine the appearance of the background corner radius.
### Configuring the indicator
- [var indicator: UIButton.Configuration.Indicator](uibutton/configuration-swift.struct/indicator-swift.property.md)
  The style of the indicator that appears on the button.
- [UIButton.Configuration.Indicator](uibutton/configuration-swift.struct/indicator-swift.enum.md)
  Constants that determine the style of the indicator that appears on a button.
- [var indicatorColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/indicatorcolortransformer.md)
  The color transformer for resolving the indicator color.
### Configuring the activity indicator
- [var showsActivityIndicator: Bool](uibutton/configuration-swift.struct/showsactivityindicator.md)
  A Boolean value that determines whether the button displays an activity indicator instead of an image.
- [var activityIndicatorColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/activityindicatorcolortransformer.md)
  The color transformer for resolving the color of the activity indicator.
### Configuring selection behavior
- [var automaticallyUpdateForSelection: Bool](uibutton/configuration-swift.struct/automaticallyupdateforselection.md)
  A Boolean value that determines whether the style automatically updates when the button is in a selected state.
### Configuring the appearance on macOS
- [var macIdiomStyle: UIButton.Configuration.MacIdiomStyle](uibutton/configuration-swift.struct/macidiomstyle-swift.property.md)
  The style to use when this button appears in macOS.
- [UIButton.Configuration.MacIdiomStyle](uibutton/configuration-swift.struct/macidiomstyle-swift.enum.md)
  The button style your app uses when running in macOS.
### Instance Properties
- [var symbolContentTransition: UISymbolContentTransition?](uibutton/configuration-swift.struct/symbolcontenttransition.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [convenience init(configuration: UIButton.Configuration, primaryAction: UIAction?)](uibutton/init(configuration:primaryaction:).md)
  Creates a new button with the specified configuration and registers the primary action event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct)*