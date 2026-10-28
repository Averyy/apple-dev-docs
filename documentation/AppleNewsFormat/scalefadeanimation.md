# ScaleFadeAnimation

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The animation in which a component scales up and fades into view.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ScaleFadeAnimation
```

## Mentions

- [About Component Animations](../AppleNews/about-component-animations.md)

## Discussion

With this animation type the component appears by getting larger and fading from transparent to opaque. Initially, the component is scaled down and at least partially transparent, but, upon entering the user’s view, the component scales up to its actual size in the layout and fades in to be completely opaque as shown in [this video](https://developer.apple.com/apple-news/videos/scale-fade.mp4).

### Example

```json
{
  "components": [
    {
      "role": "figure",
      "URL": "bundle://figure.jpg",
      "animation": {
        "type": "scale_fade",
        "initialAlpha": 0.5,
        "initialScale": 0.75
      }
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This animation always has the type `scale_fade`.

  **Allowed Values**: `scale_fade`
- `initialAlpha` (number): The initial transparency of the component (and the animation). Set `initialAlpha` to a value between `0` (completely transparent) and `1` (completely visible).

  **Default**: `0.3`; **Minimum**: `0`; **Maximum**: `1`
- `initialScale` (number): The initial scale of the component (and the animation). Set `initialScale` to a value between `0` (completely scaled down) and `1` (the component’s original size).

  **Default**: `0.75`; **Minimum**: `0`; **Maximum**: `1`
- `userControllable` (boolean): Indicates whether the animation happens in response to user action `(true`) or happens automatically (`false`).

  **Default**: `false`

## Relationships

### Inherits From
- [ComponentAnimation](./componentanimation.md)

## See Also

### Related Documentation
- [Adding Animations](../AppleNews/adding-animations.md)
  Use animations to affect how parts of your article come into view the first time they appear.
### Animations
- [About Component Animations](../AppleNews/about-component-animations.md)
  Learn how to affect the way in which components come into view.
- [object ComponentAnimation](./componentanimation.md)
  Properties that all types of animations share.
- [object AppearAnimation](./appearanimation.md)
  An animation type whereby a component appears on the screen.
- [object FadeInAnimation](./fadeinanimation.md)
  The animation whereby a component fades into view.
- [object MoveInAnimation](./moveinanimation.md)
  The animation whereby a component moves in from the side of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/scalefadeanimation)*