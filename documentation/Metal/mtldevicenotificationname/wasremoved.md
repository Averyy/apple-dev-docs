# wasRemoved

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A notification that Metal sends to observers when the system removes a GPU device.

**Availability**:
- macOS 10.13+ - Deprecated in 27.0

> **Deprecated**: Device notifications are not applicable on Apple Silicon

## Declaration

```swift
static let wasRemoved: MTLDeviceNotificationName
```

```c
extern MTLDeviceNotificationName const MTLDeviceWasRemovedNotification;
```

## Mentions

- [Handling external GPU additions and removals](../handling-external-gpu-additions-and-removals.md)

#### Discussion

This notification tells your app that an [`MTLDevice`](../mtldevice.md) instance and its methods are no longer valid to avoid runtime failures.

> ❗ **Important**:  If a person removes a GPU without warning, this notification may be posted without a prior [`removalRequested`](./removalrequested.md) notification.

## See Also

### Creating a notification name
- [static let wasAdded: MTLDeviceNotificationName](./wasadded.md)
  A notification that Metal sends to observers when the system adds a GPU device.
- [static let removalRequested: MTLDeviceNotificationName](./removalrequested.md)
  A notification that Metal sends to observers when a person requests to remove a GPU device from the system.
- [init(rawValue: String)](./init%28rawvalue%29.md)
  Creates a Metal device notification name from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname/wasremoved)*