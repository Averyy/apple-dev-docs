# TextStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TextStyle
```

## Mentions

- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)
- [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md)
- [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md)
- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)

## Discussion

A `TextStyle` object defines a style that you can apply to ranges of text. Include a property, with a name that you define and a `TextStyle` object for the value, in the [`ArticleDocument.textStyles`](./articledocument/textstyles-data.dictionary.md) object. Then,  you can use that property’s name string together with HTML, Markdown, or [`InlineTextStyle`](./inlinetextstyle.md) to apply the style to a range of text.

If you’re using Markdown syntax to style your text, see the [Inline Text Style](../AppleNews/using-markdown-with-apple-news-format.md#Inline-Text-Style) section in [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md). If you’re using HTML, see [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md).

You can use this object in [`ArticleDocument.textStyles`](./articledocument/textstyles-data.dictionary.md).

### Example

```json
{
  "textStyles": {
    "default-tag-abbr": {
      "textColor": "#34af15"
    }
  },
  "components": [
    {
      "role": "body",
      "format": "html",
      "text": "<p>The <abbr>WWF</abbr> is an international wildlife fund.</p>"
    }
  ]
}
```

## Properties

- `backgroundColor` ((Color | string("none"))): The background color for text lines. The value defaults to transparent.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Color`, `string("none")`
- `conditional` ((ConditionalTextStyle | [ConditionalTextStyle])): An instance or array of text style properties that you can apply conditionally, and the conditions that cause Apple News to apply them.

  **Allowed Types**: `ConditionalTextStyle`, `[ConditionalTextStyle]`
- `fontFamily` ((string | string("system"))): The font family, such as `GillSans`, to use for text rendering. Using a combination of `fontFamily`, `fontWeight`, `fontWidth`, and `fontStyle`, you can define the appearance of the text. Apple News automatically selects the appropriate font variant from the available variants in that family.

  See [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md).

  **Allowed Types**: `string`, `string("system")`
- `fontName` (string): The `fontName`, such as `GillSans-Bold`, that refers to an explicit font variant’s PostScript name. Alternatively, you can use a combination of `fontFamilys`, `fontWeigh`t, `fontWidth`, and/or `fontStyle` to have News automatically select the appropriate variant depending on the text formatting used.

  See [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md).
- `fontSize` (integer): The size of the font, in points. By default, Apple News uses the font size of the containing component or a default style. As a best practice, try not to go below 16 points for body text. Apple News may automatically resize the `fontSize` for different device sizes or for iOS and iPadOS devices with Larger Accessibility Sizes enabled.
- `fontStyle` (string): The font style to apply for the selected font.

  Valid values:

  - `normal`. Selects from the font family a font that’s defined as normal.
  - `italic`. Selects from the font family a font that’s defined as italic. If the family doesn’t contain an italic font variant, but contains an oblique variant, then Apple News selects `oblique` instead.
  - `oblique`. Selects from the font family a font that’s defined as oblique. If the family doesn’t contain an oblique font variant, but contains an italic variant, then Apple News selects `italic`**.**

  **Allowed Values**: `normal`, `italic`, `oblique`
- `fontWeight` ((integer | string)): The font weight to apply for font selection. In addition to explicit weights (named or numerical), you can use `lighter` and `bolder` to set text in a lighter or bolder font as compared to its surrounding text.

  If there’s no font variant with the given specifications in the provided font family, the system selects an alternative that has the closest match. If there’s no bold/bolder font, the system doesn’t create a bold alternative, but falls back to the closest match. Similarly, if there’s no italic or oblique font variant, the system won’t slant text to make it appear italicized.

  Valid values:

  - `thin` or `100`. Thin/hairline weight.
  - `extra-light`, `ultra-light,` or `200`. Extra-light/ultra-light weight.
  - `light` or `300`. Light weight.
  - `regular`, `normal`, `book`, `roman`, or `400`. Regular weight. This is the default weight if no weight is defined or inherited.
  - `medium` or `500`. Medium weight.
  - `semi-bold`, `demi-bold`, or `600`. Semi-bold/demi-bold weight.
  - `bold` or `700`. Bold weight. This is the default when using `<strong>` or `<b>` tags in HTML formatted text with default `fontWeight`.
  - `extra-bold`, `ultra-bold`, or `800`. Extra-bold/ultra-bold weight.
  - `black`, `heavy`, or `900`. Black/heavy weight.
  - `lighter`. A weight lighter than its surrounding text. When surrounding text is made bold, a value of `lighter` makes it medium.
  - `bolder`. A weight heavier than its surrounding text. When surrounding text is made light, a value of `bolder`  makes it regular.

  **Allowed Values**: `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `thin`, `extra-light`, `extralight`, `ultra-light`, `light`, `regular`, `normal`, `book`, `roman`, `medium`, `semi-bold`, `semibold`, `demi-bold`, `demibold`, `bold`, `extra-bold`, `extrabold`, `ultra-bold`, `ultrabold`, `black`, `heavy`, `lighter`, `bolder`; **Allowed Types**: `integer`, `string`
- `fontWidth` (string): The font width for font selection (known in CSS as `font-stretch`). Defines the width characteristics of a font variant between normal, condensed, and expanded. Some font families have separate families assigned for different widths (for example, `Avenir Next` and `Avenir Next Condensed`), so make sure that the `fontFamily` you select supports the specified `fontWidth`.

  Valid values:

  - `ultra-compressed`. Specifies the most compressed variant.
  - `extra-compressed`. Specifies a very compressed variant.
  - `compressed`. Specifies a compressed variant.
  - `ultra-condensed`. Specifies the most condensed variant.
  - `extra-condensed`. Specifies a very condensed variant.
  - `semi-condensed`. Specifies a semi-condensed variant.
  - `condensed`. Specifies a condensed variant.
  - `normal` (default). Specifies the font variant classified as normal.
  - `semi-expanded`. Specifies a semi-expanded variant.
  - `expanded`. Specifies an expanded variant.
  - `extra-expanded`. Specifies a very expanded variant.
  - `ultra-expanded`. Specifies the most expanded variant.

  **Allowed Values**: `ultra-compressed`, `extra-compressed`, `compressed`, `ultra-condensed`, `extra-condensed`, `condensed`, `semi-condensed`, `normal`, `semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`
- `orderedListItems` ((ListItemStyle | string("none"))): An object for use with text components with HTML markup. You can create text styles containing an `orderedListItems` definition to configure how Apple News displays list items inside `<ol>` tags.

  Use the none value for conditional design elements. Adding it here has no effect.

  > **Note**:  You can only configure display options for list items at the component level. You can’t configure individual list items, and you can’t include a mix of `orderedListItems` and `unorderedListItems` in a single component.

  **Allowed Types**: `ListItemStyle`, `string("none")`
- `strikethrough` ((TextDecoration | boolean)): The text `strikethrough`. Set `strikethrough` to `true` to use the text color inherited from the `textColor` property as the `strikethrough` color, or provide a text decoration definition with a different color. By default strikethrough is omitted (`false`).

  **Allowed Types**: `TextDecoration`, `boolean`
- `stroke` ((TextStrokeStyle | string("none"))): The `stroke` style for the text outline. By default, `stroke` is  omitted.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `TextStrokeStyle`, `string("none")`
- `textColor` (Color): The text color.
- `textShadow` ((TextShadow | string("none"))): The text shadow for this style.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `TextShadow`, `string("none")`
- `textTransform` (string): The transform to apply to the text.

  Valid values:

  - `uppercase`
  - `lowercase`
  - `capitalize`. Capitalizes the first letter of all words in the string.
  - `smallcaps`. Capitalizes the lowercase letters as small capital letters.
  - `none` (default)

  **Allowed Values**: `uppercase`, `lowercase`, `capitalize`, `smallcaps`, `none`
- `tracking` (number): The amount of tracking (spacing between characters) in text, as a percentage of the `fontSize`. The actual spacing between letters is determined by combining information from the font and font size.

  Example: Set `tracking` to `0.5` to make the distance between characters increase by 50 percent of the `fontSize`. With a font size of 10, the additional space between characters is 5 points.

  **Default**: `0`
- `underline` ((TextDecoration | boolean)): The text underlining. You can use this style for links. Set `underline` to `true` to use the text color as the underline color, or provide a text decoration with a different color. By default underline is omitted (`false`).

  **Allowed Types**: `TextDecoration`, `boolean`
- `unorderedListItems` ((ListItemStyle | string("none"))): An object for use with text components with HTML markup. You can create text styles containing an `unorderedListItems` definition to configure how Apple News displays list items inside `<ul>` tags.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  > **Note**:  You can only configure display options for list items at the component level. You can’t configure individual list items, and you can’t include a mix of `orderedListItems` and `unorderedListItems` in a single component.

  **Allowed Types**: `ListItemStyle`, `string("none")`
- `verticalAlignment` (string): The vertical alignment of the text. You can use this property for superscripts and subscripts.

  Overrides values specified in parent text styles.

  Default value: `baseline` when unspecified, or the value you specify in a `TextStyle` object applied to the same range.

  The values `superscript` and `subscript` also adjust the font size to two-thirds of the size defined for that character range.

  **Allowed Values**: `superscript`, `subscript`, `baseline`

## Relationships

### Inherited By
- [ComponentTextStyle](./componenttextstyle.md)
- [ConditionalComponentTextStyle](./conditionalcomponenttextstyle.md)
- [ConditionalTextStyle](./conditionaltextstyle.md)

## See Also

### Related Documentation
- [Adding Color to Text Ranges](../AppleNews/adding-color-to-text-ranges.md)
  Create text in color by using HTML to refer to TextStyle objects.
### Text Styles
- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md)
  Choose a font family for Apple News Format that’s supported in iOS, iPadOS, and macOS.
- [object ComponentTextStyle](./componenttextstyle.md)
  The object for defining the style for a text component, including spacing, alignment, and drop caps.
- [object DropCapStyle](./dropcapstyle.md)
  The object for defining the drop cap text style to use in the first paragraph in a text component.
- [object ListItemStyle](./listitemstyle.md)
  The object for defining the style for bulleted or numbered lists in an article.
- [object InlineTextStyle](./inlinetextstyle.md)
  The object for applying text styling when not using HTML or Markdown formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/textstyle)*