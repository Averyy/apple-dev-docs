# TextShadowOffset

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for setting an offset value to use with a text shadow.

**Availability**:
- Apple News Format 1.10+

## Declaration

```
object TextShadowOffset
```

#### Discussion

Use the `Offset` object to define an offset. A positive `x` value moves the content to the left, and a negative `x` value moves the content to the right. A positive `y` value moves the content up, and a negative `y` value moves the content down.

##### Example

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

- `x` (number) *(required)*: The `x` offset, as a value between `-50.0` and `50.0`. Implementation is device dependent.

  **Minimum**: `-50`; **Maximum**: `50`
- `y` (number) *(required)*: The `y` offset, as a value between `-50.0` and `50.0`. Implementation is device dependent.

  **Minimum**: `-50`; **Maximum**: `50`

## See Also

### Text Effects
- [object TextShadow](./textshadow.md)
  The object for creating a text shadow.
- [object TextStrokeStyle](./textstrokestyle.md)
  The object for defining the stroke to use for an outline on text.
- [object TextDecoration](./textdecoration.md)
  The object for defining color for text underline or strikethrough.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/textshadowoffset)*