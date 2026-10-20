# UIButton.Configuration

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A configuration that specifies the appearance and behavior of a button and its contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
struct Configuration
```

#### Overview

You can configure and update a button with a [`UIButton.Configuration`](./configuration-swift.struct.md). A button configuration contains all the customization options available with other methods, such as [`setTitle(_:for:)`](./settitle%28_,for%29.md), and can serve as a replacement for those methods. Alternatively, you can use a configuration in combination with these other methods and adopt new button behaviors and appearance without rewriting your customized [`UIButton`](../uibutton.md) code.

## Topics

### Creating configurations
- [static func plain() -> UIButton.Configuration](./configuration-swift.struct/plain%28%29.md)
  Creates a configuration for a button with a transparent background.
- [static func gray() -> UIButton.Configuration](./configuration-swift.struct/gray%28%29.md)
  Creates a configuration for a button with a gray background.
- [static func tinted() -> UIButton.Configuration](./configuration-swift.struct/tinted%28%29.md)
  Creates a configuration for a button with a tinted background color.
- [static func filled() -> UIButton.Configuration](./configuration-swift.struct/filled%28%29.md)
  Creates a configuration for a button with a background filled with the button’s tint color.
- [static func borderless() -> UIButton.Configuration](./configuration-swift.struct/borderless%28%29.md)
  Creates a configuration for a button that has a borderless style.
- [static func bordered() -> UIButton.Configuration](./configuration-swift.struct/bordered%28%29.md)
  Creates a configuration for a button that has a bordered style.
- [static func borderedTinted() -> UIButton.Configuration](./configuration-swift.struct/borderedtinted%28%29.md)
  Creates a configuration for a button that has a tinted, bordered style.
- [static func borderedProminent() -> UIButton.Configuration](./configuration-swift.struct/borderedprominent%28%29.md)
  Creates a configuration for a button that has a prominent, bordered style.
- [static func glass() -> UIButton.Configuration](./configuration-swift.struct/glass%28%29.md)
  Creates a configuration for a button that has a Liquid Glass style.
- [static func prominentGlass() -> UIButton.Configuration](./configuration-swift.struct/prominentglass%28%29.md)
  Creates a configuration for a button that has a prominent Liquid Glass style.
- [static func clearGlass() -> UIButton.Configuration](./configuration-swift.struct/clearglass%28%29.md)
  Creates a configuration for a button that has a clear Liquid Glass style.
- [static func prominentClearGlass() -> UIButton.Configuration](./configuration-swift.struct/prominentclearglass%28%29.md)
  Creates a configuration for a button that has a prominent, clear Liquid Glass style.
- [func updated(for: UIButton) -> UIButton.Configuration](./configuration-swift.struct/updated%28for%29.md)
  Returns a copy of the configuration, updated for the given button.
### Configuring titles
- [var title: String?](./configuration-swift.struct/title.md)
  The text of the title label the button displays.
- [var subtitle: String?](./configuration-swift.struct/subtitle.md)
  The text the subtitle label of the button displays.
- [var attributedTitle: AttributedString?](./configuration-swift.struct/attributedtitle.md)
  The text and style attributes for the button’s title label.
- [var attributedSubtitle: AttributedString?](./configuration-swift.struct/attributedsubtitle.md)
  The text and style attributes for the button’s subtitle label.
- [var titleTextAttributesTransformer: UIConfigurationTextAttributesTransformer?](./configuration-swift.struct/titletextattributestransformer.md)
  A structure to update the attributed title when the button state changes.
- [var subtitleTextAttributesTransformer: UIConfigurationTextAttributesTransformer?](./configuration-swift.struct/subtitletextattributestransformer.md)
  A structure to update the attributed subtitle when the button state changes.
- [struct UIConfigurationTextAttributesTransformer](../uiconfigurationtextattributestransformer-swift.struct.md)
  Defines a text transformation that can affect the visual appearance of a string.
- [var titlePadding: CGFloat](./configuration-swift.struct/titlepadding.md)
  The distance between the title and subtitle labels.
- [var titleAlignment: UIButton.Configuration.TitleAlignment](./configuration-swift.struct/titlealignment-swift.property.md)
  The text alignment the button uses to lay out the title and subtitle.
- [UIButton.Configuration.TitleAlignment](./configuration-swift.struct/titlealignment-swift.enum.md)
  Specifies how to align a button’s title and subtitle.
- [var titleLineBreakMode: NSLineBreakMode](./configuration-swift.struct/titlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s title.
- [var subtitleLineBreakMode: NSLineBreakMode](./configuration-swift.struct/subtitlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s subtitle.
### Configuring images
- [var image: UIImage?](./configuration-swift.struct/image.md)
  The foreground image the button displays.
- [var imagePadding: CGFloat](./configuration-swift.struct/imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](./configuration-swift.struct/imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](./configuration-swift.struct/imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](./configuration-swift.struct/imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](./configuration-swift.struct/preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.
### Configuring layout
- [var buttonSize: UIButton.Configuration.Size](./configuration-swift.struct/buttonsize.md)
  A size that requests a preferred size for the button.
- [UIButton.Configuration.Size](./configuration-swift.struct/size.md)
  A predefined size for button elements.
- [var contentInsets: NSDirectionalEdgeInsets](./configuration-swift.struct/contentinsets.md)
  The distance from the button’s content area to its bounds.
- [func setDefaultContentInsets()](./configuration-swift.struct/setdefaultcontentinsets%28%29.md)
  Restores the default content insets.
### Configuring button colors
- [var baseBackgroundColor: UIColor?](./configuration-swift.struct/basebackgroundcolor.md)
  The untransformed color for background views.
- [var baseForegroundColor: UIColor?](./configuration-swift.struct/baseforegroundcolor.md)
  The untransformed color for foreground views.
### Configuring the button background
- [var background: UIBackgroundConfiguration](./configuration-swift.struct/background.md)
  The configuration to customize the button background.
- [var cornerStyle: UIButton.Configuration.CornerStyle](./configuration-swift.struct/cornerstyle-swift.property.md)
  The button style that controls the display behavior of the background corner radius.
- [UIButton.Configuration.CornerStyle](./configuration-swift.struct/cornerstyle-swift.enum.md)
  Settings that determine the appearance of the background corner radius.
### Configuring the indicator
- [var indicator: UIButton.Configuration.Indicator](./configuration-swift.struct/indicator-swift.property.md)
  The style of the indicator that appears on the button.
- [UIButton.Configuration.Indicator](./configuration-swift.struct/indicator-swift.enum.md)
  Constants that determine the style of the indicator that appears on a button.
- [var indicatorColorTransformer: UIConfigurationColorTransformer?](./configuration-swift.struct/indicatorcolortransformer.md)
  The color transformer for resolving the indicator color.
### Configuring the activity indicator
- [var showsActivityIndicator: Bool](./configuration-swift.struct/showsactivityindicator.md)
  A Boolean value that determines whether the button displays an activity indicator instead of an image.
- [var activityIndicatorColorTransformer: UIConfigurationColorTransformer?](./configuration-swift.struct/activityindicatorcolortransformer.md)
  The color transformer for resolving the color of the activity indicator.
### Configuring selection behavior
- [var automaticallyUpdateForSelection: Bool](./configuration-swift.struct/automaticallyupdateforselection.md)
  A Boolean value that determines whether the style automatically updates when the button is in a selected state.
### Configuring the appearance on macOS
- [var macIdiomStyle: UIButton.Configuration.MacIdiomStyle](./configuration-swift.struct/macidiomstyle-swift.property.md)
  The style to use when this button appears in macOS.
- [UIButton.Configuration.MacIdiomStyle](./configuration-swift.struct/macidiomstyle-swift.enum.md)
  The button style your app uses when running in macOS.
### Instance Properties
- [var symbolContentTransition: UISymbolContentTransition?](./configuration-swift.struct/symbolcontenttransition.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Creating buttons from a configuration object
- [convenience init(configuration: UIButton.Configuration, primaryAction: UIAction?)](./init%28configuration,primaryaction%29.md)
  Creates a new button with the specified configuration and registers the primary action event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct)*