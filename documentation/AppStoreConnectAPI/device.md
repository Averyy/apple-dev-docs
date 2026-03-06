# Device

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Devices resource.

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
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DeviceResponse](deviceresponse.md)
  A response that contains a single Devices resource.
- [object DevicesResponse](devicesresponse.md)
  A response that contains a list of Devices resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/device)*