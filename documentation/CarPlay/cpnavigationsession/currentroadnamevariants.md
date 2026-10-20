# currentRoadNameVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of strings that describe variants of the current road name.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var currentRoadNameVariants: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * currentRoadNameVariants;
```

#### Discussion

Set this property with variants of the current road name, from most to least verbose.

## See Also

### Managing Upcoming Maneuvers
- [var upcomingManeuvers: [CPManeuver]](./upcomingmaneuvers.md)
  The next set of maneuvers the user should perform while following the current route.
- [var maneuverState: CPManeuverState](./maneuverstate.md)
  The current maneuver state.
- [var currentLaneGuidance: CPLaneGuidance?](./currentlaneguidance.md)
  The current lane guidance to use for navigation metadata.
- [func add([CPManeuver])](./add%28_%29-17l62.md)
  Adds one or more maneuvers, in chronological order, to the navigation session.
- [func add([CPLaneGuidance])](./add%28_%29-93qpu.md)
  Adds one or more lane guidance instances to the navigation session.
- [class CPManeuver](../cpmaneuver.md)
  An object that describes a single navigation instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/currentroadnamevariants)*