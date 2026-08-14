# init(deviceMatchingCriteria:)

**Framework**: Accessory Access  
**Kind**: init

Initializes a criteria object with the provided USB device matching properties.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)
```

#### Discussion

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:`](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/creatematchingdictionarywithvendorid:productid:bcddevice:deviceclass:devicesubclass:deviceprotocol:speed:productidarray:) to create the matching dictionary.

See USBSpec.h in [`USBSpec.h User-Space`](https://developer.apple.com/documentation/iokit/usbspec_h_user-space) in [`IOKit`](https://developer.apple.com/documentation/iokit) for more details about dictionary keys for the USB device properties.

## Parameters

- `deviceMatchingCriteria`: The matching dictionary that contains USB device properties.

## See Also

- [init?(deviceMatchingDictionary: [String : any Sendable])](aausbaccessorymatchingcriteria/init(devicematchingdictionary:).md)
  Initializes a criteria object using a USB device matching dictionary.
- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingdictionary:interfacematchingdictionaries:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingcriteria:interfacematchingcriteria:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/init(devicematchingcriteria:))*