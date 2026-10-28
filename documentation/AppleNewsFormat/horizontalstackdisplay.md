# HorizontalStackDisplay

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for displaying components side by side in a Container component.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object HorizontalStackDisplay
```

## Mentions

- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)

## Discussion

Use the `HorizontalStackDisplay` object in a container component for displaying components side by side.

Use `HorizontalStackDisplay` if you wish to specify what percent of the width the individual children should use. Use [`CollectionDisplay`](./collectiondisplay.md) if you wish to make all child components to have the same width.

To redistribute the empty space inside a horizontal stack collection, use the [`FlexibleSpacer`](./flexiblespacer.md) object.

> **Note**:  In versions of iOS before iOS 12, child components are vertically stacked if the container’s `contentDisplay` property is defined as the new `horizontal_stack` type.

This object can be used in [`Header`](./header.md), [`Container`](./container.md), [`Section`](./section.md), [`Chapter`](./chapter.md), [`Aside`](./aside.md), and [`ArticleLink`](./articlelink.md).

### Example

```json
{
  "components": [
    {
      "role": "container",
      "contentDisplay": {
        "type": "horizontal_stack"
      },
      "components": [
        {
          "role": "title",
          "text": "Sample article",
          "layout": {
            "minimumWidth": "60cw",
            "maximumWidth": "60cw"
          }
        },
        {
          "role": "spacer"
        },
        {
          "role": "image",
          "URL": "bundle://image-1.jpg",
          "layout": {
            "minimumWidth": "35cw",
            "maximumWidth": "35cw"
          }
        }
      ]
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: Always `horizontal_stack` for this object.

  **Allowed Values**: `horizontal_stack`

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
- [object FlexibleSpacer](./flexiblespacer.md)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](./divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](./articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](./supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.
- [type PublisherArticleIdentifier](./publisherarticleidentifier.md)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/horizontalstackdisplay)*