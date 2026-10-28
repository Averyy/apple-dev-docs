# LinkButton

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for opening a link in a button.

**Availability**:
- Apple News Format 1.11+

## Declaration

```
object LinkButton
```

## Discussion

Use the `LinkButton` component to display a button with a link. The link opens when someone interacts with the button. You can place the `LinkButton` anywhere in the document and style it using [`ComponentStyle`](./componentstyle.md) and [`ComponentTextStyle`](./componenttextstyle.md) properties.

### Example

```json
{
  "components": [
    {
      "role": "link_button",
      "URL": "http://apple.com",
      "text": "Read More",
      "style": {
        "backgroundColor": "#DDD",
        "mask": {
          "type": "corners",
          "radius": 25
        }
      },
      "layout": {
        "padding": 10
      }
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `link_button` for this component.

  **Allowed Values**: `link_button`
- `URL` (SupportedURLs) *(required)*: The URL to open when a person interacts with the range of text specified in the addition.
- `accessibilityLabel` (string): A string that’s read to the user when you enable certain accessibility functionalities.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  To remove a previously set condition, use `none`.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalButton | [ConditionalButton])): An instance or array of button properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalButton`, `[ConditionalButton]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): A unique identifier for this component. If you use an identifier, it must be unique across the entire document. An identifier is required if you want to anchor other components to this component.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` that’s defined at the top level of the document.

  If you don’t define layout, Apple News bases the size and position on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyl`e object that defines the appearance of this component, or a string reference to a `ComponentStyle` that’s defined at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`
- `text` (string): The text, styled according to the `textStyle` definition.
- `textStyle` ((ComponentTextStyle | string)): An inline `ComponentTextStyle` object that contains styling information, or a string reference to a `ComponentTextStyle` object that’s defined at the top level of the document.

  **Allowed Types**: `ComponentTextStyle`, `string`

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
- [object FlexibleSpacer](./flexiblespacer.md)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](./divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](./articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](./supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/linkbutton)*