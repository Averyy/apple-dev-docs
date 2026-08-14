# init(deviceMatchingCriteria:interfaceMatchingCriteria:interfaceMatchingOption:)

**Framework**: Accessory Access  
**Kind**: init

Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)
```

#### Discussion

Initialize a criteria object using USB interface matching dictionaries, for the given USB device matching dictionary.

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:`](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/creatematchingdictionarywithvendorid:productid:bcddevice:deviceclass:devicesubclass:deviceprotocol:speed:productidarray:) to create a USB device matching dictionary.

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:interfaceNumber:configurationValue:interfaceClass:interfaceSubclass:interfaceProtocol:speed:productIDArray:`](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/creatematchingdictionarywithvendorid:productid:bcddevice:interfacenumber:configurationvalue:interfaceclass:interfacesubclass:interfaceprotocol:speed:productidarray:) to create a USB interface matching dictionary.

See USBSpec.h in [`USBSpec.h User-Space`](https://developer.apple.com/documentation/iokit/usbspec_h_user-space) in [`IOKit`](https://developer.apple.com/documentation/iokit) for more details about dictionary keys for the USB device/interface matching dictionaries.

If the criteria is initialized with [`AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAny`](aausbaccessorymatchingcriteria/interfacematchingoption/matchany.md), then it evaluates to true for a USB accessory when it matches the given non-`nil` `deviceMatchingDictionary`, and for the currently set configuration, any of the `interfaceMatchingDictionaries` match at least one of its USB interfaces.

## Parameters

- `deviceMatchingCriteria`: USB device matching criteria.
- `interfaceMatchingCriteria`: USB interface matching criteria.
- `interfaceMatchingOption`: Option that specifies how the framework performs interface matching for a USB accessory. If the criteria is initialized with [`AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAll`](aausbaccessorymatchingcriteria/interfacematchingoption/matchall.md), then it evaluates to `true` for a USB accessory when - It matches the given non-nil deviceMatchingDictionary, and
- For the currently set configuration, all the `interfaceMatchingDictionaries` match at least one of its USB interfaces.

## See Also

- [init?(deviceMatchingDictionary: [String : any Sendable])](aausbaccessorymatchingcriteria/init(devicematchingdictionary:).md)
  Initializes a criteria object using a USB device matching dictionary.
- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingdictionary:interfacematchingdictionaries:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)](aausbaccessorymatchingcriteria/init(devicematchingcriteria:).md)
  Initializes a criteria object with the provided USB device matching properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/init(devicematchingcriteria:interfacematchingcriteria:interfacematchingoption:))*