# DropCapStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the drop cap text style to use in the first paragraph in a text component.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object DropCapStyle
```

## Mentions

- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)

## Discussion

Use a `DropCapStyle` object to define a drop cap that a [`ComponentTextStyle`](./componenttextstyle.md) object can use. You can apply drop caps to the first paragraph of the following components:

- [`Author`](./author.md)
- [`Body`](./body.md)
- [`Byline`](./byline.md)
- [`Caption`](./caption.md)
- [`Heading`](./heading.md)
- [`Illustrator`](./illustrator.md)
- [`Intro`](./intro.md)
- [`Photographer`](./photographer.md)
- [`PullQuote`](./pullquote.md)

> **Note**:  Using a divider between paragraphs splits text into separate components. This affects the rendering of `dropCapStyle`. If you want to include a divider between paragraphs and you don’t want the paragraph after the divider to have a drop cap, use separate text components for the block of text before and after the divider. Then make sure that you don’t have `dropCapStyle` in the text component following the divider.

You can use this object in [`TextStyle`](./textstyle.md) and [`ComponentTextStyle`](./componenttextstyle.md).

### Example

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 20,
      "dropCapStyle": {
        "numberOfLines": 5,
        "numberOfRaisedLines": 2,
        "numberOfCharacters": 1,
        "fontName": "HelveticaNeue",
        "textColor": "#FFF",
        "backgroundColor": "#000",
        "padding": 5
      }
    }
  }
}
```

## Properties

- `numberOfLines` (integer) *(required)*: The approximate number of text lines this drop cap spans. For example, if `numberOfLines` is set to `3`, and the top of the drop cap is aligned with the top of the first line, the bottom of the drop cap drops to the bottom of the third line, although the actual drop amount can vary depending on the device and its orientation.

  - Minimum: `2`
  - Maximum: `10`
- `backgroundColor` (Color): The background color of the drop cap. By default, no background color is applied, making the background effectively transparent.
- `fontName` (string): The PostScript name of the font to use for the drop cap. By default, the drop cap inherits the font of the component it’s in.
- `numberOfCharacters` (integer): A number that indicates the characters to render in the drop cap style.

  - Minimum: `1`
  - Maximum: `4`

  Default value`: 1`
- `numberOfRaisedLines` (integer): The number of text lines this drop cap raises. For example: When `numberOfRaisedLines` is `3`, and `numberOfLines` is `5`, the top of the drop cap raises above the first line by 3 lines and and the bottom of the drop cap drops to the bottom of the second line.
- `padding` (integer): A number that sets the padding of the drop cap in points. When padding is applied, the drop cap is smaller than the box that surrounds it.

  Default value: `0`
- `textColor` (Color): The color of the drop cap. The color defaults to the color of the associated text.

## See Also

### Text Styles
- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md)
  Choose a font family for Apple News Format that’s supported in iOS, iPadOS, and macOS.
- [object TextStyle](./textstyle.md)
  The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.
- [object ComponentTextStyle](./componenttextstyle.md)
  The object for defining the style for a text component, including spacing, alignment, and drop caps.
- [object ListItemStyle](./listitemstyle.md)
  The object for defining the style for bulleted or numbered lists in an article.
- [object InlineTextStyle](./inlinetextstyle.md)
  The object for applying text styling when not using HTML or Markdown formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/dropcapstyle)*