# maneuverType

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A value that represents the type of maneuver.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var maneuverType: CPManeuverType { get set }
```

```objc
@property (nonatomic, assign) CPManeuverType maneuverType;
```

#### Discussion

CarPlay requires this value to support route guidance metadata.

## See Also

### Providing maneuver information
- [var roadFollowingManeuverVariants: [String]?](./roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var linkedLaneGuidance: CPLaneGuidance](./linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var highwayExitLabel: String](./highwayexitlabel.md)
  A string that describes a highway exit.
- [var trafficSide: CPTrafficSide](./trafficside.md)
  A value that represents which side of the road the traffic drives on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/maneuvertype)*