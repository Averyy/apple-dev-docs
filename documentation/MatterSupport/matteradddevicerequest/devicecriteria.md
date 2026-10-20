# MatterAddDeviceRequest.DeviceCriteria

**Framework**: MatterSupport  
**Kind**: enum  
**Role**: Enumeration

A predicate to match against possible devices that may appear in the picker.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
enum DeviceCriteria
```

## Topics

### Creating criteria
- [init(from: any Decoder) throws](./init%28from%29.md)
  Create the request from a decoder.
### Defining the criteria
- [MatterAddDeviceRequest.DeviceCriteria.allDevices](./devicecriteria/alldevices.md)
  All device match without any filtering.
- [case all([MatterAddDeviceRequest.DeviceCriteria])](./devicecriteria/all%28_%29.md)
  A device matches the given criteria if it matches all of the individual ones
- [case any([MatterAddDeviceRequest.DeviceCriteria])](./devicecriteria/any%28_%29.md)
  A device matches the given criteria if it matches any one of the individual ones .
- [MatterAddDeviceRequest.DeviceCriteria.commissioningID(_:)](./devicecriteria/commissioningid%28_%29.md)
  A device matches if it has the given commissioning identifier.
- [MatterAddDeviceRequest.DeviceCriteria.fabricNode(rootPublicKey:nodeID:)](./devicecriteria/fabricnode%28rootpublickey,nodeid%29.md)
  A device matches if it’s paired to a fabric using the provided fabric and node identifiers.
- [case not(MatterAddDeviceRequest.DeviceCriteria)](./devicecriteria/not%28_%29.md)
  A device matches the given criteria if it does not match the provided criteria.
- [MatterAddDeviceRequest.DeviceCriteria.productID(_:)](./devicecriteria/productid%28_%29.md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.serialNumber(_:)](./devicecriteria/serialnumber%28_%29.md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.vendorID(_:)](./devicecriteria/vendorid%28_%29.md)
  A device matches if it has the given vendor.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining the device criteria
- [var showDeviceCriteria: MatterAddDeviceRequest.DeviceCriteria](./showdevicecriteria.md)
  A predicate that filters what devices appear in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/devicecriteria)*