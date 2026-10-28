# ArticleLink

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The container component for creating a link to an article.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object ArticleLink
```

## Mentions

- [Creating an Article Link](../AppleNews/creating-an-article-link.md)

## Discussion

Use the `ArticleLink` component to link a user to the article specified using the `articleIdentifier` property. If no `articleIdentifier` is provided, the component is assumed to be self referencing. Use [`ArticleThumbnail`](./articlethumbnail.md) and [`ArticleTitle`](./articletitle.md) as child components instead of [`Image`](./image.md) or [`Text`](./text.md) to provide semantic value to the linked article. You can use these components to provide content, styling, and layout, like you do with any other Apple News Format component. Apple News automatically populates the content based on nested child elements. A [`ComponentAddition`](./componentaddition.md) is automatically added to the component to allow the user to navigate to the referenced article.

### Example

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

- `articleIdentifier` ((SupportedArticleIdentifier | PublisherArticleIdentifier)): The shareable URL or CloudKit ID of an article that is navigated to, and that is used as the default title and thumbnail. If `articleIdentifier` is not provided, the identifier of the article is used.

  **Allowed Types**: `SupportedArticleIdentifier`, `PublisherArticleIdentifier`
- `role` (string) *(required)*: Always `article_link` for this component.

  **Allowed Values**: `article_link`
- `additions` ([ComponentLink]): An array of `ComponentLink` objects you can use to create a ComponentLink, allowing a link to anywhere in News.

  `additions` is automatically added to the `ArticleLink` container.

  Any link additions defined here or in any of the child components ([`ArticleTitle`](./articletitle.md) and [`ArticleThumbnail`](./articlethumbnail.md)) have no effect.
- `allowAutoplacedAds` (boolean): A Boolean value that allows the placement of ad banners between components. Nested components inherit the value of the outermost container that explicitly sets `allowAutoplacedAds`. The default value is `false`.

  **Default**: `false`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `components` ([Component]): An array of components to display as child components. Child components are positioned and rendered relative to their parent component.
- `conditional` ((ConditionalContainer | [ConditionalContainer])): An instance or array of container properties that can be applied conditionally,  and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalContainer`, `[ConditionalContainer]`
- `contentDisplay` ((CollectionDisplay | HorizontalStackDisplay | string("none"))): An object that defines how to position child components within this `articleLink` component. A [`HorizontalStackDisplay`](./horizontalstackdisplay.md), for example, allows for displaying child components side by side.

  In versions of News prior to iOS 11, child components are positioned as if `contentDisplay` were not defined.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `CollectionDisplay`, `HorizontalStackDisplay`, `string("none")`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If used, this identifier must be unique across the entire document. You will need an identifier for your component if you want to anchor other components to it. See [`Anchor`](./anchor.md).
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If `layout` is not defined, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Container](./container.md)

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
- [type SupportedArticleIdentifier](./supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.
- [type PublisherArticleIdentifier](./publisherarticleidentifier.md)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articlelink)*