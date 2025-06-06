# IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the first USB 2.0 extension capability descriptor in a BOS descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(_ bosDescriptor: UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityUSB2Extension>!
```

#### Return Value

The device capability extension pointer, or `nil` if no matching descriptor returns.

#### Discussion

This method uses [`IOUSBGetNextCapabilityDescriptorWithType(_:_:_:)`](iousbgetnextcapabilitydescriptorwithtype(_:_:_:).md) to find the first device capability extension.

## Parameters

- `bosDescriptor`: A BOS descriptor that contains the descriptors to iterate through.

## See Also

- [func IOUSBGetNextCapabilityDescriptorWithType(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](iousbgetnextcapabilitydescriptorwithtype(_:_:_:).md)
  Obtains the next descriptor matching a specific type within a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](iousbgetnextcapabilitydescriptor(_:_:).md)
  Obtains the next device capability descriptor in a BOS descriptor.
- [func IOUSBGetSuperSpeedDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedUSB>!](iousbgetsuperspeeddevicecapabilitydescriptor(_:).md)
  Obtains the first SuperSpeed capability descriptor in a BOS descriptor.
- [func IOUSBGetContainerIDDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityContainerID>!](iousbgetcontaineriddescriptor(_:).md)
  Obtains the first container ID capability descriptor in a BOS descriptor.
- [func IOUSBGetBillboardDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityBillboard>!](iousbgetbillboarddescriptor(_:).md)
  Obtains the first billboard capability descriptor in a BOS descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetusb20extensiondevicecapabilitydescriptor(_:))*