# InlineTextStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for applying text styling when not using HTML or Markdown formatting.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object InlineTextStyle
```

## Mentions

- [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md)
- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)

## Discussion

Use an `InlineTextStyle` object to apply text stylings (such as color, underline, font size, and font weight) to a specific range of text. The `InlineTextStyle` object contains either a [`TextStyle`](./textstyle.md) object or a reference to a text style that’s been defined in the [`ArticleDocument.textStyles`](./articledocument/textstyles-data.dictionary.md) object. Only properties that have values override the component text style and defaults.

You can use this object in [`Text`](./text.md).

### Example

```json
{
  "components": [
    {
      "role": "pullquote",
      "text": "The text of the pullquote.",
      "textStyle": "pullquote-medium",
      "inlineTextStyles": [
        {
          "rangeStart": 4,
          "rangeLength": 4,
          "textStyle": {
            "textColor": "#FF0000",
            "backgroundColor": "#000"
          }
        }
      ]
    }
  ]
}
```

## Properties

- `rangeLength` (integer) *(required)*: The length (in characters) of the portion of text to which Apple News applies alternative styling.
- `rangeStart` (integer) *(required)*: The starting point of the text to which Apple News applies alternative styling. Note: the first available character is at `0`, not `1`.
- `textStyle` ((TextStyle | string)) *(required)*: Either a text style object or the name of a [`TextStyle`](./textstyle.md) object defined in the [`ArticleDocument.textStyles`](./articledocument/textstyles-data.dictionary.md) object.

  **Allowed Types**: `TextStyle`, `string`

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
- [object DropCapStyle](./dropcapstyle.md)
  The object for defining the drop cap text style to use in the first paragraph in a text component.
- [object ListItemStyle](./listitemstyle.md)
  The object for defining the style for bulleted or numbered lists in an article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/inlinetextstyle)*