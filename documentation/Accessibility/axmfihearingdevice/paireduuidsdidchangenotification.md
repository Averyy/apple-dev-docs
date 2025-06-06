# pairedUUIDsDidChangeNotification

**Framework**: Accessibility  
**Kind**: property

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

#### Discussion

The system posts this notification when the value of [`pairedDeviceIdentifiers()`](axmfihearingdevice/paireddeviceidentifiers().md) changes.

## See Also

- [static func pairedDeviceIdentifiers() -> [UUID]](axmfihearingdevice/paireddeviceidentifiers.md)
  Returns the UUIDs of the hearing device peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/paireduuidsdidchangenotification)*