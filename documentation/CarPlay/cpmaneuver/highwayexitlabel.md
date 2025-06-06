# highwayExitLabel

**Framework**: CarPlay  
**Kind**: property

A string that describes a highway exit.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var highwayExitLabel: String { get set }
```

#### Discussion

Set the label to a string that describes the exit, as in the example:

```swift
   highwayExitLabel = "Exit 123"

```

## See Also

- [var maneuverType: CPManeuverType](cpmaneuver/maneuvertype.md)
  A value that represents the type of maneuver.
- [var roadFollowingManeuverVariants: [String]?](cpmaneuver/roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var linkedLaneGuidance: CPLaneGuidance](cpmaneuver/linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var trafficSide: CPTrafficSide](cpmaneuver/trafficside.md)
  A value that represents which side of the road the traffic drives on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/highwayexitlabel)*