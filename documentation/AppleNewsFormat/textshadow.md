# TextShadow

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for creating a text shadow.

**Availability**:
- Apple News Format 1.10+

## Declaration

```
object TextShadow
```

## Discussion

Use a `TextShadow` object to define a shadow that Apple News can apply to characters as part of a [`TextStyle`](./textstyle.md).

### Example

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      …
      "textShadow": {
        "radius": 5,
        "opacity": 0.7,
        "color": "#333",
        "offset": {
          "x": -2,
          "y": 2
        }
      },
      "fontSize": 30
    }
  }
}
```

## Properties

- `color` (Color) *(required)*: The text shadow color.
- `radius` (number) *(required)*: The shadow’s radius as a value, in points, between `0` and `100`.

  **Minimum**: `0`; **Maximum**: `100`
- `offset` (TextShadowOffset): The shadow’s offset.
- `opacity` (float): The opacity of the shadow as a value between `0` and `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`

## See Also

### Text Effects
- [object TextShadowOffset](./textshadowoffset.md)
  The object for setting an offset value to use with a text shadow.
- [object TextStrokeStyle](./textstrokestyle.md)
  The object for defining the stroke to use for an outline on text.
- [object TextDecoration](./textdecoration.md)
  The object for defining color for text underline or strikethrough.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/textshadow)*