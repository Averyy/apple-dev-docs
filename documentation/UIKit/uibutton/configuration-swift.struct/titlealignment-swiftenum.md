# UIButton.Configuration.TitleAlignment

**Framework**: UIKit  
**Kind**: enum

Specifies how to align a button’s title and subtitle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
enum TitleAlignment
```

#### Overview

If your button displays both [`title`](uibutton/configuration-swift.struct/title.md) and [`subtitle`](uibutton/configuration-swift.struct/subtitle.md), use this enumeration to configure how the text aligns.

## Topics

### Title alignments
- [UIButton.Configuration.TitleAlignment.automatic](uibutton/configuration-swift.struct/titlealignment-swift.enum/automatic.md)
  Aligns the title and subtitle based on other elements in the button configuration, like an image or activity indicator.
- [UIButton.Configuration.TitleAlignment.center](uibutton/configuration-swift.struct/titlealignment-swift.enum/center.md)
  Aligns the title and subtitle on their horizontal centers.
- [UIButton.Configuration.TitleAlignment.leading](uibutton/configuration-swift.struct/titlealignment-swift.enum/leading.md)
  Aligns the title and subtitle on their leading edges.
- [UIButton.Configuration.TitleAlignment.trailing](uibutton/configuration-swift.struct/titlealignment-swift.enum/trailing.md)
  Aligns the title and subtitle on their trailing edges.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [var titleLineBreakMode: NSLineBreakMode](uibutton/configuration-swift.struct/titlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s title.
- [var subtitleLineBreakMode: NSLineBreakMode](uibutton/configuration-swift.struct/subtitlelinebreakmode.md)
  The line break mode the button uses to lay out the button’s subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/titlealignment-swift.enum)*