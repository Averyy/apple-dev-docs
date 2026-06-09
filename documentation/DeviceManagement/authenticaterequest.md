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

## Declaration

```swift
object AuthenticateRequest
```

## Properties

- `BuildVersion` (string): The device’s build version. Available: iOS 9+ | iPadOS 9+ | macOS 10.7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `DeviceName` (string) *(required)*: The device’s name. Available: macOS 10.7+
- `EnrollmentID` (string): The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 13+ | iPadOS 13+ | macOS 10.15+ | visionOS 1.1+
- `IMEI` (string): The device’s IMEI (International Mobile Equipment Identity). Available: iOS 9+ | iPadOS 9+ | visionOS 1.1+ | watchOS 10+
- `MEID` (string): The device’s MEID (Mobile Equipment Identifier). Available: iOS 9+ | iPadOS 9+ | visionOS 1.1+ | watchOS 10+
- `MessageType` (string) *(required)*: The message type, which requires a value of `Authenticate`.
- `Model` (string) *(required)*: The device’s model. Available: macOS 10.7+
- `ModelName` (string) *(required)*: The device’s model name. Available: macOS 10.7+
- `OSVersion` (string): The device’s OS version. Available: iOS 9+ | iPadOS 9+ | macOS 10.7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `ProductName` (string): The device’s product name (such as `iPhone17,2`). Available: iOS 9+ | iPadOS 9+ | macOS 10.7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `SerialNumber` (string): The device’s serial number. Available: iOS 9+ | iPadOS 9+ | macOS 10.7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `Topic` (string) *(required)*: The topic that the device subscribes to.
- `UDID` (string): The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/authenticaterequest)*