# AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria

**Framework**: Accessory Access  
**Kind**: struct  
**Role**: Structure

A structure you provide that enumerates which device characteristics to search for.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct DeviceMatchingCriteria
```

## Topics

### Creating a device characteristics structure
- [init(vendorID: Int?, productID: Int?, deviceClass: Int?, deviceSubClass: Int?, deviceProtocol: Int?, speed: Int?)](./devicematchingcriteria/init%28vendorid,productid,deviceclass,devicesubclass,deviceprotocol,speed%29.md)
  Initializes a new device matching criteria structure with the provided values.
### Device characteristics
- [var deviceClass: Int?](./devicematchingcriteria/deviceclass.md)
  The value that represents the device class.
- [var deviceProtocol: Int?](./devicematchingcriteria/deviceprotocol.md)
  The value that represents the device protocol.
- [var deviceSubClass: Int?](./devicematchingcriteria/devicesubclass.md)
  The value that represents the device subclass.
- [var productID: Int?](./devicematchingcriteria/productid.md)
  The value that represents the product ID.
- [var speed: Int?](./devicematchingcriteria/speed.md)
  The value that represents the device speed.
- [var vendorID: Int?](./devicematchingcriteria/vendorid.md)
  The value that represents the vendor ID.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying device and interface criteria
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria](./interfacematchingcriteria.md)
  A structure you provide that enumerates which device interface characteristics to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/devicematchingcriteria)*