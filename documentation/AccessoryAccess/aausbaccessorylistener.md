# AAUSBAccessoryListener

**Framework**: Accessory Access  
**Kind**: protocol

A class that conforms to the framework’s USB accessory listener protocol can listen to the accessory events.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol AAUSBAccessoryListener : NSObjectProtocol, Sendable
```

#### Discussion

This protocol provides methods that notify your app when a USB accessory connects to or disconnects from the system.  The framework invokes the methods for a listener on the internal serial queue of [`AAUSBAccessoryManager`](aausbaccessorymanager.md).

## Topics

### Protocol methods
- [func usbAccessoryDidConnect(AAUSBAccessory)](aausbaccessorylistener/usbaccessorydidconnect(_:).md)
  The method the framework invokes when a USB accessory connects to the system.
- [func usbAccessoryDidDisconnect(AAUSBAccessory)](aausbaccessorylistener/usbaccessorydiddisconnect(_:).md)
  The method the framework invokes when a USB accessory disconnects from the system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener)*