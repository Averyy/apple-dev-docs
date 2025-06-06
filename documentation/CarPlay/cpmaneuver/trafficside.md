# trafficSide

**Framework**: CarPlay  
**Kind**: property

A value that represents which side of the road the traffic drives on.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var trafficSide: CPTrafficSide { get set }
```

#### Discussion

One of the [`CPTrafficSide`](cptrafficside.md) values that indicates which side of the road traffic drives on; a [`CPManeuver`](cpmaneuver.md) requires this value.

## See Also

- [var maneuverType: CPManeuverType](cpmaneuver/maneuvertype.md)
  A value that represents the type of maneuver.
- [var roadFollowingManeuverVariants: [String]?](cpmaneuver/roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var linkedLaneGuidance: CPLaneGuidance](cpmaneuver/linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var highwayExitLabel: String](cpmaneuver/highwayexitlabel.md)
  A string that describes a highway exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/trafficside)*