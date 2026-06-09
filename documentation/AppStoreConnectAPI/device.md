# Device

**Framework**: App Store Connect API  
**Kind**: dictionary

A physical Apple device registered in your developer account for testing, identified by its UDID and device type.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object Device
```

## Topics

### Objects
- [object Device.Attributes](device/attributes-data.dictionary.md)
  Attributes that describe a Devices resource.

## Properties

- `attributes` (Device.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object DevicesWithoutIncludesResponse](deviceswithoutincludesresponse.md)
  A response containing a list of registered devices, without related resources.
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DeviceResponse](deviceresponse.md)
  The response body for endpoints that create, read, or modify a single registered device.
- [object DevicesResponse](devicesresponse.md)
  The response body for endpoints that list registered devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/device)*