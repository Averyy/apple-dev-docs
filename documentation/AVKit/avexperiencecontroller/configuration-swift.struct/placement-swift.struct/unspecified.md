# unspecified

**Framework**: AVKit  
**Kind**: property

Used as default when no UIScene is specified as a placement.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var unspecified: AVExperienceController.Configuration.Placement { get }
```

#### Discussion

Experiences will be placed over the UIScene of the original container. If contained within a UIScene, the system will use that scene as a placement, if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/configuration-swift.struct/placement-swift.struct/unspecified)*