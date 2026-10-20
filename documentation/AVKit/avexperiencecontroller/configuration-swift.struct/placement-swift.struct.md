# AVExperienceController.Configuration.Placement

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

A struct used to set the placement for the media playback to be experienced.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Placement
```

#### Overview

Controls where an experience is placed. It can be over a UIScene.

## Topics

### Placements
- [static func over(scene: UIScene) -> AVExperienceController.Configuration.Placement](./placement-swift.struct/over%28scene%29.md)
  Place the video over the provided scene.
- [static var unspecified: AVExperienceController.Configuration.Placement](./placement-swift.struct/unspecified.md)
  Used as default when no UIScene is specified as a placement.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Configuring placement
- [var placement: AVExperienceController.Configuration.Placement](./placement-swift.property.md)
  Supply a Placement to be used when the original container isn’t added to the view controller hierarchy; i.e. the AVPlayerViewController is off-screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct)*