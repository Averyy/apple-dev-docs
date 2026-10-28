# AVExperienceController.Experience.multiview

**Framework**: AVKit  
**Kind**: case  
**Role**: Case

An experience where multiple videos play together.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case multiview
```

## Discussion

Configure this experience type using an [`AVMultiviewManager`](../../avmultiviewmanager.md).

It’s valid to transition to this experience from a player view controller that isn’t in a view hierarchy. This is useful when adding additional videos to a multiview experience.

Transition to embedded to remove an item from the multiview experience.

## See Also

### Supported experiences
- [AVExperienceController.Experience.embedded](./embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](./expanded.md)
  An experience where the system places the video outside of its original container.
- [AVExperienceController.Experience.immersive](./immersive.md)
  Indicates an experience in which the video extends beyond the app window boundaries/container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/multiview)*