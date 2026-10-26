# Border

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for setting borders for component sides or tables.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Border
```

#### Discussion

The `Border` object defines a component or a table cell border, including the border stroke style. The border style is the same for all sides of the component or table cell. Use a value of `false` for any side of a border that you don’t want to show.

You can use this object in [`ComponentStyle`](./componentstyle.md), [`TableCellStyle`](./tablecellstyle.md), and [`ConditionalTableCellStyle`](./conditionaltablecellstyle.md).

##### Example

```json
{
  "componentStyles": {
    "exampleComponentStyle": {
      "border": {
        "all": {
          "width": 1,
          "color": "#ddd"
        },
        "left": false,
        "right": false
      }
    }
  }
}
```

## Properties

- `all` (StrokeStyle): Defines the stroke properties of the border. You can’t set stroke properties for each side; you can only disable or enable the border for each side.
- `bottom` (boolean): Indicates whether Apple News applies the border to the bottom.

  **Default**: `true`
- `left` (boolean): Indicates whether Apple News applies the border to the left side.

  **Default**: `true`
- `right` (boolean): Indicates whether Apple News applies the border to the right side.

  **Default**: `true`
- `top` (boolean): Indicates whether Apple News applies the border to the top.

  **Default**: `true`

## See Also

### Component Style Basics
- [Defining a Component Style](../AppleNews/defining-a-component-style.md)
  Set style options for the components in your article.
- [object ComponentStyle](./componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object CornerMask](./cornermask.md)
  The object for creating rounded corners.
- [object StrokeStyle](./strokestyle.md)
  The object for defining the color, width, and style of a border or divider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/border)*