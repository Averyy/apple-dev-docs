# roadFollowingManeuverVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var roadFollowingManeuverVariants: [String]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * roadFollowingManeuverVariants;
```

## Discussion

Localize each variant for display to the individual; the array needs to contain at least one variant. The system displays the first variant that fits into the available screen space; arrange the variants in order from most- to least-preferred.

## See Also

### Providing maneuver information
- [var maneuverType: CPManeuverType](./maneuvertype.md)
  A value that represents the type of maneuver.
- [var linkedLaneGuidance: CPLaneGuidance](./linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var highwayExitLabel: String](./highwayexitlabel.md)
  A string that describes a highway exit.
- [var trafficSide: CPTrafficSide](./trafficside.md)
  A value that represents which side of the road the traffic drives on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/roadfollowingmaneuvervariants)*