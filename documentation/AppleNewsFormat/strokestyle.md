# StrokeStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the color, width, and style of a border or divider.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object StrokeStyle
```

#### Discussion

You can specify the color, width, and style (solid, dashed, or dotted) of a stroke. Such strokes have many uses, including component borders and divider components.

You can use this object in [`Border`](./border.md), [`Divider`](./divider.md), [`TableRowStyle`](./tablerowstyle.md), [`TableColumnStyle`](./tablecolumnstyle.md), [`ConditionalTableRowStyle`](./conditionaltablerowstyle.md), and [`ConditionalTableColumnStyle`](./conditionaltablecolumnstyle.md).

##### Example

```json
{
  "components": [
    {
      "role": "divider",
      "stroke": {
        "color": "black",
        "width": 1
      }
    }
  ]
}
```

## Properties

- `color` (Color): The stroke color.
- `style` (string): Defines the style of the stroke. Valid values:

  - `solid` (default): A solid stroke _______
  - `dashed`: A dashed stroke – – – – –
  - `dotted`: A dotted stroke ••••••••

  **Default**: `solid`; **Allowed Values**: `solid`, `dashed`, `dotted`
- `width` ((SupportedUnits | number)): The width of the stroke line that can be either a number in points, or a string according to [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Default**: `1`; **Allowed Types**: `SupportedUnits`, `number`

## See Also

### Related Documentation
- [Adding a Divider](../AppleNews/adding-a-divider.md)
  Create a horizontal, styled divider that extends to the right edge of the display.
### Component Style Basics
- [Defining a Component Style](../AppleNews/defining-a-component-style.md)
  Set style options for the components in your article.
- [object ComponentStyle](./componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object CornerMask](./cornermask.md)
  The object for creating rounded corners.
- [object Border](./border.md)
  The object for setting borders for component sides or tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/strokestyle)*