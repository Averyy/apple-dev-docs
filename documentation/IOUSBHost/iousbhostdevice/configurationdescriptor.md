# configurationDescriptor

**Framework**: IOUSBHost  
**Kind**: property

The currently selected configuration descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>? { get }
```

#### Return Value

A pointer to the device’s configuration descriptor, or `nil` if no matching descriptor returns.

#### Discussion

> **Note**:  The [`IOUSBHostDevice`](iousbhostdevice.md) performs memory management. Don’t free the descriptor, and assume it is valid as long as the [`IOUSBHostDevice`](iousbhostdevice.md) hasn’t called [`destroy()`](iousbhostobject/destroy().md).

 The [`IOUSBHostDevice`](iousbhostdevice.md) performs memory management. Don’t free the descriptor, and assume it is valid as long as the [`IOUSBHostDevice`](iousbhostdevice.md) hasn’t called [`destroy()`](iousbhostobject/destroy().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/configurationdescriptor)*