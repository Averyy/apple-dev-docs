# configurationDescriptor

**Framework**: IOUSBHost  
**Kind**: property

The configuration descriptor for the interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor> { get }
```

#### Return Value

A pointer to the device’s configuration descriptor.

## See Also

- [var interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor>](iousbhostinterface/interfacedescriptor.md)
  The descriptor for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/configurationdescriptor)*