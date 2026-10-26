# Caption

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding caption text.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Caption
```

## Mentions

- [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md)
- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)
- [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md)

#### Discussion

Use a `Caption` component to include a description for media components like `photo`, `gallery`, `video`, `map`, and so on. Apple News displays captions under the media component, but you can also add them above.

> **Note**:  This component creates caption text in the main article view. To add caption text in the full-screen view, use the `caption` property of the individual media component, such as [`Photo`](./photo.md).

##### Example

```json
{
  "components": [
    {
      "role": "title",
      "text": "Apple News Format"
    },
    {
      "role": "body",
      "text": "Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
    },
    {
      "role": "photo",
      "URL": "bundle://image.jpg"
    },
    {
      "role": "caption",
      "text": "Failure is not an option"
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `caption` for this component.

  **Allowed Values**: `caption`
- `text` (string) *(required)*: The text to display in the article, including any formatting tags depending on the `format` property.

  You can also use a subset of HTML tags or Markdown syntax by setting `format` to `html` or `markdown`, respectively. See [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md). Alternatively, you can style ranges of text individually using the [`InlineTextStyle`](./inlinetextstyle.md) object.
- `additions` ([Addition]): An array of all the additions that you apply to ranges of the component’s text.

  If you set format to `html` or `markdown`, Apple News Format doesnʼt support `Additions` or `InlineTextStyles`.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalText | [ConditionalText])): An instance or array of text components that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalText`, `[ConditionalText]`
- `format` (string): The formatting or markup method applied to the text.

  If you set `format` to `htm`l or `markdown`, Apple News Format doesn’t support `Additions` or `InlineTextStyles`.

  **Default**: `none`; **Allowed Values**: `markdown`, `html`, `none`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an `identifier` for your component if you want to anchor other components to it.
- `inlineTextStyles` (([InlineTextStyle] | string("none"))): An array of `InlineTextStyle` objects that you can use to apply different text styles to ranges of text. For each `InlineTextStyle`, you should supply a `rangeStart`, a `rangeLength`, and either a `TextStyle` object or the `identifier` of a `TextStyle` that you define at the top level of the document.

  Apple News Format ignores inline text styles when `format` is set to `markdown` or `html`.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `[InlineTextStyle]`, `string("none")`
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`
- `textStyle` ((ComponentTextStyle | string)): An inline `ComponentTextStyle` object that contains styling information, or a string reference to a `ComponentTextStyle` object that you define at the top level of the document.

  **Allowed Types**: `ComponentTextStyle`, `string`

## Relationships

### Inherits From
- [Text](./text.md)

## See Also

### Related Documentation
- [Adding an Image and Captions](../AppleNews/adding-an-image-and-captions.md)
  Create a photo that extends to both edges of the display, with captions that appear in the article layout and in full-screen view.
### Text
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)
  Use HTML formatting for text components.
- [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md)
  Use Markdown formatting for text components.
- [object Body](./body.md)
  The component for adding body text.
- [object Title](./title.md)
  The component for adding an article title.
- [object Heading](./heading.md)
  The text component for adding a heading.
- [object Intro](./intro.md)
  The component for adding introductory text.
- [object Author](./author.md)
  The component for adding the name of the author.
- [object Byline](./byline.md)
  The component for adding the publication date or contributor credits, especially for articles with multiple contributors.
- [object Illustrator](./illustrator.md)
  The component for adding illustrator credit.
- [object Photographer](./photographer.md)
  The component for adding a photographer credit.
- [object Quote](./quote.md)
  The component for including a quote.
- [object PullQuote](./pullquote.md)
  The component for including a pull quote.
- [object Text](./text.md)
  Properties shared by all text component types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/caption)*