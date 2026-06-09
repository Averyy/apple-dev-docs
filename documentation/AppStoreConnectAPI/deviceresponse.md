# DeviceResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a single registered device.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object DeviceResponse
```

## Properties

- `data` (Device) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [Register a new device](post-v1-devices.md)
  Register a new device for app development.
- [object Device](device.md)
  A physical Apple device registered in your developer account for testing, identified by its UDID and device type.
- [object DevicesWithoutIncludesResponse](deviceswithoutincludesresponse.md)
  A response containing a list of registered devices, without related resources.
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DevicesResponse](devicesresponse.md)
  The response body for endpoints that list registered devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/deviceresponse)*