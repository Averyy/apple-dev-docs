# removalRequested

**Framework**: Metal  
**Kind**: property

A notification that Metal sends to observers when a person requests to remove a GPU device from the system.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let removalRequested: MTLDeviceNotificationName
```

## Mentions

- [Handling External GPU Additions and Removals](handling-external-gpu-additions-and-removals.md)

#### Discussion

This notification tells your app to stop using an [`MTLDevice`](mtldevice.md) instance by releasing any objects and resources your app created with it.

> **Note**:  Metal removes the device instance from the array it returns with its methods — such as [`MTLCopyAllDevices()`](mtlcopyalldevices().md) — before sending this notification.

 Metal removes the device instance from the array it returns with its methods — such as [`MTLCopyAllDevices()`](mtlcopyalldevices().md) — before sending this notification.

## See Also

- [static let wasAdded: MTLDeviceNotificationName](mtldevicenotificationname/wasadded.md)
  A notification that Metal sends to observers when the system adds a GPU device.
- [static let wasRemoved: MTLDeviceNotificationName](mtldevicenotificationname/wasremoved.md)
  A notification that Metal sends to observers when the system removes a GPU device.
- [init(rawValue: String)](mtldevicenotificationname/init(rawvalue:).md)
  Creates a Metal device notification name from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname/removalrequested)*