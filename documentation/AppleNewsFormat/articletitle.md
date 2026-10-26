# ArticleTitle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for displaying an article title in the ArticleLink component.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object ArticleTitle
```

## Mentions

- [Creating an Article Link](../AppleNews/creating-an-article-link.md)

#### Discussion

Use the `ArticleTitle` object to display the title of the linked article. `ArticleTitle` is used in combination with the [`ArticleLink`](./articlelink.md) component and is used by [VoiceOver for iOS](https://www.apple.com/accessibility/iphone/vision/) and [VoiceOver for macOS](https://www.apple.com/accessibility/mac/vision/) to make content more accessible.

##### Example

```json
{
  "components": [
    {
      "role": "article_link",
      "articleIdentifier": "https://apple.news/AT6kNQslCQy6EE4bF8hpOoQ",
      "components": [
        {
          "role": "article_thumbnail",
          "aspectRatio": 1,
          "fillMode": "cover",
          "verticalAlignment": "top"
        },
        {
          "role": "article_title"
        }
      ]
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `article_title` for this object.

  **Allowed Values**: `article_title`
- `additions` ([Addition]): Ignored for all children of [`ArticleLink`](./articlelink.md).
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalText | [ConditionalText])): An instance or array of text properties that can be applied conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalText`, `[ConditionalText]`
- `format` (string): The formatting or markup method applied to the text.

  Valid values:

  - `html`. See [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md).
  - `markdown`. See [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md).
  - `none` (default). Styles (`inlineTextStyles)` and `additions` need to be defined to create links or change text styling for ranges of text.

  Inline styling and additions with ranges (using `inlineTextStyles` and `additions` properties) are only supported when `forma`t is `none`.

  **Default**: `none`; **Allowed Values**: `markdown`, `html`, `none`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): A unique identifier for this component. If used, the identifier must be unique across the entire document. An identifier is required if you want to anchor other components to this component. See [`Anchor`](./anchor.md).
- `inlineTextStyles` (([InlineTextStyle] | string("none"))): An array of `InlineTextStyle` objects you can use to apply different text styles to ranges of text. For each `InlineTextStyle` object, supply `rangeStart` and `rangeLength` values, and either a [`TextStyle`](./textstyle.md) object or the identifier of a text style that is defined at the top level of the document.

  Inline text styles are ignored when the `format` is set to `markdown` or `html`.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `[InlineTextStyle]`, `string("none")`
- `layout` ((ComponentLayout | string)): Either an inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If `layou`t is not defined, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`
- `text` (string): The text, styled according to the `textStyle` definition. You can also use a subset of HTML syntax by setting `format` to `html`. See [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md).
- `textStyle` ((ComponentTextStyle | string)): An inline `ComponentTextStyle` object that contains styling information, or a string reference to a `ComponentTextStyle` object that is defined at the top level of the document.

  **Allowed Types**: `ComponentTextStyle`, `string`

## Relationships

### Inherits From
- [Text](./text.md)

## See Also

### Article Structure
- [Nesting Components in an Article](../AppleNews/nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](../AppleNews/adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Creating an Article Link](../AppleNews/creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)
  Configure a side-by-side, horizontal arrangement of components for your article.
- [object Header](./header.md)
  The component for defining the top area of an article, chapter, or section.
- [object Container](./container.md)
  Properties shared by all container types.
- [object Section](./section.md)
  The component for organizing an article into sections.
- [object Chapter](./chapter.md)
  The component for organizing an article into chapters.
- [object Aside](./aside.md)
  The component for setting apart content that is not directly related to the article, such as promotional content.
- [object CollectionDisplay](./collectiondisplay.md)
  An object used in any container component type to define how the collection of child components is presented.
- [object HorizontalStackDisplay](./horizontalstackdisplay.md)
  The object for displaying components side by side in a Container component.
- [object FlexibleSpacer](./flexiblespacer.md)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](./divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](./articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](./supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articletitle)*