# TextStrokeStyle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the stroke to use for an outline on text.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TextStrokeStyle
```

#### Discussion

Use the `TextStrokeStyle` object to define a text outline.

You can use this object in [`TextStyle`](./textstyle.md) and [`ComponentTextStyle`](./componenttextstyle.md).

##### Example

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      …
      "stroke": {
        "color": "#000",
        "width": 3
      },
      "textColor": "#FFF",
      "fontSize": 30
    }
  }
}
```

## Properties

- `color` (Color): The stroke color.
- `width` (integer): Width of the stroke as a percentage relative to the font size.

  **Default**: `3`; **Minimum**: `0`

## See Also

### Text Effects
- [object TextShadow](./textshadow.md)
  The object for creating a text shadow.
- [object TextShadowOffset](./textshadowoffset.md)
  The object for setting an offset value to use with a text shadow.
- [object TextDecoration](./textdecoration.md)
  The object for defining color for text underline or strikethrough.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/textstrokestyle)*