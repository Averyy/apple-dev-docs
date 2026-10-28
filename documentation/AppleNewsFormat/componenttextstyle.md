# ComponentTextStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the style for a text component, including spacing, alignment, and drop caps.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ComponentTextStyle
```

## Mentions

- [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md)
- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)
- [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md)
- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)

## Discussion

Use a `ComponentTextStyle` object to define the text style for an entire text component (such as `body` or `heading`). A `ComponentTextStyle` object can have the same properties as a `TextStyle` object, as well as some additional properties such as a drop cap and text alignment.

To use a `ComponentTextStyle` once, include a `ComponentTextStyle` object as the value of the individual component’s `style` property.

To define a style that multiple components can use:

1. Include a property, with a name that you define and a `ComponentTextStyle` object value, in the [`ArticleDocument.componentTextStyles`](./articledocument/componenttextstyles-data.dictionary.md) object.
2. Use the name you created as the value of the individual component’s `textStyle` property.

To create a default text style for the article, define a component text style in [`ArticleDocument.componentTextStyles`](./articledocument/componenttextstyles-data.dictionary.md) object and use the key `default`.

To create a default component text style for a `role`, `d`efine a component text style in [`ArticleDocument.componentTextStyles`](./articledocument/componenttextstyles-data.dictionary.md) and use the key `default-<role>`. For example, if you define a component text style with the key `default-title`, all components with a `role` of `title` use that style, unless you override it.

For more information about properties, objects, keys, and values, see [JSON Concepts and Article Structure](../AppleNews/json-concepts-and-article-structure.md). For more about components and roles, see [Components](../AppleNews/components.md).

You can use this object in [`Text`](./text.md) and [`ArticleDocument.componentTextStyles`](./articledocument/componenttextstyles-data.dictionary.md).

### Example

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 20,
      "dropCapStyle": {
        "numberOfLines": 3,
        "numberOfRaisedLines": 2,
        "numberOfCharacters": 1,
        "fontName": "HelveticaNeue",
        "textColor": "#FFF",
        "backgroundColor": "#000",
        "padding": 5
      }
    }
  },
  "components": [
    {
      "role": "body",
      "text": "This is body text",
      "textStyle": "exampleStyle"
    }
  ]
}
```

## Properties

- `backgroundColor` ((Color | string("none"))): The background color for text lines. The value defaults to transparent.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Color`, `string("none")`
- `conditional` ((ConditionalComponentTextStyle | [ConditionalComponentTextStyle])): An instance or array of component text style properties that can be applied conditionally, and the conditions that cause them to be applied.

  **Allowed Types**: `ConditionalComponentTextStyle`, `[ConditionalComponentTextStyle]`
- `dropCapStyle` ((DropCapStyle | string("none"))): The style of drop cap to apply to the first paragraph of the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `DropCapStyle`, `string("none")`
- `firstLineIndent` (integer): The indent of the first line of each paragraph in points.
- `fontFamily` ((string | string("system"))): The font family to use for text rendering; for example, `Gill` `Sans`. Using a combination of `fontFamily`, `fontWidth`, `fontWeight`, and `fontStyle`, you can define the appearance of the text. Apple News automatically selects the appropriate font variant from the available variants in that family. See [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md).

  You can use the value `system` to show text in the default font the operating system uses.

  **Allowed Types**: `string`, `string("system")`
- `fontName` (string): The `fontName` to refer to an explicit font variant’s Postscript name, such as `GillSans-Bold`. Alternatively, you can use a combination of `fontFamily`, `fontWeight`, `fontWidth`, and/or `fontStyle` to have News automatically select the appropriate variant depending on the text formatting you use.

  See [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md).
- `fontScaling` (boolean): A Boolean value that indicates whether scaling of font sizes for various screen sizes is enabled.

  By default, text in Apple News Format articles is  scaled down when viewed on devices with screens that are narrower than the width specified in the document layout. This scaling effect occurs at a faster rate for heading roles ([`Title`](./title.md), [`Heading`](./heading.md), and so on) than for body roles ([`Body`](./body.md), [`Byline`](./byline.md), [`Caption`](./caption.md), and so on).

  To disable this effect, set `fontScaling` to `false`. When doing so, be mindful of how larger text appears on smaller devices and make use of `conditions` as appropriate. See [`ConditionalComponentTextStyle`](./conditionalcomponenttextstyle.md).

  **Default**: `true`
- `fontSize` (integer): The size of the font, in points. By default, Apple News applies the font size from a containing component or a default style. As a best practice, try not to go below 16 points for body text. The `fontSize` may be automatically resized for different device sizes or for iOS and iPadOS devices with Larger Accessibility Sizes enabled.
- `fontStyle` (string): The font style to apply.

  Valid values:

  - `normal`. Selects a font defined as normal from the font family.
  - `italic`. Selects a font defined as italic from the font family. If the family doesn’t contain an italic font variant, but contains an oblique variant, then Apple News selects `oblique` instead.
  - `oblique`. Selects a font defined as oblique from the font family. If the family doesn’t contain an oblique font variant, but contains an italic variant, then Apple News selects `italic` .

  **Allowed Values**: `normal`, `italic`, `oblique`
- `fontWeight` ((integer | string)): The font weight to apply for font selection. In addition to specific weights (named or numerical), `lighter` and `bolder` are available, to set text in a lighter or bolder font as compared to its surrounding text.

  If Apple News can’t find a font variant with the given specifications in the provided font family, it selects an alternative with the closest match. If Apple News doesn’t find a bold/bolder font, it doesn’t create a faux-bold alternative, and instead uses the closest match. Similarly, if Apple News can’t find an italic or oblique font variant, it won’t slant text or make it appear italicized.

  Valid values:

  - `thin` or `100`. Thin/hairline weight.
  - `extra-light`, `ultra-light`, or `200`. Extra-light/ultra-light weight.
  - `light` or `300`. Light weight.
  - `regular`, `normal`, `book`, `roman`, or `400` (default). Regular weight. This is the default weight if you don’t define a weight or a weight isn’t inherited.
  - `medium` or `500`. Medium weight.
  - `semi-bold`, `demi-bold`, `or` `600`. Semi-bold/demi-bold weight.
  - `bold` or `700`. Bold weight. This is the default when using `<strong>` or `<b>` tags in HTML formatted text with default `fontWeight`.
  - `extra-bold`, `ultra-bold`, or `800`. Extra-bold/ultra-bold weight.
  - `black`, `heavy`, or `900`. Black/heavy weight.
  - `lighter`. A weight lighter than its surrounding text. When surrounding text is bold, using a value of `lighter` makes text medium weight.
  - `bolder`. A weight heavier than its surrounding text. When surrounding text is light, using a value of `bolder` makes text regular weight.

  **Allowed Values**: `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `thin`, `extra-light`, `extralight`, `ultra-light`, `light`, `regular`, `normal`, `book`, `roman`, `medium`, `semi-bold`, `semibold`, `demi-bold`, `demibold`, `bold`, `extra-bold`, `extrabold`, `ultra-bold`, `ultrabold`, `black`, `heavy`, `lighter`, `bolder`; **Allowed Types**: `integer`, `string`
- `fontWidth` (string): The font width to apply for font selection (known in CSS as `font-stretch`) defines the width characteristics of a font variant between `normal`, `condensed`, and `expanded`. Some font families have separate families assigned for different widths (for example, `Avenir Next` and `Avenir Next Condensed`), so make sure that the `fontFamily` you select supports the specified `fontWidth`.

  Valid values:

  - `ultra-condensed`. Specifies the most condensed variant.
  - `extra-condensed`. Specifies a very condensed variant.
  - `condensed`. Specifies a condensed variant.
  - `semi-condensed`. Specifies a semi-condensed variant.` `
  - `normal` (default). Specifies the font variant classified as normal.
  - `semi-expanded`. Specifies a semi-expanded variant.` `
  - `expanded`. Specifies an expanded variant.
  - `extra-expanded`. Specifies a very expanded variant.` `
  - `ultra-expanded`. Specifies the most expanded variant.

  **Allowed Values**: `ultra-compressed`, `extra-compressed`, `compressed`, `ultra-condensed`, `extra-condensed`, `condensed`, `semi-condensed`, `normal`, `semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`
- `hangingPunctuation` (boolean): A Boolean value that defines whether Apple News positions punctuation outside the margins of the text.

  **Default**: `false`
- `hyphenation` (boolean): A Boolean value that indicates whether Apple News hyphenates text when necessary. By default, only components with a `role` of `body` or `intro` have hyphenation enabled. All other components default to `false`.
- `hyphenationMinimumCharactersAfter` (integer):

  > **Note**:  Available in iOS 17, iPadOS 17, and macOS 14 beta release.

  The minimum number of characters required after the hyphen to enable hyphenation.

  **Default**: `3`
- `hyphenationMinimumCharactersBefore` (integer):

  > **Note**:  Available in iOS 17, iPadOS 17, and macOS 14 beta release.

  The minimum number of characters required before the hyphen to enable hyphenation.

  **Default**: `3`
- `hyphenationMinimumWordLength` (integer):

  > **Note**:  Available in iOS 17, iPadOS 17, and macOS 14 beta release.

  The minimum number of characters required for a word to be hyphenated.

  **Default**: `0`
- `hyphenationZone` (integer):

  > **Note**:  Available in iOS 17, iPadOS 17, and macOS 14 beta release.

  The area in points from the right edge of the text component before which a word needs to start to enable hyphenation.

  By default, the value is set to `18` points.

  A larger value reduces the allowable hyphenation area of a word, which can result in a more ragged appearance of the text along the right margin.

  **Default**: `18`
- `lineBalancing` (boolean):

  > **Note**:  Available in iOS 17, iPadOS 17, and macOS 14 beta release.

  A Boolean value that defines whether the system enables line balancing for the text component.

  **Default**: `false`
- `lineHeight` (integer): A number that provides the default line height, in points. Apple News recalculates `lineHeigh`t as necessary, relative to the `fontSize`. For example, when Apple News automatically resizes the font to fit a smaller screen, it also readjusts the line height accordingly.
- `linkStyle` ((TextStyle | string("none"))): An object that provides text styling for all links within a text component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `TextStyle`, `string("none")`
- `orderedListItems` ((ListItemStyle | string("none"))): An object for use with text components with HTML markup. You can create text styles containing an `orderedListItems` definition to configure how Apple News displays the list items inside `<ol>` tags.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ListItemStyle`, `string("none")`
- `paragraphSpacingAfter` (integer): A number that defines the spacing after each paragraph in points relative to the `lineHeight`.
- `paragraphSpacingBefore` (integer): A number that defines the spacing before each paragraph in points relative to the `lineHeight`.
- `strikethrough` ((TextDecoration | boolean)): The text strikethrough. Set `strikethrough` to `true` to use the text color inherited from the `textColor` property as the strikethrough color, or provide a text decoration definition with a different color.

  **Allowed Types**: `TextDecoration`, `boolean`
- `stroke` ((TextStrokeStyle | string("none"))): The `stroke` style for the text outline. By default, Apple News omits the `stroke`.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `TextStrokeStyle`, `string("none")`
- `textAlignment` (string): The justification for all text within the component.

  If you omit `textAlignment` or set it to `none`, Apple News determines the justification by the text direction (left-to-right text is aligned to the left and right-to-left text is aligned to the right).

  **Default**: `none`; **Allowed Values**: `left`, `center`, `right`, `justified`, `none`
- `textColor` (Color): The text color.
- `textShadow` ((TextShadow | string("none"))): The text shadow for this style.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `TextShadow`, `string("none")`
- `textTransform` (string): The transform to apply to the text.

  Valid values:

  - `uppercase`
  - `lowercase`
  - `capitalize`. `C`apitalizes the first letter of all words in the string.
  - `smallcaps`. Capitalizes the lowercase letters as small capital letters.
  - `none` (default)

  **Allowed Values**: `uppercase`, `lowercase`, `capitalize`, `smallcaps`, `none`
- `tracking` (number): The amount of tracking (spacing between characters) in text, as a percentage of the `fontSize`. Apple News determines the actual spacing between letters by combining information from the font and font size.

  Example: Set `tracking` to `0.5` to make the distance between characters increase by 50 percent of the `fontSize`. With a font size of 10, the additional space between characters is 5 points.

  **Default**: `0`
- `underline` ((TextDecoration | boolean)): The text underlining. You can use this style for links. Set `underline` to `true` to use the text color as the underline color, or provide a text decoration with a different color.

  **Allowed Types**: `TextDecoration`, `boolean`
- `unorderedListItems` ((ListItemStyle | string("none"))): The object for use with text components with HTML markup. You can create text styles containing an `unorderedListItems` definition to configure how Apple News displays the list items inside `<ul>` tags.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ListItemStyle`, `string("none")`
- `verticalAlignment` (string): The vertical alignment of the text. You can use this property for superscripts and subscripts.

  To override values specified in parent text styles, use `baseline`.

  Defaults to `baseline` when unspecified, and inherits the value specified in a `TextStyle` applied to the same range.

  The values `superscript` and `subscript` also adjust the font size to 2/3 of the size defined for that character range.

  **Allowed Values**: `superscript`, `subscript`, `baseline`

## Relationships

### Inherits From
- [TextStyle](./textstyle.md)

## See Also

### Related Documentation
- [Creating Your First Article](../AppleNews/creating-your-first-article.md)
  Create an article with text components and component text styles.
### Text Styles
- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [Applying Apple News Format Fonts](../AppleNews/applying-apple-news-format-fonts.md)
  Choose a font family for Apple News Format that’s supported in iOS, iPadOS, and macOS.
- [object TextStyle](./textstyle.md)
  The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.
- [object DropCapStyle](./dropcapstyle.md)
  The object for defining the drop cap text style to use in the first paragraph in a text component.
- [object ListItemStyle](./listitemstyle.md)
  The object for defining the style for bulleted or numbered lists in an article.
- [object InlineTextStyle](./inlinetextstyle.md)
  The object for applying text styling when not using HTML or Markdown formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/componenttextstyle)*