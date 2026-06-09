# AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria

**Framework**: Accessory Access  
**Kind**: struct

A structure you provide that enumerates which device characteristics to search for.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct DeviceMatchingCriteria
```

## Topics

### Creating a device characteristics structure
- [init(vendorID: Int?, productID: Int?, deviceClass: Int?, deviceSubClass: Int?, deviceProtocol: Int?, speed: Int?)](aausbaccessorymatchingcriteria/devicematchingcriteria/init(vendorid:productid:deviceclass:devicesubclass:deviceprotocol:speed:).md)
  Initializes a new device matching criteria structure with the provided values.
### Device characteristics
- [var deviceClass: Int?](aausbaccessorymatchingcriteria/devicematchingcriteria/deviceclass.md)
  The value that represents the device class.
- [var deviceProtocol: Int?](aausbaccessorymatchingcriteria/devicematchingcriteria/deviceprotocol.md)
  The value that represents the device protocol.
- [var deviceSubClass: Int?](aausbaccessorymatchingcriteria/devicematchingcriteria/devicesubclass.md)
  The value that represents the device subclass.
- [var productID: Int?](aausbaccessorymatchingcriteria/devicematchingcriteria/productid.md)
  The value that represents the product ID.
- [var speed: Int?](aausbaccessorymatchingcriteria/devicematchingcriteria/speed.md)
  The value that represents the device speed.
- [var vendorID: Int?](aausbaccessorymatchingcriteria/devicematchingcriteria/vendorid.md)
  The value that represents the vendor ID.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria](aausbaccessorymatchingcriteria/interfacematchingcriteria.md)
  A structure you provide that enumerates which device interface characteristics to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/devicematchingcriteria)*