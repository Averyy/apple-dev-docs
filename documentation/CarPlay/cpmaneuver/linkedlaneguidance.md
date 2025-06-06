# linkedLaneGuidance

**Framework**: CarPlay  
**Kind**: property

A value that represents lane guidance associated with this maneuver.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
unowned(unsafe) var linkedLaneGuidance: CPLaneGuidance { get set }
```

#### Discussion

This value is optional; however [`CPManeuver`](cpmaneuver.md) requires this value if there is a corresponding lane guidance value.

## See Also

- [var maneuverType: CPManeuverType](cpmaneuver/maneuvertype.md)
  A value that represents the type of maneuver.
- [var roadFollowingManeuverVariants: [String]?](cpmaneuver/roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var highwayExitLabel: String](cpmaneuver/highwayexitlabel.md)
  A string that describes a highway exit.
- [var trafficSide: CPTrafficSide](cpmaneuver/trafficside.md)
  A value that represents which side of the road the traffic drives on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/linkedlaneguidance)*