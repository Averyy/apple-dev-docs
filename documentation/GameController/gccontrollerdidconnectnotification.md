# GCControllerDidConnectNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a controller connects to the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const GCControllerDidConnectNotification;
```

## Mentions

- [Adding virtual controls to games that support game controllers in iOS](./adding-virtual-controls-to-games-that-support-game-controllers-in-ios.md)
- [Discovering game controllers](./discovering-game-controllers.md)

## Discussion

The notification object is the [`GCController`](./gccontroller.md) object that connects to the device.

The system posts this notification on the main thread.

## See Also

### Discovering controllers
- [class func controllers() -> [GCController]](./gccontroller/controllers%28%29.md)
  Returns the connected controllers for the device.
- [class func startWirelessControllerDiscovery(completionHandler: (() -> Void)?)](./gccontroller/startwirelesscontrollerdiscovery%28completionhandler%29.md)
  Starts searching for nearby wireless controllers.
- [class func stopWirelessControllerDiscovery()](./gccontroller/stopwirelesscontrollerdiscovery%28%29.md)
  Stops searching for nearby wireless controllers.
- [GCControllerDidDisconnectNotification](./gccontrollerdiddisconnectnotification.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdidconnectnotification)*