# MatterAddDeviceRequest.DeviceCriteria.all(_:)

**Framework**: MatterSupport  
**Kind**: case  
**Role**: Case

A device matches the given criteria if it matches all of the individual ones

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
indirect case all([MatterAddDeviceRequest.DeviceCriteria])
```

## See Also

### Defining the criteria
- [MatterAddDeviceRequest.DeviceCriteria.allDevices](./alldevices.md)
  All device match without any filtering.
- [case any([MatterAddDeviceRequest.DeviceCriteria])](./any%28_%29.md)
  A device matches the given criteria if it matches any one of the individual ones .
- [MatterAddDeviceRequest.DeviceCriteria.commissioningID(_:)](./commissioningid%28_%29.md)
  A device matches if it has the given commissioning identifier.
- [MatterAddDeviceRequest.DeviceCriteria.fabricNode(rootPublicKey:nodeID:)](./fabricnode%28rootpublickey,nodeid%29.md)
  A device matches if it’s paired to a fabric using the provided fabric and node identifiers.
- [case not(MatterAddDeviceRequest.DeviceCriteria)](./not%28_%29.md)
  A device matches the given criteria if it does not match the provided criteria.
- [MatterAddDeviceRequest.DeviceCriteria.productID(_:)](./productid%28_%29.md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.serialNumber(_:)](./serialnumber%28_%29.md)
  A device matches if it has the given product identifier.
- [MatterAddDeviceRequest.DeviceCriteria.vendorID(_:)](./vendorid%28_%29.md)
  A device matches if it has the given vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/devicecriteria/all(_:))*