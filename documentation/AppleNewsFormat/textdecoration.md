# TextDecoration

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining color for text underline or strikethrough.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object TextDecoration
```

## Discussion

Use the `TextDecoration` object to define a stroke for strikethrough or underline.

You can use this object in [`TextStyle`](./textstyle.md) and [`ComponentTextStyle`](./componenttextstyle.md).

### Example

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      …
      "strikethrough": {
        "color": "#FFC800"
      },
      "underline": {
        "color": "#FFC800"
      }
    }
  }
}
```

## Properties

- `color` (Color): Color of the stroke. If you omit this property, Apple News uses the content’s stroke color from the text color  for underline or strikethrough.

## See Also

### Text Effects
- [object TextShadow](./textshadow.md)
  The object for creating a text shadow.
- [object TextShadowOffset](./textshadowoffset.md)
  The object for setting an offset value to use with a text shadow.
- [object TextStrokeStyle](./textstrokestyle.md)
  The object for defining the stroke to use for an outline on text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/textdecoration)*