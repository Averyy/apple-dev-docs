# usbAccessoryDidDisconnect(_:)

**Framework**: Accessory Access  
**Kind**: method

The method the framework invokes when a USB accessory disconnects from the system.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func usbAccessoryDidDisconnect(_ usbAccessory: AAUSBAccessory)
```

#### Discussion

This method is invoked every time a USB accessory, for which the listener received the connect notification, is disconnected from the system.

This method will be invoked on an arbitrary thread.

## Parameters

- `usbAccessory`: The USB accessory that disconnected from the system.

## See Also

- [func usbAccessoryDidConnect(AAUSBAccessory)](aausbaccessorylistener/usbaccessorydidconnect(_:).md)
  The method the framework invokes when a USB accessory connects to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener/usbaccessorydiddisconnect(_:))*