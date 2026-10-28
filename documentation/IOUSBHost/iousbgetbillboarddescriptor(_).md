# IOUSBGetBillboardDescriptor(_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

Obtains the first billboard capability descriptor in a BOS descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetBillboardDescriptor(_ bosDescriptor: UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityBillboard>!
```

```c
const IOUSBDeviceCapabilityBillboard *IOUSBGetBillboardDescriptor(const IOUSBBOSDescriptor *bosDescriptor);
```

## Return Value

A billboard capability descriptor pointer, or `nil` if no matching descriptor returns.

## Discussion

This method uses [`IOUSBGetNextCapabilityDescriptorWithType(_:_:_:)`](./iousbgetnextcapabilitydescriptorwithtype%28_,_,_%29.md) to find the first billboard capability descriptor.

## Parameters

- `bosDescriptor`: A BOS descriptor that contains the descriptors to iterate through.

## See Also

### BOS Descriptor Parsing
- [func IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityUSB2Extension>!](./iousbgetusb20extensiondevicecapabilitydescriptor%28_%29.md)
  Obtains the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptorWithType(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](./iousbgetnextcapabilitydescriptorwithtype%28_,_,_%29.md)
  Obtains the next descriptor matching a specific type within a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](./iousbgetnextcapabilitydescriptor%28_,_%29.md)
  Obtains the next device capability descriptor in a BOS descriptor.
- [func IOUSBGetSuperSpeedDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedUSB>!](./iousbgetsuperspeeddevicecapabilitydescriptor%28_%29.md)
  Obtains the first SuperSpeed capability descriptor in a BOS descriptor.
- [func IOUSBGetContainerIDDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityContainerID>!](./iousbgetcontaineriddescriptor%28_%29.md)
  Obtains the first container ID capability descriptor in a BOS descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetbillboarddescriptor(_:))*