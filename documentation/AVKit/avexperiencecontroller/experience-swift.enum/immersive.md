# AVExperienceController.Experience.immersive

**Framework**: AVKit  
**Kind**: case

Indicates an experience in which the video extends beyond the app window boundaries/container.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case immersive
```

#### Discussion

It is valid to transition to `immersive` even when the `AVPlayerViewController` is not in the view hiearchy. In this case, a Placement must be specified through the Configuration object. If no placement is specified, the transition result will be `.reversed`.

## See Also

- [AVExperienceController.Experience.embedded](avexperiencecontroller/experience-swift.enum/embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](avexperiencecontroller/experience-swift.enum/expanded.md)
  An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.multiview](avexperiencecontroller/experience-swift.enum/multiview.md)
  An experience where multiple videos play together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/immersive)*