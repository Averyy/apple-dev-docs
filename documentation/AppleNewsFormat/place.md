# Place

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a map with a specific point of interest.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Place
```

#### Discussion

Use the `Place` component to display a map with a single point of interest. The map automatically centers the point of interest based on the `latitude` and `longitude` locations you provide. If you want to display multiple pins on a map, use the [`Map`](./map.md) component.

##### Example

```json
{
  "components": [
    {
      "role": "title",
      "text": "Maps"
    },
    {
      "role": "body",
      "text": "With turn-by-turn spoken directions, interactive 3D views, proactive suggestions, lane guidance, and more, Maps gets you where you need to go."
    },
    {
      "role": "heading2",
      "text": "Place Heading"
    },
    {
      "role": "place",
      "mapType": "hybrid",
      "latitude": 35.065908,
      "longitude": -109.781623
    }
  ]
}
```

## Properties

- `latitude` (number) *(required)*: The latitude of the place’s location.
- `longitude` (number) *(required)*: The longitude of the place’s location.
- `role` (string) *(required)*: Always `place` for this component.

  **Allowed Values**: `place`
- `accessibilityCaption` (string): The caption that describes a place. The text is used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `caption` (string): A string that describes the place depicted on the map. For example, if the `latitude` and `longitude` point to a park, the `caption` should contain the name of the park. The caption is displayed in the full screen version of the map, and the text is used by VoiceOver if `accessibilityCaption` is not provided. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility.
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an identifier for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the role of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `mapType` (string): A string that defines the type of map to display by default.

  Valid values:

  - `standard` (default). Displays the standard map.
  - `hybrid`. Displays a map with satellite imagery with standard features overlaid.
  - `satellite`. Displays satellite imagery only.

  **Default**: `standard`; **Allowed Values**: `standard`, `hybrid`, `satellite`
- `span` (MapSpan): The object for defining the visible area of a map, relative to its center. A `span` is defined in deltas for `latitude` and `longitude`.
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Location
- [object Map](./map.md)
  The component for adding a map.
- [object MapItem](./mapitem.md)
  An object used in a map component for specifying the location of a map pin.
- [object MapSpan](./mapspan.md)
  An object used in a map or place component for defining the visible area of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/place)*