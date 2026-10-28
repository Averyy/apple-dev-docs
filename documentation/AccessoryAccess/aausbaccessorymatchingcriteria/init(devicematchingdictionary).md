# init(deviceMatchingDictionary:)

**Framework**: Accessory Access  
**Kind**: init  
**Role**: Initializer

Initializes a criteria object using a USB device matching dictionary.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(deviceMatchingDictionary dictionary: [String : any Sendable])
```

```objc
- (instancetype) initWithDeviceMatchingDictionary:(NSDictionary<NSString *,id> *) dictionary;
```

## Discussion

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:`](../../IOUSBHost/iousbhostdevice/creatematchingdictionarywithvendorid_productid_bcddevice_deviceclass_devicesubclass_deviceprotocol_speed_productidarray_.md) to create such a matching dictionary.

See [IOTypes.h User-Space](../../iokit/iotypes_h_user-space.md) in [IOKit](../../iokit/iokit.md) for more details about dictionary keys for the USB device properties.

## Parameters

- `dictionary`: The matching dictionary containing USB device properties.

## See Also

### Creating matching criteria
- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./init%28devicematchingdictionary,interfacematchingdictionaries,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)](./init%28devicematchingcriteria%29.md)
  Initializes a criteria object with the provided USB device matching properties.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./init%28devicematchingcriteria,interfacematchingcriteria,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/init(devicematchingdictionary:))*