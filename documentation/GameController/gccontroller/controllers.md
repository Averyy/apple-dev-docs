# controllers()

**Framework**: Game Controller  
**Kind**: method

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

#### Return Value

The currently connected controllers.

#### Discussion

To track the connection status of controllers, observe the framework notifications. The framework posts the [`GCControllerDidConnect`](https://developer.apple.com/documentation/foundation/nsnotification/name/1458856-gccontrollerdidconnect) (Swift) and [`GCControllerDidBecomeCurrent`](https://developer.apple.com/documentation/foundation/nsnotification/name/3547191-gccontrollerdidbecomecurrent) (Swift) notifications when a controller connects to a device. For Objective-C, it posts the [`GCControllerDidConnectNotification`](gccontrollerdidconnectnotification.md) and [`GCControllerDidBecomeCurrentNotification`](gccontrollerdidbecomecurrentnotification.md) notifications. When a controller disconnects from a device, it posts the [`GCControllerDidDisconnect`](https://developer.apple.com/documentation/foundation/nsnotification/name/1458875-gccontrollerdiddisconnect) (Swift) and [`GCControllerDidStopBeingCurrent`](https://developer.apple.com/documentation/foundation/nsnotification/name/3547192-gccontrollerdidstopbeingcurrent) (Swift) notifications. For Objective-C, it posts the [`GCControllerDidDisconnectNotification`](gccontrollerdiddisconnectnotification.md) and [`GCControllerDidStopBeingCurrentNotification`](gccontrollerdidstopbeingcurrentnotification.md) notifications.

## See Also

- [class func startWirelessControllerDiscovery(completionHandler: (() -> Void)?)](gccontroller/startwirelesscontrollerdiscovery(completionhandler:).md)
  Starts searching for nearby wireless controllers.
- [class func stopWirelessControllerDiscovery()](gccontroller/stopwirelesscontrollerdiscovery.md)
  Stops searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../foundation/nsnotification/name/1458856-gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../foundation/nsnotification/name/1458875-gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/controllers())*