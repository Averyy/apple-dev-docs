# AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria

**Framework**: Accessory Access  
**Kind**: struct

A structure you provide that enumerates which device interface characteristics to search for.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct InterfaceMatchingCriteria
```

## Topics

### Creating an interface characteristics structure
- [init(vendorID: Int?, productID: Int?, bcdDevice: Int?, interfaceNumber: Int?, configurationValue: Int?, interfaceClass: Int?, interfaceSubClass: Int?, interfaceProtocol: Int?, speed: Int?)](aausbaccessorymatchingcriteria/interfacematchingcriteria/init(vendorid:productid:bcddevice:interfacenumber:configurationvalue:interfaceclass:interfacesubclass:interfaceprotocol:speed:).md)
  Initializes a new matching criteria structure with the provided values.
### Interface characteristics
- [var bcdDevice: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/bcddevice.md)
  The 2-byte Binary-Coded Decimal (BCD) value defined by the manufacturer to indicate the device revision or version number.
- [var configurationValue: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/configurationvalue.md)
  The value that represents the configuration.
- [var interfaceClass: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/interfaceclass.md)
  The value that represents the interface class.
- [var interfaceNumber: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/interfacenumber.md)
  The value that represents the interface number.
- [var interfaceProtocol: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/interfaceprotocol.md)
  The value that represents the interface protocol.
- [var interfaceSubClass: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/interfacesubclass.md)
  The value that represents the interface subclass.
- [var productID: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/productid.md)
  The value that represents the product ID.
- [var speed: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/speed.md)
  The value that represents the interface speed.
- [var vendorID: Int?](aausbaccessorymatchingcriteria/interfacematchingcriteria/vendorid.md)
  The value that represents the vendor ID.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria](aausbaccessorymatchingcriteria/devicematchingcriteria.md)
  A structure you provide that enumerates which device characteristics to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/interfacematchingcriteria)*