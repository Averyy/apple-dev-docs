# usbAccessoryDidConnect(_:)

**Framework**: Accessory Access  
**Kind**: method  
**Role**: Instance Method

The method the framework invokes when a USB accessory connects to the system.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func usbAccessoryDidConnect(_ usbAccessory: AAUSBAccessory)
```

```objc
- (void) usbAccessoryDidConnect:(AAUSBAccessory *) usbAccessory;
```

## Discussion

This method is invoked every time a USB accessory, that satisfies the matching criteria this listener registered with `AAUSBAccessoryManager` with, is connected to the system.

The framework invokes method on an arbitrary thread.

## Parameters

- `usbAccessory`: The USB accessory that connected to the system.

## See Also

### Protocol methods
- [func usbAccessoryDidDisconnect(AAUSBAccessory)](./usbaccessorydiddisconnect%28_%29.md)
  The method the framework invokes when a USB accessory disconnects from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener/usbaccessorydidconnect(_:))*