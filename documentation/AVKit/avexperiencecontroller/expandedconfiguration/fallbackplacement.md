# fallbackPlacement

**Framework**: AVKit  
**Kind**: property

A fallback placement to use when the original container isn’t in the view controller hierarchy.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement
```

#### Discussion

The system places expanded experience over the scene of the original container. When the container isn’t available, the system uses this value. If neither specifies a valid placement, attempting to transition to an expanded experience fails.

## See Also

- [AVExperienceController.ExpandedConfiguration.Placement](avexperiencecontroller/expandedconfiguration/placement.md)
  A structure that represents where the video will be experienced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration/fallbackplacement)*