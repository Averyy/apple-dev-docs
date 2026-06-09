# configurationDescriptorData

**Framework**: Accessory Access  
**Kind**: property

Returns the currently selected configuration descriptor data.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var configurationDescriptorData: Data? { get }
```

#### Discussion

The underlying bytes can be cast to [`IOUSBConfigurationDescriptor`](https://developer.apple.com/documentation/kernel/iousbconfigurationdescriptor). If the USB accessory isn’t configured, this returns `nil`.

## See Also

- [var deviceDescriptorData: Data](aausbaccessory/devicedescriptordata.md)
  Returns the device descriptor data.
- [var registryID: UInt64](aausbaccessory/registryid.md)
  Returns the IORegistry ID for the USB accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/configurationdescriptordata)*