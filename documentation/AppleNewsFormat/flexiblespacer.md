# FlexibleSpacer

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for redistributing empty space inside a horizontal stack collection.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object FlexibleSpacer
```

## Mentions

- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)

## Discussion

Use the `FlexibleSpacer` object to redistribute the extra space between child components in a [`HorizontalStackDisplay`](./horizontalstackdisplay.md).  Otherwise, if you have two child components in a horizontal stack that don’t use up all of the space, the extra space is always on the right side. The `FlexibleSpacer` object does not have an intrinsic size, but is sized to fit any remaining width, and to fit the height of the parent container. The object is ignored when used outside of the `HorizontalStackDisplay` context.

### Example

```json
{
  "components": [
    {
      "role": "container",
      "components": [
        {
          "role": "image",
          "URL": "bundle://summer.jpg",
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
          "URL": "bundle://winter.jpg",
          "layout": {
            "minimumWidth": "35cw",
            "maximumWidth": "35cw"
          }
        }
      ],
      "contentDisplay": {
        "type": "horizontal_stack"
      }
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `spacer` for this object.

  **Allowed Values**: `spacer`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that can be applied conditionally,  and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If used, this identifier must be unique across the entire document. You will need an identifier for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  The width of the spacer is determined automatically based on any remaining horizontal space, and the height is that of the parent container. Any top or bottom margins specified on a spacer component’s layout decreases the height of the layout within the parent container.

  All properties of `ComponentLayout` object are supported except `minimumHeight` and `minimumWidth`.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

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
- [object Divider](./divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](./articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](./supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.
- [type PublisherArticleIdentifier](./publisherarticleidentifier.md)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/flexiblespacer)*