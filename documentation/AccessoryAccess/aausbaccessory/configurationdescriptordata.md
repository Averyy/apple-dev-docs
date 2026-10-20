# configurationDescriptorData

**Framework**: Accessory Access  
**Kind**: property  
**Role**: Instance Property

Returns the currently selected configuration descriptor data.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var configurationDescriptorData: Data? { get }
```

```objc
@property (readonly, nullable) NSData * configurationDescriptorData;
```

#### Discussion

The underlying bytes can be cast to [`IOUSBConfigurationDescriptor`](../../kernel/iousbconfigurationdescriptor.md). If the USB accessory isn’t configured, this returns `nil`.

## See Also

### Getting information about a USB accessory
- [var deviceDescriptorData: Data](./devicedescriptordata.md)
  Returns the device descriptor data.
- [var registryID: UInt64](./registryid.md)
  Returns the IORegistry ID for the USB accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/configurationdescriptordata)*