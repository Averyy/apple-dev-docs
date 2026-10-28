# removalRequested

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A notification that Metal sends to observers when a person requests to remove a GPU device from the system.

**Availability**:
- macOS 10.13+ - Deprecated in 27.0

> **Deprecated**: Device notifications are not applicable on Apple Silicon

## Declaration

```swift
static let removalRequested: MTLDeviceNotificationName
```

```c
extern MTLDeviceNotificationName const MTLDeviceRemovalRequestedNotification;
```

## Mentions

- [Handling external GPU additions and removals](../handling-external-gpu-additions-and-removals.md)

## Discussion

This notification tells your app to stop using an [`MTLDevice`](../mtldevice.md) instance by releasing any objects and resources your app created with it.

> **Note**:  Metal removes the device instance from the array it returns with its methods — such as [`MTLCopyAllDevices()`](../mtlcopyalldevices%28%29.md) — before sending this notification.

## See Also

### Creating a notification name
- [static let wasAdded: MTLDeviceNotificationName](./wasadded.md)
  A notification that Metal sends to observers when the system adds a GPU device.
- [static let wasRemoved: MTLDeviceNotificationName](./wasremoved.md)
  A notification that Metal sends to observers when the system removes a GPU device.
- [init(rawValue: String)](./init%28rawvalue%29.md)
  Creates a Metal device notification name from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname/removalrequested)*