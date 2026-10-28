# batteryStates

**Framework**: DockKit  
**Kind**: property  
**Role**: Instance Property

Battery states from the accessory that indicate changes in battery charge or readiness

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
final var batteryStates: DockAccessory.BatteryStates { get throws }
```

## Return Value

Accessory events related to button presses and common camera controls.

## Discussion

> **Throws**: [`DockKitError.notConnected`](../dockkiterror/notconnected.md) if device is disconnected, or [`DockKitError.notSupportedByDevice`](../dockkiterror/notsupportedbydevice.md) if device doesn’t support updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/batterystates-swift.property)*