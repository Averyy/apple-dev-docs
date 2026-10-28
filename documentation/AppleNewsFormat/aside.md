# Aside

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for setting apart content that is not directly related to the article, such as promotional content.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Aside
```

## Mentions

- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)
- [Nesting Components in an Article](../AppleNews/nesting-components-in-an-article.md)
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)

## Discussion

Use an `aside` component to hold information not directly related to your article. Use an `aside` to help Siri make the most informed content recommendations to people using Apple News and to provide better accuracy for placing your content within feeds, such as the Today feed, channel feeds, and topic feeds.

When News recommends content, it ignores any content in the `aside` component, so you can put content there that is not directly related to the article, such as promotional content, links to other articles, or author biographies.

### Example

```json
{
  "components": [
    {
      "role": "aside",
      "components": [
        {
          "role": "body",
          "text": "<a href=\"https://www.apple.com/newsroom/2017/06/swift-playgrounds-expands-coding-education-to-robots-drones-and-musical-instruments/\">Swift Playgrounds expands coding education to robots, drones and musical instruments</a>",
          "format": "html"
        }
      ]
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `aside` for this component.

  **Allowed Values**: `aside`
- `additions` ([ComponentLink]): An array of `ComponentLink` objects you can use to create a ComponentLink, allowing a link to anywhere in News.

  You can add a link to a [`Container`](./container.md) component to make the entire component tappable. Any links used in its child components are not interactable.
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
- `contentDisplay` ((CollectionDisplay | HorizontalStackDisplay | string("none"))): An object that defines how to position child components within this `aside` component. A [`HorizontalStackDisplay`](./horizontalstackdisplay.md), for example, allows for displaying child components side by side.

  In versions of News prior to iOS 11, child components are positioned as if `contentDisplay` were not defined.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `CollectionDisplay`, `HorizontalStackDisplay`, `string("none")`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If used, this `identifier` must be unique across the entire document. You will need an `identifier` for your component if you want to anchor other components to it.
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

### Related Documentation
- [About Containers](../AppleNews/about-containers.md)
  Learn the basic Apple News Format container concepts required for the three advanced tutorials.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/aside)*