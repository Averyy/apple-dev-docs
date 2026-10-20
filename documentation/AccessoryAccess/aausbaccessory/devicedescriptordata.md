# deviceDescriptorData

**Framework**: Accessory Access  
**Kind**: property  
**Role**: Instance Property

Returns the device descriptor data.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var deviceDescriptorData: Data { get }
```

```objc
@property (readonly) NSData * deviceDescriptorData;
```

#### Discussion

The underlying bytes can be cast to [`IOUSBDeviceDescriptor`](../../iokit/iousbdevicedescriptor.md).

## See Also

### Getting information about a USB accessory
- [var configurationDescriptorData: Data?](./configurationdescriptordata.md)
  Returns the currently selected configuration descriptor data.
- [var registryID: UInt64](./registryid.md)
  Returns the IORegistry ID for the USB accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/devicedescriptordata)*