# highwayExitLabel

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A string that describes a highway exit.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var highwayExitLabel: String { get set }
```

```objc
@property (nonatomic, copy) NSString * highwayExitLabel;
```

#### Discussion

Set the label to a string that describes the exit, as in the example:

```swift
   highwayExitLabel = "Exit 123"

```

## See Also

### Providing maneuver information
- [var maneuverType: CPManeuverType](./maneuvertype.md)
  A value that represents the type of maneuver.
- [var roadFollowingManeuverVariants: [String]?](./roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var linkedLaneGuidance: CPLaneGuidance](./linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var trafficSide: CPTrafficSide](./trafficside.md)
  A value that represents which side of the road the traffic drives on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/highwayexitlabel)*