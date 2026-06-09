# DeviceCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create a Device.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object DeviceCreateRequest
```

## Topics

### Objects
- [object DeviceCreateRequest.Data](devicecreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (DeviceCreateRequest.Data) *(required)*: The resource data.

## See Also

- [object Device](device.md)
  A physical Apple device registered in your developer account for testing, identified by its UDID and device type.
- [object DevicesWithoutIncludesResponse](deviceswithoutincludesresponse.md)
  A response containing a list of registered devices, without related resources.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DeviceResponse](deviceresponse.md)
  The response body for endpoints that create, read, or modify a single registered device.
- [object DevicesResponse](devicesresponse.md)
  The response body for endpoints that list registered devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/devicecreaterequest)*