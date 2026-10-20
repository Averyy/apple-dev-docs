# trafficSide

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A value that represents which side of the road the traffic drives on.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var trafficSide: CPTrafficSide { get set }
```

```objc
@property (nonatomic, assign) CPTrafficSide trafficSide;
```

#### Discussion

One of the [`CPTrafficSide`](../cptrafficside.md) values that indicates which side of the road traffic drives on; a [`CPManeuver`](../cpmaneuver.md) requires this value.

## See Also

### Providing maneuver information
- [var maneuverType: CPManeuverType](./maneuvertype.md)
  A value that represents the type of maneuver.
- [var roadFollowingManeuverVariants: [String]?](./roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var linkedLaneGuidance: CPLaneGuidance](./linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var highwayExitLabel: String](./highwayexitlabel.md)
  A string that describes a highway exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/trafficside)*