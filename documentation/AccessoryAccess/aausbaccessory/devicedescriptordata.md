# deviceDescriptorData

**Framework**: Accessory Access  
**Kind**: property

Returns the device descriptor data.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var deviceDescriptorData: Data { get }
```

#### Discussion

The underlying bytes can be cast to [`IOUSBDeviceDescriptor`](https://developer.apple.com/documentation/iokit/iousbdevicedescriptor).

## See Also

- [var configurationDescriptorData: Data?](aausbaccessory/configurationdescriptordata.md)
  Returns the currently selected configuration descriptor data.
- [var registryID: UInt64](aausbaccessory/registryid.md)
  Returns the IORegistry ID for the USB accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/devicedescriptordata)*