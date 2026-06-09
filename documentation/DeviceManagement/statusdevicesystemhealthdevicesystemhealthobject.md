# StatusDeviceSystemHealthDeviceSystemHealthObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary where each key represents a hardware component name and each value is a string indicating the component’s health status, which has the following values:

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
object StatusDeviceSystemHealthDeviceSystemHealthObject
```

#### Discussion

- `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `non-genuine`: The component isn’t a genuine Apple component.

Not all keys are supported on each device. The dictionary includes only components that are present and reportable on the device.

## Properties

- `Baseband` (string): The baseband health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `Camera` (string): The camera health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `non-genuine`: The component isn’t a genuine Apple component.
- `Display` (string): The display health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `non-genuine`: The component isn’t a genuine Apple component.
- `FaceID` (string): The Face ID health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `NFC` (string): The NFC (Near Field Communication) health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `TouchID` (string): The Touch ID health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `UWB` (string): The UWB (Ultra-Wideband) radio health status, which has the following values: - `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdevicesystemhealthdevicesystemhealthobject)*