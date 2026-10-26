# BannerAdvertisement

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a full-width banner ad.

**Availability**:
- Apple News Format 1.7+ - Deprecated in 1.17

> **Deprecated**: Manual ads are no longer supported in Apple News. Use [`AutoPlacement`](./autoplacement.md) instead.

## Declaration

```
object BannerAdvertisement
```

## Mentions

- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)

#### Discussion

`The BannerAdvertisement` object spans the full width of your display. A range of different banner heights are available depending on the availability of advertising content through Advertising Platforms.(An advertisement can appear inside a `Container` component only if the container is full-width.)

Keep these points in mind when including a banner advertisement in your article:

- Do not apply animations, scenes, or behaviors to advertisement components.
- Advertisements placed on the first “screen” of the article will not be rendered—with one exception: short articles that are only one screen can render one ad.
- The dimensions of visible areas vary with screen size and text size.
- If two or more advertising components are placed on the same screen, only the first will be rendered.
- Do not position advertising components immediately before or after images.
- For the `bannerType` property, choose only one value. The default value, `any`, allows any standard, double-height or large-banner advertisement to serve within a specific placement, based on availability.

For information about medium, fixed-sized advertisements, see [`MediumRectangleAdvertisement`](./mediumrectangleadvertisement.md).

##### Example

```json
{
  "components": [
    {
      "role": "banner_advertisement",
      "bannerType": "standard"
    }
  ]
}
```

## Properties

- `role` (string) *(required)* *(deprecated)*: Always `banner_advertisement` for this component.

  **Allowed Values**: `banner_advertisement`
- `anchor` (Anchor) *(deprecated)*: An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))) *(deprecated)*: An object that defines an animation the component applies

  Use the none value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `bannerType` (string) *(deprecated)*: The type of banner to show.

  **Allowed Values**: `any`, `standard`, `double_height`, `large`
- `behavior` ((Behavior | string("none"))) *(deprecated)*: An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])) *(deprecated)*: An instance or array of component properties that can be applied conditionally, and the conditions that cause them to be applied.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean) *(deprecated)*: A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string) *(deprecated)*: An optional unique identifier for this component. If used, this `identifier` must be unique across the entire document. You will need an `identifier` for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)) *(deprecated)*: An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If `layout` is not defined, size and position will be based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))) *(deprecated)*: An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Advertisements
- [object MediumRectangleAdvertisement](./mediumrectangleadvertisement.md)
  The component for adding a medium, fixed-size rectangle ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/banneradvertisement)*