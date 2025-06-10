# Tip

**Framework**: TipKit  
**Kind**: protocol

A type that sets a tip’s content, as well as the conditions for when it displays.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol Tip : Identifiable, Sendable
```

#### Overview

Use this protocol for setting a tip’s content, as well as defining the conditions for when it appears in a view. You create custom tips by declaring types that conform to the `Tip` protocol. Set your tip’s content by giving it a [`title`](tip/title.md),  [`message`](tip/message.md),  [`image`](tip/image.md), and a list of [`actions`](tip/actions.md).

For example, to create a tip with a `title`, `message`, and `image`:

```swift
struct FavoriteBackyardTip: Tip {
    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text? {
        Text("Your favorite backyards always appear at the top of the list.")
    }

    var image: Image? {
        Image(systemName: "star")
    }
}
```

For a tip to be valid, you need to set its `title`. To control when a tip displays, pass instances of [`Rule`](tip/rule.md) and [`Option`](tip/option.md) into the [`rules`](tip/rules.md) and [`options`](tip/options.md) properties of the tip.

After you define your tip’s content, display it in either a [`TipView`](tipview.md) or a [`popoverTip(_:arrowEdge:action:)`](https://developer.apple.com/documentation/SwiftUI/View/popoverTip(_:arrowEdge:action:)).

## Topics

### Setting tip content
- [var title: Text](tip/title.md)
  A title that names the tip.
- [var message: Text?](tip/message.md)
  A short description of how to use the tip’s feature.
- [var image: Image?](tip/image.md)
  The image associated with the tip.
- [var id: String](tip/id.md)
  The tip’s unique identifier.
### Controlling when tips appear
- [var rules: [Self.Rule]](tip/rules.md)
  The rules that determine when a tip is eligible for display. For more information on rules, see [`Rule`](tips/rule.md).
- [typealias Rule](tip/rule.md)
  A condition to meet before displaying a tip.
- [typealias Event](tip/event.md)
  A repeatable user-defined action.
### Customizing tip behavior
- [var options: [any TipOption]](tip/options.md)
  Customizations for a tip.
- [typealias Option](tip/option.md)
  A type that represents the various customizations that you can make to a tip’s behavior.
- [typealias IgnoresDisplayFrequency](tip/ignoresdisplayfrequency.md)
  Controls whether a tip obeys the preconfigured display frequency interval.
- [typealias MaxDisplayCount](tip/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [typealias MaxDisplayDuration](tip/maxdisplayduration.md)
  Specifies the maximum amount of time a tip is displayed before it is invalidated.
### Providing actions
- [var actions: [Self.Action]](tip/actions.md)
  Buttons that help people get started or learn more about your feature.
- [typealias Action](tip/action.md)
  A type that describes a control associated with a tip.
### Monitoring tip status
- [var status: Self.Status](tip/status-swift.property.md)
  The current status of a tip based on its rules and the configured [`displayFrequency(_:)`](tips/configurationoption/displayfrequency(_:).md).
- [var statusUpdates: AsyncStream<Self.Status>](tip/statusupdates.md)
  An asynchronous sequence for monitoring a tip’s status changes.
- [var shouldDisplay: Bool](tip/shoulddisplay.md)
  A Boolean value that determines whether to display a tip.
- [var shouldDisplayUpdates: AsyncMapSequence<AsyncStream<Self.Status>, Bool>](tip/shoulddisplayupdates.md)
  An asynchronous sequence for monitoring a tip’s display eligibility.
- [typealias Status](tip/status-swift.typealias.md)
  A type that describes the current display eligibility status for a tip.
- [typealias InvalidationReason](tip/invalidationreason.md)
  A type that describes why the system permanently invalidated a tip.
### Invalidating a tip
- [func invalidate(reason: Self.InvalidationReason)](tip/invalidate(reason:).md)
  Permanently invalidates a tip and prevents it from displaying.
- [func resetEligibility() async](tip/reseteligibility.md)
  Reset a previously invalidated tip.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AnyTip](anytip.md)

## See Also

- [class TipGroup](tipgroup.md)
  A collection of tips that can be presented one at a time using a specific order or based on the first tip eligible for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip)*