# DeviceUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a Device.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object DeviceUpdateRequest
```

## Topics

### Objects
- [object DeviceUpdateRequest.Data](deviceupdaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (DeviceUpdateRequest.Data) *(required)*: The resource data.

## See Also

- [object Device](device.md)
  A physical Apple device registered in your developer account for testing, identified by its UDID and device type.
- [object DevicesWithoutIncludesResponse](deviceswithoutincludesresponse.md)
  A response containing a list of registered devices, without related resources.
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceResponse](deviceresponse.md)
  The response body for endpoints that create, read, or modify a single registered device.
- [object DevicesResponse](devicesresponse.md)
  The response body for endpoints that list registered devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/deviceupdaterequest)*