# GetReplacementDetailsResponse

**Framework**: Device Management  
**Kind**: dictionary

Information about a replacement device, including the original device it replaces and the date the replacement occurred.

## Declaration

```swift
object GetReplacementDetailsResponse
```

## Properties

- `serial_number` (string): The serial number of the replacement device.
- `original_device_serial_number` (string): The serial number of the original device that this device replaces.
- `replacement_date` (string): The date when the device replacement occurred, in ISO 8601 format with day granularity in UTC (for example, `2025-01-15`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getreplacementdetailsresponse)*