# MoveInAnimation

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The animation whereby a component moves in from the side of the screen.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object MoveInAnimation
```

## Mentions

- [About Component Animations](../AppleNews/about-component-animations.md)

## Discussion

With this animation type the component moves into view from the left or right side of the screen. Initially, the component is out of view as shown in [this video](https://developer.apple.com/apple-news/videos/move-in.mp4).

You can configure a preferred starting position, but the position is not guaranteed. For example, if another component is blocking the preferred position, the `MoveInAnimation` attempts to start from the opposite side. If both sides are covered by other components, Apple News doesn’t apply the `MoveInAnimation`.

### Example

```json
{
  "components": [
    {
      "role": "heading1",
      "text": "2. Unbeatable Heat"
    },
    {
      "role": "figure",
      "URL": "bundle://figure.jpg",
      "animation": {
        "type": "move_in",
        "preferredStartingPosition": "left"
      }
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This animation always has the type `move_in`.

  **Allowed Values**: `move_in`
- `preferredStartingPosition` (string): Indicates which side of the screen is the starting point of the animation. Valid values:

  - `left`: Move the component in from the left side of the screen.
  - `right`: Move the component in from the right side of the screen.

  By default, the animation starts on the side that’s closest to the component.

  **Allowed Values**: `left`, `right`
- `userControllable` (boolean): Indicates whether the animation happens in response to user action (`true`) or happens automatically (`false`).

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
- [object ScaleFadeAnimation](./scalefadeanimation.md)
  The animation in which a component scales up and fades into view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/moveinanimation)*