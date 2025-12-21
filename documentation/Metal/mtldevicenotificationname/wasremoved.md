# wasRemoved

**Framework**: Metal  
**Kind**: property

A notification that Metal sends to observers when the system removes a GPU device.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let wasRemoved: MTLDeviceNotificationName
```

## Mentions

- [Handling external GPU additions and removals](handling-external-gpu-additions-and-removals.md)

#### Discussion

This notification tells your app that an [`MTLDevice`](mtldevice.md) instance and its methods are no longer valid to avoid runtime failures.

> ❗ **Important**:  If a person removes a GPU without warning, this notification may be posted without a prior [`removalRequested`](mtldevicenotificationname/removalrequested.md) notification.

## See Also

- [static let wasAdded: MTLDeviceNotificationName](mtldevicenotificationname/wasadded.md)
  A notification that Metal sends to observers when the system adds a GPU device.
- [static let removalRequested: MTLDeviceNotificationName](mtldevicenotificationname/removalrequested.md)
  A notification that Metal sends to observers when a person requests to remove a GPU device from the system.
- [init(rawValue: String)](mtldevicenotificationname/init(rawvalue:).md)
  Creates a Metal device notification name from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname/wasremoved)*