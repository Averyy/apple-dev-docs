# CornerMask

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for creating rounded corners.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object CornerMask
```

## Discussion

Use the `CornerMas`k object to specify the corner radius for a component, and enable or disable the effect on a per-corner basis (`topRight`, `topLeft`, `bottomRight`, and `bottomLeft`). All corners are enabled by default. When you specify a border alongside a corner radius, the borders take into account the radius of the mask and are drawn within the unmasked area of the component.

You can use this object in [`ComponentStyle`](./componentstyle.md).

### Example

```json
{
  "components": [
    {
      "role": "container",
      "style": "exampleComponentStyle",
      "components": [
        {
          "role": "title",
          "text": "Drought"
        }
      ]
    }
  ],
  "componentStyles": {
    "exampleComponentStyle": {
      "backgroundColor": "#FF0000",
      "mask": {
        "type": "corners",
        "radius": 25,
        "topRight": false,
        "bottomRight": false
      }
    }
  }
}
```

## Properties

- `bottomLeft` (boolean): A Boolean that indicates whether the bottom-left corner is masked.

  **Default**: `true`
- `bottomRight` (boolean): A Boolean that indicates whether the bottom-right corner is masked.

  **Default**: `true`
- `curve` (string): The type of curve to use for rendering the mask’s corner.

  Valid values:

  - `circular`. Creates a rounded corner.
  - `continuous`. Creates a continuous corner.

  **Default**: `circular`; **Allowed Values**: `circular`, `continuous`
- `radius` ((SupportedUnits | number)): A supported unit or number that describes the radius of the corners in points. Corner radius can’t exceed half the component width or height, whichever is smaller.

  **Allowed Types**: `SupportedUnits`, `number`
- `topLeft` (boolean): A Boolean that indicates whether the top-left corner is masked.

  **Default**: `true`
- `topRight` (boolean): A Boolean that indicates whether the top-right corner is masked.

  **Default**: `true`
- `type` (string): The type of mask. The value is always `corners`.

  **Allowed Values**: `corners`

## See Also

### Component Style Basics
- [Defining a Component Style](../AppleNews/defining-a-component-style.md)
  Set style options for the components in your article.
- [object ComponentStyle](./componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object Border](./border.md)
  The object for setting borders for component sides or tables.
- [object StrokeStyle](./strokestyle.md)
  The object for defining the color, width, and style of a border or divider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/cornermask)*