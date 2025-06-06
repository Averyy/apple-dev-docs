# MatterAddDeviceRequest.DeviceCriteria.all(_:)

**Framework**: MatterSupport  
**Kind**: case

A device matches the given criteria if it matches all of the individual ones

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
indirect case all([MatterAddDeviceRequest.DeviceCriteria])
```

## See Also

- [MatterAddDeviceRequest.DeviceCriteria.allDevices](matteradddevicerequest/devicecriteria/alldevices.md)
  All device match without any filtering.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/devicecriteria/all(_:))*