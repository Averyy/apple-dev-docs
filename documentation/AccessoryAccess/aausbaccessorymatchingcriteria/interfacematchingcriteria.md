# AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria

**Framework**: Accessory Access  
**Kind**: struct  
**Role**: Structure

A structure you provide that enumerates which device interface characteristics to search for.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct InterfaceMatchingCriteria
```

## Topics

### Creating an interface characteristics structure
- [init(vendorID: Int?, productID: Int?, bcdDevice: Int?, interfaceNumber: Int?, configurationValue: Int?, interfaceClass: Int?, interfaceSubClass: Int?, interfaceProtocol: Int?, speed: Int?)](./interfacematchingcriteria/init%28vendorid,productid,bcddevice,interfacenumber,configurationvalue,interfaceclass,interfacesubclass,interfaceprotocol,speed%29.md)
  Initializes a new matching criteria structure with the provided values.
### Interface characteristics
- [var bcdDevice: Int?](./interfacematchingcriteria/bcddevice.md)
  The 2-byte Binary-Coded Decimal (BCD) value defined by the manufacturer to indicate the device revision or version number.
- [var configurationValue: Int?](./interfacematchingcriteria/configurationvalue.md)
  The value that represents the configuration.
- [var interfaceClass: Int?](./interfacematchingcriteria/interfaceclass.md)
  The value that represents the interface class.
- [var interfaceNumber: Int?](./interfacematchingcriteria/interfacenumber.md)
  The value that represents the interface number.
- [var interfaceProtocol: Int?](./interfacematchingcriteria/interfaceprotocol.md)
  The value that represents the interface protocol.
- [var interfaceSubClass: Int?](./interfacematchingcriteria/interfacesubclass.md)
  The value that represents the interface subclass.
- [var productID: Int?](./interfacematchingcriteria/productid.md)
  The value that represents the product ID.
- [var speed: Int?](./interfacematchingcriteria/speed.md)
  The value that represents the interface speed.
- [var vendorID: Int?](./interfacematchingcriteria/vendorid.md)
  The value that represents the vendor ID.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying device and interface criteria
- [AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria](./devicematchingcriteria.md)
  A structure you provide that enumerates which device characteristics to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/interfacematchingcriteria)*