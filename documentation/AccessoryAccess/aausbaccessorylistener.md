# AAUSBAccessoryListener

**Framework**: Accessory Access  
**Kind**: protocol  
**Role**: Protocol

A class that conforms to the framework’s USB accessory listener protocol can listen to the accessory events.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol AAUSBAccessoryListener : NSObjectProtocol, Sendable
```

```objc
@protocol AAUSBAccessoryListener <NSObject>
```

## Discussion

This protocol provides methods that notify your app when a USB accessory connects to or disconnects from the system.  The framework invokes the methods for a listener on the internal serial queue of [`AAUSBAccessoryManager`](./aausbaccessorymanager.md).

## Topics

### Protocol methods
- [func usbAccessoryDidConnect(AAUSBAccessory)](./aausbaccessorylistener/usbaccessorydidconnect%28_%29.md)
  The method the framework invokes when a USB accessory connects to the system.
- [func usbAccessoryDidDisconnect(AAUSBAccessory)](./aausbaccessorylistener/usbaccessorydiddisconnect%28_%29.md)
  The method the framework invokes when a USB accessory disconnects from the system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener)*