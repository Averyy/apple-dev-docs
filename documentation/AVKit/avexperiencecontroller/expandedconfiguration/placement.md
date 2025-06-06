# AVExperienceController.ExpandedConfiguration.Placement

**Framework**: AVKit  
**Kind**: struct

A structure that represents where the video will be experienced.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Placement
```

#### Overview

Control where an experience is placed. It can be over a UIScene.

## Topics

### Placements
- [static func over(scene: UIScene) -> AVExperienceController.ExpandedConfiguration.Placement](avexperiencecontroller/expandedconfiguration/placement/over(scene:).md)
  Places the video over the provided scene.
- [static var unspecified: AVExperienceController.ExpandedConfiguration.Placement](avexperiencecontroller/expandedconfiguration/placement/unspecified.md)
  Doesn’t specify placement.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement](avexperiencecontroller/expandedconfiguration/fallbackplacement.md)
  A fallback placement to use when the original container isn’t in the view controller hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration/placement)*