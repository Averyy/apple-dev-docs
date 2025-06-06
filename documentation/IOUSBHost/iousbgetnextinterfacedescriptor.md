# IOUSBGetNextInterfaceDescriptor(_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the next interface descriptor in a configuration descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextInterfaceDescriptor(_ configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceDescriptor>!
```

#### Return Value

The next interface descriptor pointer, or `nil` if no matching descriptor returns.

#### Discussion

This method uses [`IOUSBGetNextDescriptorWithType(_:_:_:)`](iousbgetnextdescriptorwithtype(_:_:_:).md) to find the next interface descriptor.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A descriptor pointer within the bounds of  , or  .

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
- [func IOUSBGetConfigurationMaxPowerMilliAmps(UInt32, UnsafePointer<IOUSBConfigurationDescriptor>!) -> UInt32](iousbgetconfigurationmaxpowermilliamps(_:_:).md)
  Obtains the maximum bus current that a configuration descriptor requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextinterfacedescriptor(_:_:))*