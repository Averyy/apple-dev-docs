# StatusDeviceSystemHealthDeviceSystemHealthObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

A dictionary where each key represents a hardware component name and each value is a string indicating the component’s health status, which has the following values:

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```
object StatusDeviceSystemHealthDeviceSystemHealthObject
```

#### Discussion

- `ok`: The component is operating normally.
- `error`: The component has a detected error or failure.
- `non-genuine`: The component isn’t a genuine Apple component.
- `pending-repair`: The component is a genuine Apple component that requires a restart to finish its repair.

Not all keys are supported on each device. The dictionary includes only components that are present and reportable on the device.

## Properties

- `Baseband` (string): The baseband health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.

  **Allowed Values**: `ok`, `error`
- `Camera` (string): The camera health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.
  - `non-genuine`: The component isn’t a genuine Apple component.
  - `pending-repair`: The component is a genuine Apple component that requires a restart to finish its repair.

  **Allowed Values**: `ok`, `error`, `non-genuine`, `pending-repair`
- `Display` (string): The display health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.
  - `non-genuine`: The component isn’t a genuine Apple component.
  - `pending-repair`: The component is a genuine Apple component that requires a restart to finish its repair.

  **Allowed Values**: `ok`, `error`, `non-genuine`, `pending-repair`
- `FaceID` (string): The Face ID health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.
  - `pending-repair`: The component is a genuine Apple component that requires a restart to finish its repair.

  **Allowed Values**: `ok`, `error`, `pending-repair`
- `NFC` (string): The NFC (Near Field Communication) health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.

  **Allowed Values**: `ok`, `error`
- `TouchID` (string): The Touch ID health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.
  - `pending-repair`: The component is a genuine Apple component that requires a restart to finish its repair.

  **Allowed Values**: `ok`, `error`, `pending-repair`
- `UWB` (string): The UWB (Ultra-Wideband) radio health status, which has the following values:

  - `ok`: The component is operating normally.
  - `error`: The component has a detected error or failure.

  **Allowed Values**: `ok`, `error`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdevicesystemhealthdevicesystemhealthobject)*