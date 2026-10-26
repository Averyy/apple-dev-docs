# Fill

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for setting a fill type and attachment for a component’s background fill.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Fill
```

## Mentions

- [Nesting Components in an Article](../AppleNews/nesting-components-in-an-article.md)

#### Discussion

This is an abstract definition. Don’t use this object type directly; use only the objects that extend `Fill,` for example [`GradientFill`](./gradientfill.md), [`ImageFill`](./imagefill.md), `and` [`VideoFill`](./videofill.md).

## Properties

- `type` (string) *(required)*: The type of fill to apply.

  **Allowed Values**: `linear_gradient`, `image`, `repeatable_image`, `video`
- `attachment` (string): Indicates how the fill behaves when a person scrolls.

  Valid values:

  - `scroll` (default): The fill scrolls along with its component.
  - `fixed`: The fill stays at a fixed position within the viewport.

  **Default**: `scroll`; **Allowed Values**: `fixed`, `scroll`

## Relationships

### Inherited By
- [GradientFill](./gradientfill.md)
- [ImageFill](./imagefill.md)
- [RepeatableImageFill](./repeatableimagefill.md)
- [VideoFill](./videofill.md)

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
- [object LinearGradientFill](./lineargradientfill.md)
  The object for displaying a linear gradient as a component background.
- [object GradientFill](./gradientfill.md)
  The properties all gradient fill types share.
- [object ColorStop](./colorstop.md)
  The object for specifying the color and location for a color stop in a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/fill)*