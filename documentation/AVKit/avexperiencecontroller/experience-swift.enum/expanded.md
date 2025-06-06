# AVExperienceController.Experience.expanded

**Framework**: Avkit  
**Kind**: case

An experience where the system places the video outside of its original container.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case expanded
```

#### Discussion

Transition to this experience to get the appropriate expanded experience for the platform.

It’s valid to transition to this experience even when the original container isn’t in a view hierarchy. In this case, you must specify a [`fallbackPlacement`](avexperiencecontroller/expandedconfiguration/fallbackplacement.md) or the transition result is [`AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)`](avexperiencecontroller/transitioncontext/transitionresult/reversed(reason:).md).

> **Note**: This experience to is analogous to a player view controller’s fullscreen state.

## See Also

- [AVExperienceController.Experience.embedded](avexperiencecontroller/experience-swift.enum/embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.multiview](avexperiencecontroller/experience-swift.enum/multiview.md)
  An experience where multiple videos play together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVKit/avexperiencecontroller/experience-swift.enum/expanded)*