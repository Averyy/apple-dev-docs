# wasAdded

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A notification that Metal sends to observers when the system adds a GPU device.

**Availability**:
- macOS 10.13+ - Deprecated in 27.0

> **Deprecated**: Device notifications are not applicable on Apple Silicon

## Declaration

```swift
static let wasAdded: MTLDeviceNotificationName
```

```c
extern MTLDeviceNotificationName const MTLDeviceWasAddedNotification;
```

## Mentions

- [Handling external GPU additions and removals](../handling-external-gpu-additions-and-removals.md)

## See Also

### Creating a notification name
- [static let removalRequested: MTLDeviceNotificationName](./removalrequested.md)
  A notification that Metal sends to observers when a person requests to remove a GPU device from the system.
- [static let wasRemoved: MTLDeviceNotificationName](./wasremoved.md)
  A notification that Metal sends to observers when the system removes a GPU device.
- [init(rawValue: String)](./init%28rawvalue%29.md)
  Creates a Metal device notification name from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname/wasadded)*