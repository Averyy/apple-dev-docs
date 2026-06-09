# DevicesWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of registered devices, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object DevicesWithoutIncludesResponse
```

## Properties

- `data` ([Device]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object Device](device.md)
  A physical Apple device registered in your developer account for testing, identified by its UDID and device type.
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DeviceResponse](deviceresponse.md)
  The response body for endpoints that create, read, or modify a single registered device.
- [object DevicesResponse](devicesresponse.md)
  The response body for endpoints that list registered devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/deviceswithoutincludesresponse)*