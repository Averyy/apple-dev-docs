# AVExperienceController.Experience.embedded

**Framework**: AVKit  
**Kind**: case

An experience where the video embeds within its original container.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case embedded
```

#### Discussion

This experience is the starting state and is valid on all platforms. You may embed video in the original container even if that container isn’t visible or not in the view hierarchy. It’s valid to transition to this experience from any other experience, even when the player view controller isn’t in the view hierarchy.

It’s the app’s responsibility to correctly manage the player view controller’s view lifecycle.

> **Note**: This experience to is analogous to a player view controller’s inline state.

This experience to is analogous to a player view controller’s inline state.

## See Also

- [AVExperienceController.Experience.expanded](avexperiencecontroller/experience-swift.enum/expanded.md)
  An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](avexperiencecontroller/experience-swift.enum/multiview.md)
  An experience where multiple videos play together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/embedded)*