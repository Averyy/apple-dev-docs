# DevicesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list registered devices.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object DevicesResponse
```

## Properties

- `data` ([Device]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

- [List devices](get-v1-devices.md)
  Find and list devices registered to your team.
- [object Device](device.md)
  A physical Apple device registered in your developer account for testing, identified by its UDID and device type.
- [object DevicesWithoutIncludesResponse](deviceswithoutincludesresponse.md)
  A response containing a list of registered devices, without related resources.
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DeviceResponse](deviceresponse.md)
  The response body for endpoints that create, read, or modify a single registered device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/devicesresponse)*