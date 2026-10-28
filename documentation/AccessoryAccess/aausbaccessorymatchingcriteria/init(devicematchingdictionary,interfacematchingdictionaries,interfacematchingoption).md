# init(deviceMatchingDictionary:interfaceMatchingDictionaries:interfaceMatchingOption:)

**Framework**: Accessory Access  
**Kind**: init  
**Role**: Initializer

Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)
```

```objc
- (instancetype) initWithDeviceMatchingDictionary:(NSDictionary<NSString *,id> *) deviceMatchingDictionary interfaceMatchingDictionaries:(NSArray<NSDictionary<NSString *,id> *> *) interfaceMatchingDictionaries interfaceMatchingOption:(AAUSBAccessoryMatchingCriteriaInterfaceMatchingOption) interfaceMatchingOption;
```

## Discussion

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:`](../../IOUSBHost/iousbhostdevice/creatematchingdictionarywithvendorid_productid_bcddevice_deviceclass_devicesubclass_deviceprotocol_speed_productidarray_.md) to create a USB device matching dictionary.

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:interfaceNumber:configurationValue:interfaceClass:interfaceSubclass:interfaceProtocol:speed:productIDArray:`](../../IOUSBHost/iousbhostinterface/creatematchingdictionarywithvendorid_productid_bcddevice_interfacenumber_configurationvalue_interfaceclass_interfacesubclass_interfaceprotocol_speed_productidarray_.md) to create a USB interface matching dictionary.

See USBSpec.h in [USBSpec.h User-Space](../../iokit/usbspec_h_user-space.md) in [IOKit](../../iokit/iokit.md) for more details about dictionary keys for the USB device/interface matching dictionaries.

### Understanding interface matching options

If you initialize the criteria with [`AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAll`](./interfacematchingoption/matchall.md), then it evaluates to true for a USB accessory when

- It matches the provided non-`nil` `deviceMatchingDictionary`, and
- For the currently set configuration, all the `interfaceMatchingDictionaries` match at least one of its USB interfaces.

If you initialize the criteria is with [`AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAny`](./interfacematchingoption/matchany.md), then it evaluates to true for a USB accessory when

- It matches the provided non-`nil` `deviceMatchingDictionary`, and
- For the currently set configuration, any of the `interfaceMatchingDictionaries` match at least one of its USB interfaces.

## Parameters

- `deviceMatchingDictionary`: USB device matching dictionary.
- `interfaceMatchingDictionaries`: USB interface matching criteria.
- `interfaceMatchingOption`: Option specifying how the framework performs interface matching for a USB accessory. For more information on interface matching options, see [Understanding interface matching options](./init%28devicematchingdictionary,interfacematchingdictionaries,interfacematchingoption%29.md#Understanding-interface-matching-options).

## See Also

### Creating matching criteria
- [init?(deviceMatchingDictionary: [String : any Sendable])](./init%28devicematchingdictionary%29.md)
  Initializes a criteria object using a USB device matching dictionary.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)](./init%28devicematchingcriteria%29.md)
  Initializes a criteria object with the provided USB device matching properties.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./init%28devicematchingcriteria,interfacematchingcriteria,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/init(devicematchingdictionary:interfacematchingdictionaries:interfacematchingoption:))*