# placement

**Framework**: AVKit  
**Kind**: property

Supply a Placement to be used when the original container isn’t added to the view controller hierarchy; i.e. the AVPlayerViewController is off-screen.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var placement: AVExperienceController.Configuration.Placement
```

#### Discussion

Indicates the placement of where the media playback will be experienced. Setting this property will apply to all experiences, unless its overwritten by the targeted experience configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.property)*