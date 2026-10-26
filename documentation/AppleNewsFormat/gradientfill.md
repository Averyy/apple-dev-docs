# GradientFill

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The properties all gradient fill types share.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object GradientFill
```

## Mentions

- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)

#### Discussion

This is an abstract definition. Don’t use this object type directly; use only the object that extends it, such as [`LinearGradientFill`](./lineargradientfill.md).

You can use this object in [`ComponentStyle`](./componentstyle.md).

## Properties

- `colorStops` ([ColorStop]) *(required)*: An array of color stops. Each stop sets a color and location along the gradient.

  Provide at least 2 `colorStop` items.
- `type` (string) *(required)*: The type of gradient; for example `linear_gradient`.
- `attachment` (string): A string that indicates how `fill` behaves when a person scrolls.

  Valid values:

  - `scroll` (default). The fill scrolls along with its component.
  - `fixed`. The fill stays at a fixed position within the viewport.

  **Default**: `scroll`; **Allowed Values**: `fixed`, `scroll`

## Relationships

### Inherits From
- [Fill](./fill.md)
### Inherited By
- [LinearGradientFill](./lineargradientfill.md)

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
- [object Fill](./fill.md)
  The object for setting a fill type and attachment for a component’s background fill.
- [object ColorStop](./colorstop.md)
  The object for specifying the color and location for a color stop in a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/gradientfill)*