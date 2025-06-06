# IOUSBGetNextCapabilityDescriptorWithType(_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the next descriptor matching a specific type within a BOS descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextCapabilityDescriptorWithType(_ bosDescriptor: UnsafePointer<IOUSBBOSDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!, _ type: UInt8) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!
```

#### Return Value

A device capability descriptor pointer, or `nil` if no matching descriptor returns.

#### Discussion

This method uses [`IOUSBGetNextCapabilityDescriptor(_:_:)`](iousbgetnextcapabilitydescriptor(_:_:).md), and further validates that the returned descriptor’s `bDevCapabilityType` field matches the type parameter.

## Parameters

- `bosDescriptor`: A BOS descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of  , or  .
- `type`: The descriptor type to find.

## See Also

- [func IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityUSB2Extension>!](iousbgetusb20extensiondevicecapabilitydescriptor(_:).md)
  Obtains the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](iousbgetnextcapabilitydescriptor(_:_:).md)
  Obtains the next device capability descriptor in a BOS descriptor.
- [func IOUSBGetSuperSpeedDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedUSB>!](iousbgetsuperspeeddevicecapabilitydescriptor(_:).md)
  Obtains the first SuperSpeed capability descriptor in a BOS descriptor.
- [func IOUSBGetContainerIDDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityContainerID>!](iousbgetcontaineriddescriptor(_:).md)
  Obtains the first container ID capability descriptor in a BOS descriptor.
- [func IOUSBGetBillboardDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityBillboard>!](iousbgetbillboarddescriptor(_:).md)
  Obtains the first billboard capability descriptor in a BOS descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextcapabilitydescriptorwithtype(_:_:_:))*