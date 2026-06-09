# usbAccessoryDidConnect(_:)

**Framework**: Accessory Access  
**Kind**: method

The method the framework invokes when a USB accessory connects to the system.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func usbAccessoryDidConnect(_ usbAccessory: AAUSBAccessory)
```

#### Discussion

This method is invoked every time a USB accessory, that satisfies the matching criteria this listener registered with `AAUSBAccessoryManager` with, is connected to the system.

The framework invokes method on an arbitrary thread.

## Parameters

- `usbAccessory`: The USB accessory that connected to the system.

## See Also

- [func usbAccessoryDidDisconnect(AAUSBAccessory)](aausbaccessorylistener/usbaccessorydiddisconnect(_:).md)
  The method the framework invokes when a USB accessory disconnects from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener/usbaccessorydidconnect(_:))*