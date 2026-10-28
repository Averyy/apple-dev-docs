# IOUSBGetNextDescriptor(_:_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

Obtains the next descriptor in a configuration descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextDescriptor(_ configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!
```

```c
const IOUSBDescriptorHeader *IOUSBGetNextDescriptor(const IOUSBConfigurationDescriptor *configurationDescriptor, const IOUSBDescriptorHeader *currentDescriptor);
```

## Return Value

A descriptor pointer, or `nil` if no matching descriptor returns.

## Discussion

This method advances the current descriptor by its length, and validates that the new descriptor fits within the bounds of `configurationDescriptor`. Use `nil` for `currentDescriptor` to return the first descriptor after the configuration descriptor.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `currentDescriptor`: A description header within the bounds of `configurationDescriptor`, or `nil`.

## See Also

### Configuration Descriptor Parsing
- [func IOUSBGetNextDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](./iousbgetnextdescriptorwithtype%28_,_,_%29.md)
  Obtains the next descriptor in a configuration descriptor that matches the type.
- [func IOUSBGetNextAssociatedDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](./iousbgetnextassociateddescriptor%28_,_,_%29.md)
  Obtains the next associated descriptor in a configuration descriptor.
- [func IOUSBGetNextAssociatedDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](./iousbgetnextassociateddescriptorwithtype%28_,_,_,_%29.md)
  Obtains the next associated descriptor in a configuration descriptor and matches the type.
- [func IOUSBGetNextInterfaceAssociationDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceAssociationDescriptor>!](./iousbgetnextinterfaceassociationdescriptor%28_,_%29.md)
  Obtains the next interface association descriptor in a configuration descriptor.
- [func IOUSBGetNextInterfaceDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceDescriptor>!](./iousbgetnextinterfacedescriptor%28_,_%29.md)
  Obtains the next interface descriptor in a configuration descriptor.
- [func IOUSBGetConfigurationMaxPowerMilliAmps(UInt32, UnsafePointer<IOUSBConfigurationDescriptor>!) -> UInt32](./iousbgetconfigurationmaxpowermilliamps%28_,_%29.md)
  Obtains the maximum bus current that a configuration descriptor requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextdescriptor(_:_:))*