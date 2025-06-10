# TipGroup

**Framework**: TipKit  
**Kind**: class

A collection of tips that can be presented one at a time using a specific order or based on the first tip eligible for display.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
final class TipGroup
```

#### Overview

Use this class to group multiple tips together and have them presented one at a time. You display tips in a specific order with an [`TipGroup.Priority.ordered`](tipgroup/priority/ordered.md) priority or display the first tip eligible for display with a [`TipGroup.Priority.firstAvailable`](tipgroup/priority/firstavailable.md) priority.

TipGroup has a [`TipGroup.Priority.firstAvailable`](tipgroup/priority/firstavailable.md) default priority.

```swift
struct TrailDetails: View {
    let trail: Trail

    @State
    var trailDetailTips = TipGroup {
        FindTrailheadTip()
        ExposureRatingTip()
        SlopeProfileTip()
    }

    var body: some View {
        ScrollView(.vertical) {
            // Trail title
            Text(trail.name)
                .font(.title)
            NavigateToTrailButton(trailLocation: trail.location)
                .popoverTip(trailDetailTips.currentTip as? FindTrailheadTip)

            // Trail exposure rating
            TipView(trailDetailTips.currentTip as? ExposureRatingTip, arrowEdge: .bottom)
            Text("Exposure Rating: \(trail.exposureRating)")

            // Trail slope angle
            TipView(trailDetailTips.currentTip as? SlopeProfileTip, arrowEdge: .bottom)
            Text("Slope Angle: \(trail.slopeAngle)°")
        }
    }
}
```

## Topics

### Creating a tip group
- [init(TipGroup.Priority, () -> [any Tip])](tipgroup/init(_:_:).md)
  Creates a tip group with the specified presentation priority.
### Controlling the display order of a TipGroup’s tips
- [TipGroup.Priority](tipgroup/priority.md)
  Order priority for a [`TipGroup`](tipgroup.md).
### Getting the currently available tip
- [var currentTip: (any Tip)?](tipgroup/currenttip.md)
  Returns the current tip available for display.
- [var currentTipUpdates: some AsyncSequence<any Tip, Never>](tipgroup/currenttipupdates.md)
  Stream of tips that become eligible for display.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Tip](tip.md)
  A type that sets a tip’s content, as well as the conditions for when it displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipgroup)*