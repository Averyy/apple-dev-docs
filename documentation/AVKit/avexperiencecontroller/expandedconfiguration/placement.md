# AVExperienceController.ExpandedConfiguration.Placement

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

A structure that represents where the video will be experienced.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Placement
```

## Overview

Control where an experience is placed. It can be over a UIScene.

## Topics

### Placements
- [static func over(scene: UIScene) -> AVExperienceController.ExpandedConfiguration.Placement](./placement/over%28scene%29.md)
  Places the video over the provided scene.
- [static var unspecified: AVExperienceController.ExpandedConfiguration.Placement](./placement/unspecified.md)
  Doesn’t specify placement.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Specifying placement
- [var fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement](./fallbackplacement.md)
  A fallback placement to use when the original container isn’t in the view controller hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration/placement)*