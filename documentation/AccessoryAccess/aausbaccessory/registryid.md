# registryID

**Framework**: Accessory Access  
**Kind**: property  
**Role**: Instance Property

Returns the IORegistry ID for the USB accessory.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var registryID: UInt64 { get }
```

```objc
@property (readonly) uint64_t registryID;
```

## See Also

### Getting information about a USB accessory
- [var configurationDescriptorData: Data?](./configurationdescriptordata.md)
  Returns the currently selected configuration descriptor data.
- [var deviceDescriptorData: Data](./devicedescriptordata.md)
  Returns the device descriptor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/registryid)*