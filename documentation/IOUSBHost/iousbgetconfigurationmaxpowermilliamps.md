# IOUSBGetConfigurationMaxPowerMilliAmps(_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the maximum bus current that a configuration descriptor requires.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetConfigurationMaxPowerMilliAmps(_ usbDeviceSpeed: UInt32, _ descriptor: UnsafePointer<IOUSBConfigurationDescriptor>!) -> UInt32
```

#### Return Value

The number of milliamps necessary.

#### Discussion

This method parses a configuration descriptor and returns the number of milliamps necessary to power the device.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The configuration descriptor to parse.

## See Also

- [func IOUSBGetNextDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextdescriptor(_:_:).md)
  Obtains the next descriptor in a configuration descriptor.
- [func IOUSBGetNextDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextdescriptorwithtype(_:_:_:).md)
  Obtains the next descriptor in a configuration descriptor that matches the type.
- [func IOUSBGetNextAssociatedDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextassociateddescriptor(_:_:_:).md)
  Obtains the next associated descriptor in a configuration descriptor.
- [func IOUSBGetNextAssociatedDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](iousbgetnextassociateddescriptorwithtype(_:_:_:_:).md)
  Obtains the next associated descriptor in a configuration descriptor and matches the type.
- [func IOUSBGetNextInterfaceAssociationDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceAssociationDescriptor>!](iousbgetnextinterfaceassociationdescriptor(_:_:).md)
  Obtains the next interface association descriptor in a configuration descriptor.
- [func IOUSBGetNextInterfaceDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceDescriptor>!](iousbgetnextinterfacedescriptor(_:_:).md)
  Obtains the next interface descriptor in a configuration descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetconfigurationmaxpowermilliamps(_:_:))*