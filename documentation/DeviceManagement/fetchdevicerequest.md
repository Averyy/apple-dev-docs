# FetchDeviceRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for a list of devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object FetchDeviceRequest
```

## Properties

- `cursor` (string): A hex string that represents the starting position for a request. Use this to retrieve the list of devices that have been added or removed since a previous request. The string can be up to 1000 characters. On the initial request, this should be omitted.
- `limit` (int32): The maximum number of entries to return. Optional.

## See Also

- [object FetchDeviceResponse](fetchdeviceresponse.md)
  The response that contains a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetchdevicerequest)*