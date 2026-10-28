# title

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text of the title label the button displays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var title: String? { get set }
```

## Discussion

This property matches the string value of the [`attributedTitle`](./attributedtitle.md) property. To change the button title when the button state changes, use [`configurationUpdateHandler`](../configurationupdatehandler-swift.property.md) or [`updateConfiguration()`](../updateconfiguration%28%29.md).

## See Also

### Configuring titles
- [var subtitle: String?](./subtitle.md)
  The text the subtitle label of the button displays.
- [var attributedTitle: AttributedString?](./attributedtitle.md)
  The text and style attributes for the button’s title label.
- [var attributedSubtitle: AttributedString?](./attributedsubtitle.md)
  The text and style attributes for the button’s subtitle label.
- [var titleTextAttributesTransformer: UIConfigurationTextAttributesTransformer?](./titletextattributestransformer.md)
  A structure to update the attributed title when the button state changes.
- [var subtitleTextAttributesTransformer: UIConfigurationTextAttributesTransformer?](./subtitletextattributestransformer.md)
  A structure to update the attributed subtitle when the button state changes.
- [struct UIConfigurationTextAttributesTransformer](../../uiconfigurationtextattributestransformer-swift.struct.md)
  Defines a text transformation that can affect the visual appearance of a string.
- [var titlePadding: CGFloat](./titlepadding.md)
  The distance between the title and subtitle labels.
- [var titleAlignment: UIButton.Configuration.TitleAlignment](./titlealignment-swift.property.md)
  The text alignment the button uses to lay out the title and subtitle.
- [UIButton.Configuration.TitleAlignment](./titlealignment-swift.enum.md)
  Specifies how to align a button’s title and subtitle.
- [var titleLineBreakMode: NSLineBreakMode](./titlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s title.
- [var subtitleLineBreakMode: NSLineBreakMode](./subtitlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/title)*