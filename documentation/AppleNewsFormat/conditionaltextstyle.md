# ConditionalTextStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditional properties for a text style, and when the conditional properties are in effect.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object ConditionalTextStyle
```

## Mentions

- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)

## Discussion

Use the `ConditionalTextStyle` object to define an array of conditional text style properties and the conditions under which to apply them. When a condition is met, the value of a property in `ConditionalTextStyle` overrides the value of the same property if defined in the parent `TextStyle` object. See [`TextStyle`](./textstyle.md).

### Example

```json
{
  "components": [
    {
      "role": "body",
      "text": "Lorem ipsum dolor sit amet, <span data-anf-textstyle='exampleTextStyle'>consectetur adipiscing elit.</span>",
      "format": "html"
    }
  ],
  "textStyles": {
    "exampleTextStyle": {
      "textColor": "#FF0000",
      "conditional": [
        {
          "underline": true,
          "textColor": "#000",
          "conditions": [
            {
              "minContentSizeCategory": "XXXL"
            }
          ]
        }
      ]
    }
  }
}
```

## Properties

- `conditions` ((Condition | [Condition])) *(required)*: An instance or array of conditions that, when met, cause the conditional text style properties to take effect.

  **Allowed Types**: `Condition`, `[Condition]`
- `backgroundColor` ((Color | string("none"))): The background color for text lines. This value defaults to transparent.

  To remove a previously set condition, use `none`.

  **Allowed Types**: `Color`, `string("none")`
- `fontFamily` ((string | string("system"))): The font family to use for text rendering; for example, `Gill Sans`. Using a combination of `fontFamily`, `fontWeight`, and `fontStyle`, you can define the appearance of the text. Apple News automatically selects the appropriate font variant from the available variants in that family. See [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md).

  In iOS 13, iPadOS 13,  and macOS 10.15 and later, you can use the value `system` to show text in the default font used by the operating system.

  **Allowed Types**: `string`, `string("system")`
- `fontName` (string): The font name to use to refer to an explicit font variant’s PostScript name, such as `GillSans-Bold`. Alternatively, you can use a combination of `fontFamily`, `fontWeight`, and `fontStyle` to have Apple News automatically select the appropriate variant depending on the text formatting used.

  See [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md).
- `fontSize` (integer): The size of the font, in points. By default, the font size is inherited from a parent component or a default style. As a best practice, try not to go below 16 points for body text. Apple News may automatically resize the `fontSize` for different device sizes or for iOS and iPadOS devices with Larger Accessibility Sizes enabled.
- `fontStyle` (string): The font style to apply for the selected font.

  Valid values:

  - `normal`. Selects from the font family a font that Apple News defines as normal.
  - `italic`. Selects from the font family a font that Apple News defines as italic. If the family doesn’t contain an italic font variant, but contains an oblique variant, Apple News selects `oblique`  instead.
  - `oblique`. Selects from the font family a font that Apple News defines as oblique. If the family doesn’t contain an oblique font variant, but contains an italic variant, Apple News selects `italic` instead.

  **Allowed Values**: `normal`, `italic`, `oblique`
- `fontWeight` ((integer | string)): The font weight to apply for the selected font. In addition to explicit weights (named or numerical), `lighter` and `bolder` are available, to set text in a lighter or bolder font as compared to the surrounding text.

  If Apple News can’t find a font variant with the given specifications in the provided font family, it selects an alternative with the closest match. If Apple News doesn’t find a bold/bolder font, it doesn’t create a faux-bold alternative, and instead uses the closest match. Similarly, if Apple News can’t find an italic or oblique font variant, it won’t slant text or make it appear italicized.

  Valid values:

  - `thin` or `100`. Thin or hairline weight.
  - `extra-light`, `ultra-light`, or `200`. Extra-light or ultra-light weight.
  - `light` or `300`. Light weight.
  - `regular`, `normal`, `book`, `roman`, or `400`. Regular weight. This is the default if no weight is defined or inherited.
  - `medium` or `500`. Medium weight.
  - `semi-bold`, `demi-bold`, or `600`. Semi-bold or demi-bold weight.
  - `bold` or `700`. Bold weight. This is the default when using `<strong>` or `<b>` tags in HTML with default `fontWeight`.
  - `extra-bold`, `ultra-bold`, or `800`. Extra-bold or ultra-bold weight.
  - `black`, `heavy`, or `900`. Black or heavy weight.
  - `lighter`. A weight lighter than its surrounding text. When you make the surrounding text bold, a value of `lighter` makes it medium.
  - `bolder`. A weight heavier than its surrounding text. When you make surrounding text light, a value of `bolder` makes it regular.

  **Allowed Values**: `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `thin`, `extra-light`, `extralight`, `ultra-light`, `light`, `regular`, `normal`, `book`, `roman`, `medium`, `semi-bold`, `semibold`, `demi-bold`, `demibold`, `bold`, `extra-bold`, `extrabold`, `ultra-bold`, `ultrabold`, `black`, `heavy`, `lighter`, `bolder`; **Allowed Types**: `integer`, `string`
- `fontWidth` (string): The font width for the selected font (known in CSS as font-stretch). This value defines the width characteristics of a font variant between normal, condensed, and expanded. Some font families are categorized by width (for example, `Avenir Next` and `Avenir Next Condensed`), so make sure that the font family you select supports the specified font width.

  Valid values:

  - `ultra-condensed`. The most condensed variant.
  - `extra-condensed`. A very condensed variant.
  - `condensed`. A condensed variant.
  - `semi-condensed`. A semi-condensed variant.
  - `normal` (default). The font variant classified as normal.
  - `semi-expanded`. A semi-expanded variant.
  - `expanded`. An expanded variant.
  - `extra-expanded`. A very expanded variant.
  - `ultra-expanded`. The most expanded variant.

  **Allowed Values**: `ultra-compressed`, `extra-compressed`, `compressed`, `ultra-condensed`, `extra-condensed`, `condensed`, `semi-condensed`, `normal`, `semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`
- `orderedListItems` ((ListItemStyle | string("none"))): An object for use with text components with HTML markup. You can create text styles containing an `orderedListItems` definition to configure how to display list items inside `<ol>` tags.

  To remove a previously set condition, use `none`.

  **Allowed Types**: `ListItemStyle`, `string("none")`
- `strikethrough` ((TextDecoration | boolean)): The text strikethrough. Set `strikethrough` to `true` to use the text color inherited from the `textColor` property as the strikethrough color, or provide a text decoration definition with a different color. By default, Apple News omits strikethrough (`false`).

  **Allowed Types**: `TextDecoration`, `boolean`
- `stroke` ((TextStrokeStyle | string("none"))): The stroke style for the text outline. By default, Apple News omits `stroke`.

  To remove a previously set condition, use `none`.

  **Allowed Types**: `TextStrokeStyle`, `string("none")`
- `textColor` (Color): The text color.
- `textShadow` ((TextShadow | string("none"))): The text shadow for this style.

  To remove a previously set condition, use `none`.

  **Allowed Types**: `TextShadow`, `string("none")`
- `textTransform` (string): The transform to apply to the text.

  Valid values:

  - `uppercase`
  - `lowercase`
  - `capitalize`. Capitalizes the first letter of all words in the string.
  - `smallcaps`. Capitalizes the lowercase letters as short capital letters.
  - `none` (default)

  **Allowed Values**: `uppercase`, `lowercase`, `capitalize`, `smallcaps`, `none`
- `tracking` (number): The amount of tracking (spacing between characters) in text, as a percentage of the font size. The actual spacing between letters is determined by combining information from the font and font size.

  Example: Set tracking to `0.5` to make the distance between characters increase by 50% of the `fontSize`. With a font size of `10`, the additional space between characters is `5` points.

  **Default**: `0`
- `underline` ((TextDecoration | boolean)): The text underlining. You can use this style for links. Set underline to `true` to use the text color as the underline color, or provide a text decoration with a different color. By default, Apple News omits underline  (`false`).

  **Allowed Types**: `TextDecoration`, `boolean`
- `unorderedListItems` ((ListItemStyle | string("none"))): An object for use with text components with HTML markup. You can create text styles containing an `unorderedListItems` definition to configure how to display list items inside `<ul>` tags.

  To remove a previously set condition, use none.

  **Allowed Types**: `ListItemStyle`, `string("none")`
- `verticalAlignment` (string): The vertical alignment of the text. You can use this property for superscripts and subscripts.

  Overrides values specified in parent text styles.

  Default value: `baseline` when unspecified, or the value specified in a `TextStyle` object applied to the same range.

  The values `superscript` and `subscript` also adjust the font size to two-thirds of the size defined for that character range.

  **Allowed Values**: `superscript`, `subscript`, `baseline`

## Relationships

### Inherits From
- [TextStyle](./textstyle.md)

## See Also

### Conditional Design Elements
- [object Condition](./condition.md)
  The object for defining a condition that, when met, causes conditional properties to go into effect.
- [object ConditionalComponent](./conditionalcomponent.md)
  The object for defining conditional properties for a component, and when the conditional properties are in effect.
- [object ConditionalComponentLayout](./conditionalcomponentlayout.md)
  The object for defining conditional properties for a component layout, and when the conditional properties are in effect.
- [object ConditionalAutoPlacement](./conditionalautoplacement.md)
  The object for defining conditional properties for an automatically placed component, and when the conditional properties are in effect.
- [object ConditionalSection](./conditionalsection.md)
  The object for defining conditional properties for a section component, and when the conditional properties are in effect.
- [object ConditionalDocumentStyle](./conditionaldocumentstyle.md)
  The object for defining conditional properties for a document style, and when the conditional properties are in effect.
- [object ConditionalText](./conditionaltext.md)
  The object for defining conditional properties for a text component, and when the conditional properties are in effect.
- [object ConditionalComponentTextStyle](./conditionalcomponenttextstyle.md)
  The object for defining conditional properties for a component text style, and when the conditional properties are in effect.
- [object ConditionalComponentStyle](./conditionalcomponentstyle.md)
  The object for defining conditional properties for a component style, and when the conditional properties are in effect.
- [object ConditionalContainer](./conditionalcontainer.md)
  The object for defining conditional properties for a container component, and when the conditional properties are in effect.
- [object ConditionalDivider](./conditionaldivider.md)
  The object for defining conditional properties for a divider component, and when the conditional properties are in effect.
- [object ConditionalButton](./conditionalbutton.md)
  The object for defining a button component’s conditional properties, and when the conditional properties are in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionaltextstyle)*