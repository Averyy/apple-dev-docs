# accessoryEvents

**Framework**: DockKit  
**Kind**: property

Events from the accessory that signify button presses or common camera controls.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
final var accessoryEvents: DockAccessory.AccessoryEvents { get throws }
```

#### Return Value

Accessory events related to button presses and common camera controls.

#### Discussion

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device is disconnected, or [`DockKitError.notSupportedByDevice`](dockkiterror/notsupportedbydevice.md) if device doesn’t support updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/accessoryevents-swift.property)*