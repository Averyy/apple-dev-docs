# attributedSubtitle

**Framework**: UIKit  
**Kind**: property

The text and style attributes for the button’s subtitle label.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var attributedSubtitle: AttributedString? { get set }
```

#### Discussion

The configuration sets the [`subtitle`](uibutton/configuration-swift.struct/subtitle.md) property to match the string value of this attributed string. To change the button subtitle when the button state changes, use [`configurationUpdateHandler`](uibutton/configurationupdatehandler-swift.property.md) or [`updateConfiguration()`](uibutton/updateconfiguration().md).

## See Also

- [var title: String?](uibutton/configuration-swift.struct/title.md)
  The text of the title label the button displays.
- [var subtitle: String?](uibutton/configuration-swift.struct/subtitle.md)
  The text the subtitle label of the button displays.
- [var attributedTitle: AttributedString?](uibutton/configuration-swift.struct/attributedtitle.md)
  The text and style attributes for the button’s title label.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/attributedsubtitle)*