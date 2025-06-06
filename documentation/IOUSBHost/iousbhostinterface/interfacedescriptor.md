# interfaceDescriptor

**Framework**: IOUSBHost  
**Kind**: property

The descriptor for the interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor> { get }
```

#### Return Value

A pointer to the interface’s descriptor.

## See Also

- [var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>](iousbhostinterface/configurationdescriptor.md)
  The configuration descriptor for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/interfacedescriptor)*