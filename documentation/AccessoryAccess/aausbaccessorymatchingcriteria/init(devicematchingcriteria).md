# init(deviceMatchingCriteria:)

**Framework**: Accessory Access  
**Kind**: init  
**Role**: Initializer

Initializes a criteria object with the provided USB device matching properties.

**Availability**:
- macOS 27.0+

## Declaration

```swift
convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)
```

## Discussion

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:`](../../IOUSBHost/iousbhostdevice/creatematchingdictionarywithvendorid_productid_bcddevice_deviceclass_devicesubclass_deviceprotocol_speed_productidarray_.md) to create the matching dictionary.

See USBSpec.h in [USBSpec.h User-Space](../../iokit/usbspec_h_user-space.md) in [IOKit](../../iokit/iokit.md) for more details about dictionary keys for the USB device properties.

## Parameters

- `deviceMatchingCriteria`: The matching dictionary that contains USB device properties.

## See Also

### Creating matching criteria
- [init?(deviceMatchingDictionary: [String : any Sendable])](./init%28devicematchingdictionary%29.md)
  Initializes a criteria object using a USB device matching dictionary.
- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./init%28devicematchingdictionary,interfacematchingdictionaries,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./init%28devicematchingcriteria,interfacematchingcriteria,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/init(devicematchingcriteria:))*