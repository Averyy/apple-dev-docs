# stopWirelessControllerDiscovery()

**Framework**: Game Controller  
**Kind**: method

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

#### Discussion

If you call this method while the framework searches for wireless controllers, the framework stops searching and invokes the completion handler you pass to the [`startWirelessControllerDiscovery(completionHandler:)`](gccontroller/startwirelesscontrollerdiscovery(completionhandler:).md) method.

## See Also

- [class func controllers() -> [GCController]](gccontroller/controllers.md)
  Returns the connected controllers for the device.
- [class func startWirelessControllerDiscovery(completionHandler: (() -> Void)?)](gccontroller/startwirelesscontrollerdiscovery(completionhandler:).md)
  Starts searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidConnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidDisconnect.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/stopwirelesscontrollerdiscovery())*