# MatterAddDeviceRequest.DeviceCriteria.fabricNode(rootPublicKey:nodeID:)

**Framework**: MatterSupport  
**Kind**: case  
**Role**: Case

A device matches if it’s paired to a fabric using the provided fabric and node identifiers.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
case fabricNode(rootPublicKey: Data, nodeID: UInt64)
```

## Discussion

This will only match for devices already known to the system during the commissioning operation.

## See Also

### Defining the criteria
- [MatterAddDeviceRequest.DeviceCriteria.allDevices](./alldevices.md)
  All device match without any filtering.
- [case all([MatterAddDeviceRequest.DeviceCriteria])](./all%28_%29.md)
  A device matches the given criteria if it matches all of the individual ones
- [case any([MatterAddDeviceRequest.DeviceCriteria])](./any%28_%29.md)
  A device matches the given criteria if it matches any one of the individual ones .
- [MatterAddDeviceRequest.DeviceCriteria.commissioningID(_:)](./commissioningid%28_%29.md)
  A device matches if it has the given commissioning identifier.
- [case not(MatterAddDeviceRequest.DeviceCriteria)](./not%28_%29.md)
  A device matches the given criteria if it does not match the provided criteria.
- [MatterAddDeviceRequest.DeviceCriteria.productID(_:)](./productid%28_%29.md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.serialNumber(_:)](./serialnumber%28_%29.md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.vendorID(_:)](./vendorid%28_%29.md)
  A device matches if it has the given vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/devicecriteria/fabricnode(rootpublickey:nodeid:))*