# AAUSBAccessoryMatchingCriteria

**Framework**: Accessory Access  
**Kind**: class  
**Role**: Class

A class that represents the accessory matching criteria for a USB accessory.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class AAUSBAccessoryMatchingCriteria
```

```objc
@interface AAUSBAccessoryMatchingCriteria : NSObject
```

#### Discussion

A class that conforms to the [`AAUSBAccessoryListener`](./aausbaccessorylistener.md) protocol can use [`AAUSBAccessoryMatchingCriteria`](./aausbaccessorymatchingcriteria.md) objects to register itself with [`AAUSBAccessoryManager`](./aausbaccessorymanager.md).

## Topics

### Creating matching criteria
- [init?(deviceMatchingDictionary: [String : any Sendable])](./aausbaccessorymatchingcriteria/init%28devicematchingdictionary%29.md)
  Initializes a criteria object using a USB device matching dictionary.
- [init?(deviceMatchingDictionary: [String : any Sendable]?, interfaceMatchingDictionaries: [[String : any Sendable]], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./aausbaccessorymatchingcriteria/init%28devicematchingdictionary,interfacematchingdictionaries,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching dictionaries, for the provided USB device matching criteria.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria)](./aausbaccessorymatchingcriteria/init%28devicematchingcriteria%29.md)
  Initializes a criteria object with the provided USB device matching properties.
- [convenience init(deviceMatchingCriteria: AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria?, interfaceMatchingCriteria: [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria], interfaceMatchingOption: AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption)](./aausbaccessorymatchingcriteria/init%28devicematchingcriteria,interfacematchingcriteria,interfacematchingoption%29.md)
  Initializes a criteria object using USB interface matching criteria, for the given USB device matching criteria.
### Specifying device and interface criteria
- [AAUSBAccessoryMatchingCriteria.DeviceMatchingCriteria](./aausbaccessorymatchingcriteria/devicematchingcriteria.md)
  A structure you provide that enumerates which device characteristics to search for.
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingCriteria](./aausbaccessorymatchingcriteria/interfacematchingcriteria.md)
  A structure you provide that enumerates which device interface characteristics to search for.
### Matching options
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption](./aausbaccessorymatchingcriteria/interfacematchingoption.md)
  Values that represent options for performing interface matching using interface matching criteria.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria)*