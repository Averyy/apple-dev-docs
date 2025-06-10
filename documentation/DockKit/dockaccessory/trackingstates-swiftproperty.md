# trackingStates

**Framework**: DockKit  
**Kind**: property

Provides an access to the asynchronous sequence of tracking session states

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
final var trackingStates: DockAccessory.TrackingStates { get throws }
```

#### Return Value

A `DockAccessory.TrackingStates` instance representing the current state of tracking.

#### Discussion

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device is disconnected, or [`DockKitError.notSupportedByDevice`](dockkiterror/notsupportedbydevice.md) if device doesn’t support updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/trackingstates-swift.property)*