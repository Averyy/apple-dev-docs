# MatterAddDeviceRequest.DeviceCriteria

**Framework**: MatterSupport  
**Kind**: enum

A predicate to match against possible devices that may appear in the picker.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
enum DeviceCriteria
```

## Topics

### Creating criteria
- [init(from: any Decoder) throws](matteradddevicerequest/init(from:).md)
  Create the request from a decoder.
### Defining the criteria
- [MatterAddDeviceRequest.DeviceCriteria.allDevices](matteradddevicerequest/devicecriteria/alldevices.md)
  All device match without any filtering.
- [case all([MatterAddDeviceRequest.DeviceCriteria])](matteradddevicerequest/devicecriteria/all(_:).md)
  A device matches the given criteria if it matches all of the individual ones
- [case any([MatterAddDeviceRequest.DeviceCriteria])](matteradddevicerequest/devicecriteria/any(_:).md)
  A device matches the given criteria if it matches any one of the individual ones .
- [MatterAddDeviceRequest.DeviceCriteria.commissioningID(_:)](matteradddevicerequest/devicecriteria/commissioningid(_:).md)
  A device matches if it has the given commissioning identifier.
- [MatterAddDeviceRequest.DeviceCriteria.fabricNode(rootPublicKey:nodeID:)](matteradddevicerequest/devicecriteria/fabricnode(rootpublickey:nodeid:).md)
  A device matches if it’s paired to a fabric using the provided fabric and node identifiers.
- [case not(MatterAddDeviceRequest.DeviceCriteria)](matteradddevicerequest/devicecriteria/not(_:).md)
  A device matches the given criteria if it does not match the provided criteria.
- [MatterAddDeviceRequest.DeviceCriteria.productID(_:)](matteradddevicerequest/devicecriteria/productid(_:).md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.serialNumber(_:)](matteradddevicerequest/devicecriteria/serialnumber(_:).md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.vendorID(_:)](matteradddevicerequest/devicecriteria/vendorid(_:).md)
  A device matches if it has the given vendor.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var showDeviceCriteria: MatterAddDeviceRequest.DeviceCriteria](matteradddevicerequest/showdevicecriteria.md)
  A predicate that filters what devices appear in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/devicecriteria)*