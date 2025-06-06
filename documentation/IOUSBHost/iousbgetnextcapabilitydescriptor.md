# IOUSBGetNextCapabilityDescriptor(_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the next device capability descriptor in a BOS descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextCapabilityDescriptor(_ bosDescriptor: UnsafePointer<IOUSBBOSDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!
```

#### Return Value

A device capability descriptor pointer, or `nil` if no descriptor returns.

#### Discussion

This method advances the current descriptor by its length, and validates that the new descriptor fits within the bounds of `bosDescriptor`. Use `nil` for `currentDescriptor` to return the first descriptor after the BOS descriptor.

## Parameters

- `bosDescriptor`: A BOS descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of  , or  .

## See Also

- [func IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityUSB2Extension>!](iousbgetusb20extensiondevicecapabilitydescriptor(_:).md)
  Obtains the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptorWithType(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](iousbgetnextcapabilitydescriptorwithtype(_:_:_:).md)
  Obtains the next descriptor matching a specific type within a BOS descriptor.
- [func IOUSBGetSuperSpeedDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedUSB>!](iousbgetsuperspeeddevicecapabilitydescriptor(_:).md)
  Obtains the first SuperSpeed capability descriptor in a BOS descriptor.
- [func IOUSBGetContainerIDDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityContainerID>!](iousbgetcontaineriddescriptor(_:).md)
  Obtains the first container ID capability descriptor in a BOS descriptor.
- [func IOUSBGetBillboardDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityBillboard>!](iousbgetbillboarddescriptor(_:).md)
  Obtains the first billboard capability descriptor in a BOS descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextcapabilitydescriptor(_:_:))*