# AuthenticateRequest

**Framework**: Device Management  
**Kind**: dictionary

The authenticate request details.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AuthenticateRequest
```

## Properties

- `BuildVersion` (string): The device’s build version.
- `DeviceName` (string) *(required)*: The device’s name.
- `EnrollmentID` (string): The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available in iOS 13 and later, macOS 10.15 and later, and visionOS 2 and later.
- `IMEI` (string): The device’s IMEI (International Mobile Equipment Identity).
- `MEID` (string): The device’s MEID (Mobile Equipment Identifier).
- `MessageType` (string) *(required)*: The message type, which requires a value of `Authenticate`.
- `Model` (string) *(required)*: The device’s model.
- `ModelName` (string) *(required)*: The device’s model name.
- `OSVersion` (string): The device’s OS version.
- `ProductName` (string): The device’s product name (such as `iPhone17,2`).
- `SerialNumber` (string): The device’s serial number.
- `Topic` (string) *(required)*: The topic that the device subscribes to.
- `UDID` (string): The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/authenticaterequest)*