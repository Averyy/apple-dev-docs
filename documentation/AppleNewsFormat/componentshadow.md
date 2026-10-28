# ComponentShadow

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for creating a component shadow.

**Availability**:
- Apple News Format 1.10+

## Declaration

```
object ComponentShadow
```

## Discussion

Use a `ComponentShadow` object to define a shadow that you can apply to components as part of [`ComponentStyle`](./componentstyle.md).

### Example

```json
{
  "componentStyles": {
    "exampleStyle": {
      "backgroundColor": "#FFF",
      "shadow": {
        "color": "#33333350",
        "opacity": 0.33,
        "radius": "10cw",
        "offset": {
          "x": 2,
          "y": "10cw"
        }
      }
    }
  }
}
```

## Properties

- `color` (Color) *(required)*: The component shadow color.
- `radius` ((SupportedUnits | number)) *(required)*: The shadow’s radius.

  **Default**: `0`; **Allowed Types**: `SupportedUnits`, `number`
- `offset` (ComponentShadowOffset): The shadow’s offset.
- `opacity` (float): The opacity of the shadow as a value between `0` and `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`

## See Also

### Component Effects
- [object ComponentShadowOffset](./componentshadowoffset.md)
  The object for setting an offset value to use with a component shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/componentshadow)*