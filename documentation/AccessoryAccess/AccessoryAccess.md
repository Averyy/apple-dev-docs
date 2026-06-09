# Accessory Access

**Framework**: Accessory Access  
**Kind**: module

Manage access to connected USB accessories.

**Availability**:
- macOS 27.0+ (Beta)

#### Discussion

The AccessoryAccess framework provides access to connected USB devices that use the [`IOUSBHost`](https://developer.apple.com/documentation/IOUSBHost) framework, allowing clients to express interest through one or more registered accessory listeners.

## Topics

### Managing accessories
- [class AAUSBAccessoryManager](aausbaccessorymanager.md)
  A class your app uses to manage USB accessories and the listener objects for those accessories.
- [class AAUSBAccessory](aausbaccessory.md)
  A class that represents a USB accessory.
### Identifying specific USB accessories
- [class AAUSBAccessoryMatchingCriteria](aausbaccessorymatchingcriteria.md)
  A class that represents the accessory matching criteria for a USB accessory.
### Responding to changes in accessory status
- [protocol AAUSBAccessoryListener](aausbaccessorylistener.md)
  A class that conforms to the framework’s USB accessory listener protocol can listen to the accessory events.
### Errors
- [struct AAError](aaerror.md)
  Values that describe errors the AccessoryAccess framework returns.
- [let AAErrorDomain: String](aaerrordomain.md)
  The string that represents the framework’s error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryAccess)*