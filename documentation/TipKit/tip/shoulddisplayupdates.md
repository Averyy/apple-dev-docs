# shouldDisplayUpdates

**Framework**: TipKit  
**Kind**: property

An asynchronous sequence for monitoring a tip’s display eligibility.

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
var shouldDisplayUpdates: AsyncMapSequence<AsyncStream<Self.Status>, Bool> { get }
```

## See Also

- [var status: Self.Status](tip/status-swift.property.md)
  The current status of a tip based on its rules and the configured [`displayFrequency(_:)`](tips/configurationoption/displayfrequency(_:).md).
- [var statusUpdates: AsyncStream<Self.Status>](tip/statusupdates.md)
  An asynchronous sequence for monitoring a tip’s status changes.
- [var shouldDisplay: Bool](tip/shoulddisplay.md)
  A Boolean value that determines whether to display a tip.
- [typealias Status](tip/status-swift.typealias.md)
  A type that describes the current display eligibility status for a tip.
- [typealias InvalidationReason](tip/invalidationreason.md)
  A type that describes why the system permanently invalidated a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/shoulddisplayupdates)*