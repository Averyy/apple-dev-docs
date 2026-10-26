# ListItemStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the style for bulleted or numbered lists in an article.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ListItemStyle
```

#### Discussion

Use the `ListItemStyle` object to define text formatting for a bulleted (unordered) or numbered (ordered) list. Put `listItemStyle` inside a [`TextStyle`](./textstyle.md) object or [`ComponentTextStyle`](./componenttextstyle.md) object and set the text component’s `format` property to `html`. See [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md).

You can use this object in [`TextStyle`](./textstyle.md) and [`ComponentTextStyle`](./componenttextstyle.md).

##### Example

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      …
      "unorderedListItems": {
        "type": "character",
        "character": "✓"
      }
    }
  }
}
```

## Properties

- `type` (string) *(required)*: The type of list item indicator to use.

  Allowed options are:

  - `bullet`: Prepends a bullet before each list item. This is the default for unordered lists.
  - `decimal`: Prepends each list item with an incremental number. This is the default for ordered lists.
  - `lower_alphabetical`: Prepends list items with a lowercase letter.
  - `upper_alphabetical`: Prepends list items with an uppercase letter.
  - `lower_roman`: Prepends list items with a lowercase Roman numeral.
  - `upper_roman`: Prepends list items with an uppercase Roman numeral.
  - `character`: Prepends list items with a custom character. Use the `character` property to specify a character.
  - `none`: Doesn’t prepend any indicator for list items. Indenting is still in effect.

  **Allowed Values**: `bullet`, `decimal`, `lower_roman`, `upper_roman`, `lower_alphabetical`, `upper_alphabetical`, `character`, `none`
- `character` (string): If `type` is set to `character`, provide the character to use as the list item indicator. Only a single character is supported.

  **Maximum Length**: `1`

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
- [object InlineTextStyle](./inlinetextstyle.md)
  The object for applying text styling when not using HTML or Markdown formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/listitemstyle)*