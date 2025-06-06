# AVExperienceController.ExpandedConfiguration

**Framework**: AVKit  
**Kind**: struct

A structure that specifies options for an expanded experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct ExpandedConfiguration
```

#### Overview

It’s valid to transition to this experience even when the original container isn’t in a view hierarchy. In this case, you must specify a [`fallbackPlacement`](avexperiencecontroller/expandedconfiguration/fallbackplacement.md) or the transition result is [`AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)`](avexperiencecontroller/transitioncontext/transitionresult/reversed(reason:).md).

## Topics

### Creating an expanded configuration
- [init(fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement)](avexperiencecontroller/expandedconfiguration/init(fallbackplacement:).md)
  Creates a configuration object for an expanded experience.
### Specifying placement
- [var fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement](avexperiencecontroller/expandedconfiguration/fallbackplacement.md)
  A fallback placement to use when the original container isn’t in the view controller hierarchy.
- [AVExperienceController.ExpandedConfiguration.Placement](avexperiencecontroller/expandedconfiguration/placement.md)
  A structure that represents where the video will be experienced.

## See Also

- [var expanded: AVExperienceController.ExpandedConfiguration](avexperiencecontroller/configuration-swift.struct/expanded.md)
  Configuration options for an expanded experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration)*