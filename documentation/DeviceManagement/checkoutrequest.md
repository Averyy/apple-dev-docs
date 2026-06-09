# CheckOutRequest

**Framework**: Device Management  
**Kind**: dictionary

The check out request details.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object CheckOutRequest
```

## Properties

- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | visionOS 1.1+
- `MessageType` (string) *(required)*: The message type, which requires a value of `CheckOut`.
- `Topic` (string) *(required)*: The topic the device subscribes to.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/checkoutrequest)*