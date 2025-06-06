# CMTextMarkup

**Framework**: Core Media

Attributes that specify text markup in legible media.

#### Overview

Core Media supports legible media streams like subtitles and closed captions. In some cases, apps may need to specify style information to control rendering. In other cases, the framework indicates the text and styling to apply.

## Topics

### Fonts
- [let kCMTextMarkupAttribute_FontFamilyName: CFString](kcmtextmarkupattribute_fontfamilyname.md)
  A name of a font family.
- [let kCMTextMarkupAttribute_GenericFontFamilyName: CFString](kcmtextmarkupattribute_genericfontfamilyname.md)
  A generic font family name identifier.
- [let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString](kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight.md)
  A base font size as a percentage of the video height.
- [let kCMTextMarkupAttribute_RelativeFontSize: CFString](kcmtextmarkupattribute_relativefontsize.md)
  A font size as a percentage of the current default font size.
### Styles
- [let kCMTextMarkupAttribute_BoldStyle: CFString](kcmtextmarkupattribute_boldstyle.md)
  A bold font style.
- [let kCMTextMarkupAttribute_ItalicStyle: CFString](kcmtextmarkupattribute_italicstyle.md)
  An italic font style.
- [let kCMTextMarkupAttribute_UnderlineStyle: CFString](kcmtextmarkupattribute_underlinestyle.md)
  An underline font style.
- [let kCMTextMarkupAttribute_CharacterEdgeStyle: CFString](kcmtextmarkupattribute_characteredgestyle.md)
  A style for character edges.
### Colors
- [let kCMTextMarkupAttribute_ForegroundColorARGB: CFString](kcmtextmarkupattribute_foregroundcolorargb.md)
  A foreground color for the text.
- [let kCMTextMarkupAttribute_BackgroundColorARGB: CFString](kcmtextmarkupattribute_backgroundcolorargb.md)
  A background color for the text.
- [let kCMTextMarkupAttribute_CharacterBackgroundColorARGB: CFString](kcmtextmarkupattribute_characterbackgroundcolorargb.md)
  A background color for individual text characters.
### Layout
- [let kCMTextMarkupAttribute_VerticalLayout: CFString](kcmtextmarkupattribute_verticallayout.md)
  The vertical layout of a text block.
- [let kCMTextMarkupAttribute_Alignment: CFString](kcmtextmarkupattribute_alignment.md)
  The text alignment in the writing direction of the first line of text.
- [let kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection.md)
  The placement of the block of text as a percentage in the writing direction.
- [let kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection.md)
  The placement of the first line in a block of text as a percentage in the direction orthogonal to the writing direction.
- [let kCMTextMarkupAttribute_WritingDirectionSizePercentage: CFString](kcmtextmarkupattribute_writingdirectionsizepercentage.md)
  The width or height as a percentage of the bounding box that contains the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtextmarkup)*