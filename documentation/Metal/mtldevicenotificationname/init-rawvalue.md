# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a Metal device notification name from a string.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

Use this type’s static properties instead of this initializer.

## Parameters

- `rawValue`: A string of the notification’s name.

## See Also

- [static let wasAdded: MTLDeviceNotificationName](mtldevicenotificationname/wasadded.md)
  A notification that Metal sends to observers when the system adds a GPU device.
- [static let removalRequested: MTLDeviceNotificationName](mtldevicenotificationname/removalrequested.md)
  A notification that Metal sends to observers when a person requests to remove a GPU device from the system.
- [static let wasRemoved: MTLDeviceNotificationName](mtldevicenotificationname/wasremoved.md)
  A notification that Metal sends to observers when the system removes a GPU device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicenotificationname/init(rawvalue:))*