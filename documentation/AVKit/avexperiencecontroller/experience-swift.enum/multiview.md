# AVExperienceController.Experience.multiview

**Framework**: AVKit  
**Kind**: case

An experience where multiple videos play together.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case multiview
```

#### Discussion

Configure this experience type using an [`AVMultiviewManager`](avmultiviewmanager.md).

It’s valid to transition to this experience from a player view controller that isn’t in a view hierarchy. This is useful when adding additional videos to a multiview experience.

Transition to embedded to remove an item from the multiview experience.

## See Also

- [AVExperienceController.Experience.embedded](avexperiencecontroller/experience-swift.enum/embedded.md)
  An experience where the video embeds within its original container.
- [AVExperienceController.Experience.expanded](avexperiencecontroller/experience-swift.enum/expanded.md)
  An experience where the system places the video outside of its original container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/experience-swift.enum/multiview)*