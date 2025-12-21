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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/immersive)*