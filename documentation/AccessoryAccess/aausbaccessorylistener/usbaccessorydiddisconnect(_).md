# usbAccessoryDidDisconnect(_:)

**Framework**: Accessory Access  
**Kind**: method  
**Role**: Instance Method

The method the framework invokes when a USB accessory disconnects from the system.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func usbAccessoryDidDisconnect(_ usbAccessory: AAUSBAccessory)
```

```objc
- (void) usbAccessoryDidDisconnect:(AAUSBAccessory *) usbAccessory;
```

#### Discussion

This method is invoked every time a USB accessory, for which the listener received the connect notification, is disconnected from the system.

This method will be invoked on an arbitrary thread.

## Parameters

- `usbAccessory`: The USB accessory that disconnected from the system.

## See Also

### Protocol methods
- [func usbAccessoryDidConnect(AAUSBAccessory)](./usbaccessorydidconnect%28_%29.md)
  The method the framework invokes when a USB accessory connects to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener/usbaccessorydiddisconnect(_:))*