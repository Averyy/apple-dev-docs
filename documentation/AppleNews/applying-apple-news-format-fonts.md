# Applying Apple News Format Fonts

**Framework**: Apple News

Choose a font family for Apple News Format that’s supported in iOS, iPadOS, and macOS.

#### Overview

Fonts determine the look of text in your article. Within font families, the properties `fontWeight`, `fontWidth`, and `fontStyle` provide variations on the font for bolder or lighter, condensed or expanded, and regular or italicized text. To specify a font variant in Apple News Format, you can also use an explicit font variant’s PostScript name (listed in parentheses) in a `fontName` property without style modifiers (see [`TextStyle`](https://developer.apple.com/documentation/applenewsformat/textstyle)). For information about using fonts in Apple News Format, see [`Defining and Applying Text Styles`](defining-and-applying-text-styles.md).

##### Choose a Font Family

The following table lists font families for Apple News Format that are supported in iOS, iPadOS, and macOS.

> ❗ **Important**:  Some font families may not support all unicode values.

| **Font family name** | **Variants** |
| --- | --- |
| Academy Engraved LET | fontWeight: regular (AcademyEngravedLetPlain) |
| Al Nile | fontWeight: regular (AlNile) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (AlNile-Bold) |
| American Typewriter | fontWeight: regular (AmericanTypewriter) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (AmericanTypewriter-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (AmericanTypewriter-Semibold) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed (AmericanTypewriter-Condensed) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed; fontWeight: bold (AmericanTypewriter-CondensedBold) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed; fontWeight: light (AmericanTypewriter-CondensedLight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (AmericanTypewriter-Light) |
| Apple Color Emoji | fontWeight: regular (AppleColorEmoji) |
| Apple SD Gothic Neo | fontWeight: ultra-light (AppleSDGothicNeo-UltraLight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (AppleSDGothicNeo-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (AppleSDGothicNeo-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (AppleSDGothicNeo-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (AppleSDGothicNeo-SemiBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (AppleSDGothicNeo-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: extra-bold (AppleSDGothicNeo-ExtraBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy (AppleSDGothicNeo-Heavy) ![None](/images/com.apple.applenews/spacer.png) fontWeight: thin (AppleSDGothicNeo-Thin) |
| Arial | fontWeight: regular (ArialMT) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic;  (Arial-BoldItalicMT) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Arial-BoldMT) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Arial-ItalicMT) |
| Arial Hebrew | fontWeight: regular (ArialHebrew) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (ArialHebrew-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (ArialHebrew-Light) |
| Arial Rounded MT Bold | fontWeight: regular (ArialRoundedMTBold) |
| Avenir | fontWeight: black (Avenir-Black) ![None](/images/com.apple.applenews/spacer.png) fontWeight: black; fontStyle: oblique (Avenir-BlackOblique) ![None](/images/com.apple.applenews/spacer.png) fontWeight: Book; (Avenir-Book) ![None](/images/com.apple.applenews/spacer.png) fontWeight: book; fontStyle: oblique (Avenir-BookOblique) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy (Avenir-Heavy) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy; fontStyle: oblique (Avenir-HeavyOblique) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (Avenir-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light; fontStyle: oblique (Avenir-LightOblique) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (Avenir-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium; fontStyle: oblique (Avenir-MediumOblique) ![None](/images/com.apple.applenews/spacer.png) fontStyle: oblique (Avenir-Oblique) ![None](/images/com.apple.applenews/spacer.png) fontWeight: roman (Avenir-Roman) |
| Avenir Next | fontWeight: bold (AvenirNext-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (AvenirNext-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: demi-bold (AvenirNext-DemiBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: demi-bold; fontStyle: italic (AvenirNext-DemiBoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy (AvenirNext-Heavy) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy; fontStyle: italic (AvenirNext-HeavyItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (AvenirNext-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (AvenirNext-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium; fontStyle: italic (AvenirNext-MediumItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (AvenirNext-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-light (AvenirNext-UltraLight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-light; fontStyle: italic (AvenirNext-UltraLightItalic) |
| Avenir Next Condensed | fontWeight: bold (AvenirNextCondensed-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (AvenirNextCondensed-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: demi-bold (AvenirNextCondensed-DemiBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: demi-bold; fontStyle: italic (AvenirNextCondensed-DemiBoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy (AvenirNextCondensed-Heavy) ![None](/images/com.apple.applenews/spacer.png) fontWeight: heavy; fontStyle: italic (AvenirNextCondensed-HeavyItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (AvenirNextCondensed-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (AvenirNextCondensed-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium; fontStyle: italic (AvenirNextCondensed-MediumItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (AvenirNextCondensed-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-light (AvenirNextCondensed-UltraLight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-light; fontStyle: italic (AvenirNextCondensed-UltraLightItalic) |
| Baskerville | fontWeight: regular (Baskerville) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Baskerville-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (Baskerville-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Baskerville-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (Baskerville-SemiBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold; fontStyle: italic (Baskerville-SemiBoldItalic) |
| Bodoni 72 | fontWeight: bold (BodoniSvtyTwoITCTT-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: book (BodoniSvtyTwoITCTT-Book) ![None](/images/com.apple.applenews/spacer.png) fontWeight: book; fontStyle: italic (BodoniSvtyTwoITCTT-BookIta) |
| Bodoni 72 Oldstyle | fontWeight: bold (BodoniSvtyTwoOSITCTT-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: book (BodoniSvtyTwoOSITCTT-Book) ![None](/images/com.apple.applenews/spacer.png) fontWeight: book; fontStyle: italic (BodoniSvtyTwoOSITCTT-BookIt) |
| Bodoni 72 Smallcaps | fontWeight: book (BodoniSvtyTwoSCITCTT-Book) |
| Bradley Hand | fontWeight: bold (BradleyHandITCTT-Bold) |
| Chalkboard SE | fontWeight: bold (ChalkboardSE-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (ChalkboardSE-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (ChalkboardSE-Regular) |
| Cochin | fontWeight: regular (Cochin) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Cochin-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (Cochin-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Cochin-Italic) |
| Copperplate | fontWeight: regular (Copperplate) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Copperplate-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (Copperplate-Light) |
| Courier | fontWeight: regular (Courier) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Courier-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: oblique (Courier-BoldOblique) ![None](/images/com.apple.applenews/spacer.png) fontStyle: oblique (Courier-Oblique) |
| Courier New | fontWeight: bold; fontStyle: italic (CourierNewPS-BoldItalicMT) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (CourierNewPS-BoldMT) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (CourierNewPS-ItalicMT) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (CourierNewPSMT) |
| DIN Alternate | fontWeight: bold (DINAlternate-Bold) |
| DIN Condensed | fontWeight: bold (DINCondensed-Bold) |
| Didot | fontWeight: regular (Didot) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Didot-Bold) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Didot-Italic) |
| Euphemia UCAS | fontWeight: regular (EuphemiaUCAS) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (EuphemiaUCAS-Bold) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (EuphemiaUCAS-Italic) |
| Farah | fontWeight: regular (Farah) |
| Futura | fontWidth: condensed; fontWeight: extra bold (Futura-CondensedExtraBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Futura-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed; fontWeight: medium (Futura-CondensedMedium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (Futura-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium; fontStyle: italic (Futura-MediumItalic) |
| Georgia | fontWeight: regular (Georgia) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Georgia-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (Georgia-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Georgia-Italic) |
| Gill Sans | fontWeight: regular (GillSans) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (GillSans-SemiBold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold; fontStyle: italic (GillSans-SemiBoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (GillSans-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (GillSans-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-bold (GillSans-UltraBold) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (GillSans-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (GillSans-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light; fontStyle: italic (GillSans-LightItalic) |
| Heiti SC | fontWeight: light (STHeitiSC-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (STHeitiSC-Medium) |
| Heiti TC | fontWeight: light (STHeitiTC-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (STHeitiTC-Medium) |
| Helvetica | fontWeight: regular (Helvetica) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Helvetica-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: oblique (Helvetica-BoldOblique) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (Helvetica-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light; fontStyle: oblique (Helvetica-LightOblique) ![None](/images/com.apple.applenews/spacer.png) fontStyle: oblique (Helvetica-Oblique) |
| Helvetica Neue | fontWeight: regular (HelveticaNeue) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (HelveticaNeue-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (HelveticaNeue-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed; fontWeight: black (HelveticaNeue-CondensedBlack) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed; fontWeight: bold (HelveticaNeue-CondensedBold) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (HelveticaNeue-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (HelveticaNeue-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light; fontStyle: italic (HelveticaNeue-LightItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (HelveticaNeue-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium; fontStyle: italic (HelveticaNeue-MediumItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-light (HelveticaNeue-UltraLight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ultra-light; fontStyle: italic (HelveticaNeue-UltraLightItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: thin (HelveticaNeue-Thin) ![None](/images/com.apple.applenews/spacer.png) fontWeight: thin; fontStyle: italic (HelveticaNeue-ThinItalic) |
| Hiragino Mincho ProN | fontWeight: regular (HiraMinProN-W3) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (HiraMinProN-W6) |
| Hiragino Sans | fontWeight: regular (HiraginoSans-W3) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (HiraginoSans-W6) |
| Hoefler Text | fontWeight: black (HoeflerText-Black) ![None](/images/com.apple.applenews/spacer.png) fontWeight: black; fontStyle: italic (HoeflerText-BlackItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (HoeflerText-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (HoeflerText-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: ornaments (HoeflerText-Ornaments) |
| Marker Felt | fontWeight: thin (MarkerFelt-Thin) ![None](/images/com.apple.applenews/spacer.png) fontWeight: wide (MarkerFelt-Wide) |
| Menlo | fontWeight: bold; fontStyle: italic (Menlo-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (Menlo-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Menlo-Bold) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Menlo-Italic) |
| Noteworthy | fontWeight: bold (Noteworthy-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (Noteworthy-Light) |
| Optima | fontWeight: bold (Optima-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (Optima-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight:  extra black (Optima-ExtraBlack) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Optima-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (Optima-Regular) |
| Palatino | fontWeight: bold (Palatino-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (Palatino-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Palatino-Italic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: roman (Palatino-Roman) |
| Papyrus | fontWeight: regular (Papyrus) ![None](/images/com.apple.applenews/spacer.png) fontWidth: condensed (Papyrus-Condensed) |
| Party LET | fontWeight: regular (PartyLetPlain) |
| PingFang HK | fontWeight: ultra-light (PingFangHK-Ultralight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (PingFangHK-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: thin (PingFangHK-Thin) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (PingFangHK-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (PingFangHK-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (PingFangHK-Semibold) |
| PingFang SC | fontWeight: ultra-light (PingFangSC-Ultralight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (PingFangSC-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: thin (PingFangSC-Thin) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (PingFangSC-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (PingFangSC-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (PingFangSC-Semibold) |
| PingFang TC | fontWeight: ultra-light (PingFangTC-Ultralight) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (PingFangTC-Light) ![None](/images/com.apple.applenews/spacer.png) fontWeight: thin (PingFangTC-Thin) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (PingFangTC-Regular) ![None](/images/com.apple.applenews/spacer.png) fontWeight: medium (PingFangTC-Medium) ![None](/images/com.apple.applenews/spacer.png) fontWeight: semi-bold (PingFangTC-Semibold) |
| Savoye Let | fontWeight: regular (SavoyeLetPlain) |
| Snell Roundhand | fontWeight: regular (SnellRoundhand) ![None](/images/com.apple.applenews/spacer.png) fontWeight: black (SnellRoundhand-Black) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (SnellRoundhand-Bold) |
| Thonburi | fontWeight: regular (Thonburi) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Thonburi-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: light (Thonburi-Light) |
| Times New Roman | fontWeight: bold; fontStyle: italic (TimesNewRomanPS-BoldItalicMT) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (TimesNewRomanPS-BoldMT) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (TimesNewRomanPS-ItalicMT) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (TimesNewRomanPSMT) |
| Trebuchet MS | fontWeight: bold; fontStyle: italic (Trebuchet-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontWeight: regular (TrebuchetMS) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (TrebuchetMS-Bold) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (TrebuchetMS-Italic) |
| Verdana | fontWeight: regular (Verdana) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold (Verdana-Bold) ![None](/images/com.apple.applenews/spacer.png) fontWeight: bold; fontStyle: italic (Verdana-BoldItalic) ![None](/images/com.apple.applenews/spacer.png) fontStyle: italic (Verdana-Italic) |
| Zapf Dingbats | fontWeight: regular (ZapfDingbatsITC) |
| Zapfino | fontWeight: regular (Zapfino) |

##### Apply the Fonts to Your Article

The following example code shows how to apply the Arial font family to your article.

```json
{
  "sample": {
    "textStyles": {
      "default-tag-abbr": {
        "fontFamily": "Arial",
        "fontWeight": "bold",
        "fontStyle": "italic"
      },
      "default-tag-title": {
        "fontName": "Arial-BoldItalicMT",
      }
    },
    "components": [
      {
        "role": "body",
        "format": "html",
        "text": "<p>The <abbr>UFO</abbr> is an <title>Unidentified Flying Object</title>.</p>"
      }
    ]
  }
}
```

## See Also

- [Defining and Applying Text Styles](defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [object TextStyle](../applenewsformat/textstyle.md)
  The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.
- [object ComponentTextStyle](../applenewsformat/componenttextstyle.md)
  The object for defining the style for a text component, including spacing, alignment, and drop caps.
- [object DropCapStyle](../applenewsformat/dropcapstyle.md)
  The object for defining the drop cap text style to use in the first paragraph in a text component.
- [object ListItemStyle](../applenewsformat/listitemstyle.md)
  The object for defining the style for bulleted or numbered lists in an article.
- [object InlineTextStyle](../applenewsformat/inlinetextstyle.md)
  The object for applying text styling when not using HTML or Markdown formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/applying-apple-news-format-fonts)*