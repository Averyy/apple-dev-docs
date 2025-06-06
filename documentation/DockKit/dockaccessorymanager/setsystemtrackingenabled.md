# setSystemTrackingEnabled(_:)

**Framework**: DockKit  
**Kind**: method

Enable and disable system tracking for camera-enabled apps.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setSystemTrackingEnabled(_ isEnabled: Bool) async throws
```

## Mentions

- [Modify rotation and positioning programmatically](modify-rotation-and-positioning-behavior-programmatically.md)

#### Discussion

DockKit enables system tracking by default, and any camera stream automatically generates and sends tracking events when a device docks to a compatible dock accessory.

Always set this value to `false` before performing your own custom tracking.

> **Note**: [`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

[`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

## See Also

- [var isSystemTrackingEnabled: Bool](dockaccessorymanager/issystemtrackingenabled.md)
  An indication of whether system tracking is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessorymanager/setsystemtrackingenabled(_:))*