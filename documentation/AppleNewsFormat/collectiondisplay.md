# CollectionDisplay

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

An object used in any container component type to define how the collection of child components is presented.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object CollectionDisplay
```

## Discussion

This image shows a `CollectionDisplay` with a `distribution` property of `wide`.

![Screenshot of three images with whitespace equally distributed between them to fill the width of the available space.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-4099199@2x.png)

This image shows a `CollectionDisplay` with a `distribution` property of `narrow`.

![Screenshot of three images next to each other with a defined amount of whitespace between them.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-4099200@2x.png)

This object can be used in [`Header`](./header.md), [`Container`](./container.md), [`Section`](./section.md), [`Chapter`](./chapter.md), [`Aside`](./aside.md), and [`ArticleLink`](./articlelink.md).

### Example

```json
{
  "components": [
    {
      "role": "container",
      "contentDisplay": {
        "type": "collection",
        "minimumWidth": 150,
        "gutter": "15",
        "rowSpacing": "30",
        "distribution": "wide"
      },
      "components": [
        {
          "role": "image",
          "URL": "bundle://gallery-02.jpg",
          "caption": "Coyotes are also seen in cities more often."
        },
        {
          "role": "image",
          "URL": "bundle://gallery-03.jpg",
          "explicitContent": true
        }
      ]
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: Always `collection` for this object.

  **Allowed Values**: `collection`
- `alignment` (string): A string that defines how components are aligned within their rows. This is especially visible when `distribution` is set to `narrow`.

  Valid values:

  - `left` (default). The group of components is left-aligned within the available space. Remaining space is added at the right of the row.
  - `center`. The group of components is centered within the available space. Remaining space is added at both sides of the row.
  - `right`. The group of components is right-aligned within the available space. Remaining space is added at the left of the row.

  **Default**: `left`; **Allowed Values**: `left`, `center`, `right`
- `distribution` (string): A string that defines how components should be distributed horizontally in a row.

  Valid values:

  - `wide` (default). Components are spread across the full width of the component. Whitespace is equally distributed into the space between components.
  - `narrow`. Components are placed next to each other as closely as possible, separated by the width defined in the `gutter` property. Any remaining whitespace is applied to the left and right of the collection.

  **Default**: `wide`; **Allowed Values**: `wide`, `narrow`
- `gutter` ((SupportedUnits | number)): A number in points or a string referring to a supported unit of measure defining the vertical gutter between components.

  See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  This value cannot be negative.

  **Default**: `0`; **Allowed Types**: `SupportedUnits`, `number`
- `maximumWidth` ((SupportedUnits | number)): A number in points or a string referring to a supported unit of measure defining the maximum width of each child component inside the collection.

  If the `maximumWidth` is smaller than the `minimumWidth`, the `minimumWidth` is used.

  If no `maximumWidth` is provided, a default of `100cw` is used.

  See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumWidth` ((SupportedUnits | number)): A number in points or a string referring to a supported unit of measure defining the minimum width of each child component inside the collection.

  `minimumWidth` should not exceed the `maximumWidth` value. A child component will never be larger than the width of its parent. If no `minimumWidth` has been provided, News attempts to decide the optimal size for each child component based on its contents. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  This value cannot be negative.

  **Allowed Types**: `SupportedUnits`, `number`
- `rowSpacing` ((SupportedUnits | number)): A number in points or a string referring to a supported unit of measure defining the horizontal spacing between rows. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  This value cannot be negative.

  **Default**: `0`; **Allowed Types**: `SupportedUnits`, `number`
- `variableSizing` (boolean): A Boolean value that defines whether the components’ area is allowed to be sized differently per row.

  If `true`, individual rows might have different widths for their components to make use of the entire available width.

  If `false`, all components in the collection will have the same width.

  **Default**: `false`
- `widows` (string): A string that defines the approach to prevent the collection from having component widows.

  Valid values:

  - `equalize`. Every row contains an equal amount of components. When provided with an uneven amount of components, each row consists of 1 component.
  - `optimize` (default). Looks for the most optimal distribution of components, but allows each row to have a different amount of components.
  - `allow`. Each row contains as many components as it can fit or are available. Allows for widows to occur.

  **Default**: `optimize`; **Allowed Values**: `equalize`, `optimize`, `allow`

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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/collectiondisplay)*