# AVExperienceController.Experience.expanded

**Framework**: AVKit  
**Kind**: case  
**Role**: Case

An experience where the system places the video outside of its original container.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case expanded
```

#### Discussion

Transition to this experience to get the appropriate expanded experience for the platform.

It’s valid to transition to this experience even when the original container isn’t in a view hierarchy. In this case, you must specify a [`fallbackPlacement`](../expandedconfiguration/fallbackplacement.md) or the transition result is [`AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)`](../transitioncontext/transitionresult/reversed%28reason%29.md).

> **Note**: This experience to is analogous to a player view controller’s fullscreen state.

## See Also

### Supported experiences
- [AVExperienceController.Experience.embedded](./embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.multiview](./multiview.md)
  An experience where multiple videos play together.
- [AVExperienceController.Experience.immersive](./immersive.md)
  Indicates an experience in which the video extends beyond the app window boundaries/container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/expanded)*