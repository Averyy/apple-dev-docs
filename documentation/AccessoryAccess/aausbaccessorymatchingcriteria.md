# AAUSBAccessoryMatchingCriteria

**Framework**: Accessory Access  
**Kind**: class

A class that represents the accessory matching criteria for a USB accessory.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class AAUSBAccessoryMatchingCriteria
```

#### Discussion

A class that conforms to the [`AAUSBAccessoryListener`](aausbaccessorylistener.md) protocol can use [`AAUSBAccessoryMatchingCriteria`](aausbaccessorymatchingcriteria.md) objects to register itself with [`AAUSBAccessoryManager`](aausbaccessorymanager.md).

## Topics

### Creating matching criteria
- [init?(deviceMatchingDictionary: [String : any Sendable])](aausbaccessorymatchingcriteria/init(devicematchingdictionary:).md)
  Initializes a criteria object using a USB device matching dictionary.
- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingdictionary:interfacematchingdictionaries:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)](aausbaccessorymatchingcriteria/init(devicematchingcriteria:).md)
  Initializes a criteria object with the provided USB device matching properties.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](aausbaccessorymatchingcriteria/init(devicematchingcriteria:interfacematchingcriteria:interfacematchingoption:).md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.
### Specifying device and interface criteria
- [AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria](aausbaccessorymatchingcriteria/devicematchingcriteria.md)
  A structure you provide that enumerates which device characteristics to search for.
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria](aausbaccessorymatchingcriteria/interfacematchingcriteria.md)
  A structure you provide that enumerates which device interface characteristics to search for.
### Matching options
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption](aausbaccessorymatchingcriteria/interfacematchingoption.md)
  Values that represent options for performing interface matching using interface matching criteria.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria)*