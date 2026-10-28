# configurationDescriptor

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The configuration descriptor for the interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor> { get }
```

```objc
@property (readonly) const IOUSBConfigurationDescriptor * configurationDescriptor;
```

## Return Value

A pointer to the device’s configuration descriptor.

## See Also

### Retrieving Function Descriptors
- [var interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor>](./interfacedescriptor.md)
  The descriptor for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/configurationdescriptor)*