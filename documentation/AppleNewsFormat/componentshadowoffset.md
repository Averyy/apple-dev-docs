# ComponentShadowOffset

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for setting an offset value to use with a component shadow.

**Availability**:
- Apple News Format 1.10+

## Declaration

```
object ComponentShadowOffset
```

#### Discussion

Use the `ComponentShadowOffset` object to define an offset. A positive `x` value moves the shadow to the right, and a negative `x` value moves the shadow to the left. A positive `y` value moves the shadow down, and a negative `y` value moves the shadow up.

##### Example

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

- `x` ((SupportedUnits | number)): The `x` offset, as a value in [`SupportedUnits`](./supportedunits.md). Implementation is device dependent.

  **Allowed Types**: `SupportedUnits`, `number`
- `y` ((SupportedUnits | number)): The `y` offset, as a value in [`SupportedUnits`](./supportedunits.md). Implementation is device dependent.

  **Allowed Types**: `SupportedUnits`, `number`

## See Also

### Component Effects
- [object ComponentShadow](./componentshadow.md)
  The object for creating a component shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/componentshadowoffset)*