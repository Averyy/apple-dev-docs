# stopWirelessControllerDiscovery()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Type Method

Stops searching for nearby wireless controllers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func stopWirelessControllerDiscovery()
```

```objc
+ (void) stopWirelessControllerDiscovery;
```

## Discussion

If you call this method while the framework searches for wireless controllers, the framework stops searching and invokes the completion handler you pass to the [`startWirelessControllerDiscovery(completionHandler:)`](./startwirelesscontrollerdiscovery%28completionhandler%29.md) method.

## See Also

### Discovering controllers
- [class func controllers() -> [GCController]](./controllers%28%29.md)
  Returns the connected controllers for the device.
- [class func startWirelessControllerDiscovery(completionHandler: (() -> Void)?)](./startwirelesscontrollerdiscovery%28completionhandler%29.md)
  Starts searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.
- [GCControllerDidConnectNotification](../gccontrollerdidconnectnotification.md)
  A notification that posts after a controller connects to the device.
- [GCControllerDidDisconnectNotification](../gccontrollerdiddisconnectnotification.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/stopwirelesscontrollerdiscovery())*