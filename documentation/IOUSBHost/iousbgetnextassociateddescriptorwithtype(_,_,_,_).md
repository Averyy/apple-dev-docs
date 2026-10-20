# IOUSBGetNextAssociatedDescriptorWithType(_:_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

Obtains the next associated descriptor in a configuration descriptor and matches the type.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextAssociatedDescriptorWithType(_ configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>!, _ parentDescriptor: UnsafePointer<IOUSBDescriptorHeader>!, _ currentDescriptor: UnsafePointer<IOUSBDescriptorHeader>!, _ type: UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!
```

```c
const IOUSBDescriptorHeader *IOUSBGetNextAssociatedDescriptorWithType(const IOUSBConfigurationDescriptor *configurationDescriptor, const IOUSBDescriptorHeader *parentDescriptor, const IOUSBDescriptorHeader *currentDescriptor, const uint8_t type);
```

#### Return Value

A descriptor pointer, or `nil` if no matching descriptor returns.

#### Discussion

This method uses [`IOUSBGetNextAssociatedDescriptor(_:_:_:)`](./iousbgetnextassociateddescriptor%28_,_,_%29.md), and further validates that the returned descriptor’s `bDescriptorType` field matches the type that the parameter passes.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `parentDescriptor`: A descriptor pointer within the bounds of `configurationDescriptor`.
- `currentDescriptor`: A descriptor pointer within the bounds of `configurationDescriptor`, or `nil`.
- `type`: The descriptor type to find.

## See Also

### Configuration Descriptor Parsing
- [func IOUSBGetNextDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](./iousbgetnextdescriptor%28_,_%29.md)
  Obtains the next descriptor in a configuration descriptor.
- [func IOUSBGetNextDescriptorWithType(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UInt8) -> UnsafePointer<IOUSBDescriptorHeader>!](./iousbgetnextdescriptorwithtype%28_,_,_%29.md)
  Obtains the next descriptor in a configuration descriptor that matches the type.
- [func IOUSBGetNextAssociatedDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBDescriptorHeader>!](./iousbgetnextassociateddescriptor%28_,_,_%29.md)
  Obtains the next associated descriptor in a configuration descriptor.
- [func IOUSBGetNextInterfaceAssociationDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceAssociationDescriptor>!](./iousbgetnextinterfaceassociationdescriptor%28_,_%29.md)
  Obtains the next interface association descriptor in a configuration descriptor.
- [func IOUSBGetNextInterfaceDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBInterfaceDescriptor>!](./iousbgetnextinterfacedescriptor%28_,_%29.md)
  Obtains the next interface descriptor in a configuration descriptor.
- [func IOUSBGetConfigurationMaxPowerMilliAmps(UInt32, UnsafePointer<IOUSBConfigurationDescriptor>!) -> UInt32](./iousbgetconfigurationmaxpowermilliamps%28_,_%29.md)
  Obtains the maximum bus current that a configuration descriptor requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextassociateddescriptorwithtype(_:_:_:_:))*