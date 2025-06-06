# subtitleLineBreakMode

**Framework**: UIKit  
**Kind**: property

The line break mode the button uses to lay out the button’s subtitle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var subtitleLineBreakMode: NSLineBreakMode { get set }
```

#### Discussion

Word and character wrapping modes enable multiline text, while other modes restrict the text to a single line.

The default value is [`NSLineBreakMode.byWordWrapping`](nslinebreakmode/bywordwrapping.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/subtitlelinebreakmode)*