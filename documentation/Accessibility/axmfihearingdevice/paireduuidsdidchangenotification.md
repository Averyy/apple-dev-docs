# pairedUUIDsDidChangeNotification

**Framework**: Accessibility  
**Kind**: property  
**Role**: Type Property

A notification that the system posts when there’s a change to the UUIDs of the hearing device peripherals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let pairedUUIDsDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AXMFiHearingDevicePairedUUIDsDidChangeNotification;
```

## Discussion

The system posts this notification when the value of [`pairedDeviceIdentifiers()`](./paireddeviceidentifiers%28%29.md) changes.

## See Also

### Paired hearing devices
- [static func pairedDeviceIdentifiers() -> [UUID]](./paireddeviceidentifiers%28%29.md)
  Returns the UUIDs of the hearing device peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/paireduuidsdidchangenotification)*