# LinearGradientFill

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for displaying a linear gradient as a component background.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object LinearGradientFill
```

## Mentions

- [Applying a Background to a Component](../AppleNews/applying-a-background-to-a-component.md)

## Discussion

Use the `LinearGradientFill` object to cause the background for a component to be a linear gradient between two (or more) colors. Specify the colors you want to use and a percentage for each color along with an angle for the gradient and the behavior of the background when the person scrolls.

You can use this object in [`ComponentStyle`](./componentstyle.md).

### Example

```json
{
  "components": [
    {
      "role": "container",
      "style": "exampleStyle",
      "layout": {
        "ignoreDocumentMargin": true,
        "minimumHeight": 150
      },
      "components": [
        {
          "role": "title",
          "text": "Season Preview: Nobody Saw This Coming",
          "anchor": {
            "targetAnchorPosition": "center"
          }
        }
      ]
    }
  ],
  "componentStyles": {
    "exampleStyle": {
      "fill": {
        "type": "linear_gradient",
        "angle": 180,
        "colorStops": [
          {
            "color": "#00000000"
          },
          {
            "color": "#FFFFFF"
          }
        ]
      }
    }
  }
}
```

## Properties

- `colorStops` ([ColorStop]) *(required)*: An array of color stops. Each stop sets a color and percentage.

  Provide at least 2 `colorStop` items.
- `type` (string) *(required)*: Always `linear_gradient` for this object.

  **Allowed Values**: `linear_gradient`
- `angle` (number): The angle of the gradient fill, in degrees. Use the angle to set the direction of the gradient. For example, a value of `180` defines a gradient that changes color from top to bottom. An angle of `90` defines a gradient that changes color from left to right.

  If you omit `angle`, Apple News uses an angle of `180` (top to bottom).

  **Default**: `180`

## Relationships

### Inherits From
- [GradientFill](./gradientfill.md)

## See Also

### Backgrounds for Components
- [Applying a Background to a Component](../AppleNews/applying-a-background-to-a-component.md)
  Change the appearance of the backgrounds in your article.
- [object ImageFill](./imagefill.md)
  The object for adding an image background fill to a component.
- [object RepeatableImageFill](./repeatableimagefill.md)
  The object for adding a background image that Apple News can repeat.
- [object VideoFill](./videofill.md)
  The object for adding a video background fill to a component.
- [object GradientFill](./gradientfill.md)
  The properties all gradient fill types share.
- [object Fill](./fill.md)
  The object for setting a fill type and attachment for a component’s background fill.
- [object ColorStop](./colorstop.md)
  The object for specifying the color and location for a color stop in a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/lineargradientfill)*