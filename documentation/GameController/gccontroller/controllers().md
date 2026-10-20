# controllers()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Type Method

Returns the connected controllers for the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func controllers() -> [GCController]
```

```objc
+ (NSArray<GCController *> *) controllers;
```

## Mentions

- [Discovering game controllers](../discovering-game-controllers.md)
- [Discovering and tracking spatial game controllers and styli](../discovering-and-tracking-spatial-game-controllers-and-styli.md)

#### Return Value

The currently connected controllers.

#### Discussion

To track the connection status of controllers, observe the framework notifications. The framework posts the [`GCControllerDidConnect`](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidconnect.md) (Swift) and [`GCControllerDidBecomeCurrent`](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidbecomecurrent.md) (Swift) notifications when a controller connects to a device. For Objective-C, it posts the [`GCControllerDidConnectNotification`](../gccontrollerdidconnectnotification.md) and [`GCControllerDidBecomeCurrentNotification`](../gccontrollerdidbecomecurrentnotification.md) notifications. When a controller disconnects from a device, it posts the [`GCControllerDidDisconnect`](../../Foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect.md) (Swift) and [`GCControllerDidStopBeingCurrent`](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidstopbeingcurrent.md) (Swift) notifications. For Objective-C, it posts the [`GCControllerDidDisconnectNotification`](../gccontrollerdiddisconnectnotification.md) and [`GCControllerDidStopBeingCurrentNotification`](../gccontrollerdidstopbeingcurrentnotification.md) notifications.

## See Also

### Discovering controllers
- [class func startWirelessControllerDiscovery(completionHandler: (() -> Void)?)](./startwirelesscontrollerdiscovery%28completionhandler%29.md)
  Starts searching for nearby wireless controllers.
- [class func stopWirelessControllerDiscovery()](./stopwirelesscontrollerdiscovery%28%29.md)
  Stops searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/controllers())*