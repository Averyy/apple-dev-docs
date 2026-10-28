# IOUSBGetNextCapabilityDescriptorWithType(_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

Obtains the next descriptor matching a specific type within a BOS descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextCapabilityDescriptorWithType(_ bosDescriptor: UnsafePointer<IOUSBBOSDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!, _ type: UInt8) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!
```

```c
const IOUSBDeviceCapabilityDescriptorHeader *IOUSBGetNextCapabilityDescriptorWithType(const IOUSBBOSDescriptor *bosDescriptor, const IOUSBDeviceCapabilityDescriptorHeader *currentDescriptor, const uint8_t type);
```

## Return Value

A device capability descriptor pointer, or `nil` if no matching descriptor returns.

## Discussion

This method uses [`IOUSBGetNextCapabilityDescriptor(_:_:)`](./iousbgetnextcapabilitydescriptor%28_,_%29.md), and further validates that the returned descriptor’s `bDevCapabilityType` field matches the type parameter.

## Parameters

- `bosDescriptor`: A BOS descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of `configurationDescriptor`, or `nil`.
- `type`: The descriptor type to find.

## See Also

### BOS Descriptor Parsing
- [func IOUSBGetUSB20ExtensionDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityUSB2Extension>!](./iousbgetusb20extensiondevicecapabilitydescriptor%28_%29.md)
  Obtains the first USB 2.0 extension capability descriptor in a BOS descriptor.
- [func IOUSBGetNextCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!, UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!) -> UnsafePointer<IOUSBDeviceCapabilityDescriptorHeader>!](./iousbgetnextcapabilitydescriptor%28_,_%29.md)
  Obtains the next device capability descriptor in a BOS descriptor.
- [func IOUSBGetSuperSpeedDeviceCapabilityDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilitySuperSpeedUSB>!](./iousbgetsuperspeeddevicecapabilitydescriptor%28_%29.md)
  Obtains the first SuperSpeed capability descriptor in a BOS descriptor.
- [func IOUSBGetContainerIDDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityContainerID>!](./iousbgetcontaineriddescriptor%28_%29.md)
  Obtains the first container ID capability descriptor in a BOS descriptor.
- [func IOUSBGetBillboardDescriptor(UnsafePointer<IOUSBBOSDescriptor>!) -> UnsafePointer<IOUSBDeviceCapabilityBillboard>!](./iousbgetbillboarddescriptor%28_%29.md)
  Obtains the first billboard capability descriptor in a BOS descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextcapabilitydescriptorwithtype(_:_:_:))*