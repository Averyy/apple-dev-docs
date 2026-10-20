# AVExperienceController.ExpandedConfiguration

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

A structure that specifies options for an expanded experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct ExpandedConfiguration
```

#### Overview

It’s valid to transition to this experience even when the original container isn’t in a view hierarchy. In this case, you must specify a [`fallbackPlacement`](./expandedconfiguration/fallbackplacement.md) or the transition result is [`AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)`](./transitioncontext/transitionresult/reversed%28reason%29.md).

## Topics

### Creating an expanded configuration
- [init(fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement)](./expandedconfiguration/init%28fallbackplacement%29.md)
  Creates a configuration object for an expanded experience.
### Specifying placement
- [var fallbackPlacement: AVExperienceController.ExpandedConfiguration.Placement](./expandedconfiguration/fallbackplacement.md)
  A fallback placement to use when the original container isn’t in the view controller hierarchy.
- [AVExperienceController.ExpandedConfiguration.Placement](./expandedconfiguration/placement.md)
  A structure that represents where the video will be experienced.
### Configuring automatic immersive transitions
- [var automaticTransitionToImmersive: AVExperienceController.ExpandedConfiguration.AutomaticTransitionToImmersive](./expandedconfiguration/automatictransitiontoimmersive-swift.property.md)
  The expanded experience automatic transition behavior for the immersive experience.
- [AVExperienceController.ExpandedConfiguration.AutomaticTransitionToImmersive](./expandedconfiguration/automatictransitiontoimmersive-swift.enum.md)
  The expanded experience automatic transition behavior into the immersive experience.

## See Also

### Configuring experiences
- [var expanded: AVExperienceController.ExpandedConfiguration](./configuration-swift.struct/expanded.md)
  Configuration options for an expanded experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/expandedconfiguration)*