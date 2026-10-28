# Section

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for organizing an article into sections.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Section
```

## Mentions

- [Adding a Scene to a Chapter or a Section Header](../AppleNews/adding-a-scene-to-a-chapter-or-a-section-header.md)
- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)
- [Nesting Components in an Article](../AppleNews/nesting-components-in-an-article.md)

## Discussion

A `section` is a full-width container component that lets you nest components so you can divide a large article into separate parts with potentially different styling. You can also use the `section` component to divide large chapters.

The `section` component is a structural component intended to organize an entire article, so you generally use it in the `components` array in the [`ArticleDocument`](./articledocument.md) properties. The overall height of a section is determined by the height of its child components.

> **Note**:  The `section` component has the same properties as the `chapter` component, so you can use the one that fits best for your content.

### Example

```json
{
  "components": [
    {
      "role": "section",
      "components": [
        {
          "role": "header",
          "style": {
            "fill": {
              "type": "image",
              "URL": "bundle://header.jpg",
              "fillMode": "cover",
              "verticalAlignment": "top",
              "horizontalAlignment": "center"
            }
          },
          "layout": {
            "minimumHeight": "75cw"
          },
          "components": [
            {
              "role": "title",
              "text": "Article Title",
              "anchor": {
                "targetAnchorPosition": "center"
              },
              "textStyle": {
                "textAlignment": "center"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `section` for this component.

  **Allowed Values**: `section`
- `additions` ([ComponentLink]): An array of `ComponentLink` objects you can use to create a ComponentLink, allowing a link to anywhere in News.

  You can add a link to a [`Container`](./container.md) component to make the entire component tappable. Any links used in its child components are not interactable.
- `allowAutoplacedAds` (boolean): A Boolean value that allows the placement of ad banners between components. Nested components inherit the value of the outermost container that explicitly sets `allowAutoplacedAds`. The default value is `true`.

  **Default**: `true`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `components` ([Component]): An array of components to display as child components. Child components are positioned and rendered relative to their parent component.
- `conditional` ((ConditionalSection | [ConditionalSection])): An instance or array of section properties that can be applied conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalSection`, `[ConditionalSection]`
- `contentDisplay` ((CollectionDisplay | HorizontalStackDisplay | string("none"))): An object that defines how to position child components within this `section` component. A [`HorizontalStackDisplay`](./horizontalstackdisplay.md), for example, allows for displaying child components side by side.

  In versions of News prior to iOS 11, child components are positioned as if `contentDisplay` were not defined.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `CollectionDisplay`, `HorizontalStackDisplay`, `string("none")`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If used, this `identifier` must be unique across the entire document. You will need an `identifier` for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If `layout` is not defined, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `scene` (Scene): A set of animations applied to any `header` component that is a child of this section.
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Container](./container.md)

## See Also

### Related Documentation
- [About Containers](../AppleNews/about-containers.md)
  Learn the basic Apple News Format container concepts required for the three advanced tutorials.
- [Adding Parallax Behavior](../AppleNews/adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
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
- [type PublisherArticleIdentifier](./publisherarticleidentifier.md)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/section)*