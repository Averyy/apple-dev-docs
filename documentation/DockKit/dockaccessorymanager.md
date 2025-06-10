# DockAccessoryManager

**Framework**: DockKit  
**Kind**: class

Observe the state of dock accessories and enable or disable system tracking.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class DockAccessoryManager
```

#### Overview

`DockAccessoryManager`  enables and disables system tracking for camera-enabled apps, and provides docking and undocking notifications. If you want to customize the tracking behavior of a dock accessory, use [`accessoryStateChanges`](dockaccessorymanager/accessorystatechanges.md) to obtain that accessory.

This class is a singleton, so use [`shared`](dockaccessorymanager/shared.md) to fetch the single instance.

## Topics

### Obtaining a manager
- [static let shared: DockAccessoryManager](dockaccessorymanager/shared.md)
  The accessory manager singleton object.
### Controlling dock accessories
- [var accessoryStateChanges: DockAccessory.StateChanges](dockaccessorymanager/accessorystatechanges.md)
  Obtain a reference to a dock accessory and receive notifications about its state.
### Changing tracking behavior
- [var isSystemTrackingEnabled: Bool](dockaccessorymanager/issystemtrackingenabled.md)
  An indication of whether system tracking is enabled.
- [func setSystemTrackingEnabled(Bool) async throws](dockaccessorymanager/setsystemtrackingenabled(_:).md)
  Enable and disable system tracking for camera-enabled apps.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Controlling a DockKit accessory using your camera app](controlling-a-dockkit-accessory-using-your-camera-app.md)
  Follow subjects in real time using an iPhone that you mount on a DockKit accessory.
- [class DockAccessory](dockaccessory.md)
  Obtain accessory information and control tracking behavior.
- [enum DockKitError](dockkiterror.md)
  A list of errors that DockKit sends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessorymanager)*