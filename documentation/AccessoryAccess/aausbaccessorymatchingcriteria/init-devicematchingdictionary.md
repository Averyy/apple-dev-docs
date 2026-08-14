# init(deviceMatchingDictionary:)

**Framework**: Accessory Access  
**Kind**: init

Initializes a criteria object using a USB device matching dictionary.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(deviceMatchingDictionary dictionary: [String : any Sendable])
```

#### Discussion

Use [`createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:`](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/creatematchingdictionarywithvendorid:productid:bcddevice:deviceclass:devicesubclass:deviceprotocol:speed:productidarray:) to create such a matching dictionary.

See [`IOTypes.h User-Space`](https://developer.apple.com/documentation/iokit/iotypes_h_user-space) in [`IOKit`](https://developer.apple.com/documentation/iokit) for more details about dictionary keys for the USB device properties.

## Parameters

- `dictionary`: The matching dictionary containing USB device properties.

## See Also

- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingdictionary:interfacematchingdictionaries:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)](aausbaccessorymatchingcriteria/init(devicematchingcriteria:).md)
  Initializes a criteria object with the provided USB device matching properties.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingcriteria:interfacematchingcriteria:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/init(devicematchingdictionary:))*