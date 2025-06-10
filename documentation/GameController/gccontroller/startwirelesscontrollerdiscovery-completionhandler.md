# startWirelessControllerDiscovery(completionHandler:)

**Framework**: Game Controller  
**Kind**: method

Starts searching for nearby wireless controllers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func startWirelessControllerDiscovery() async
```

#### Discussion

Call this method when the user chooses to discover wireless controllers from your interface. The framework searches asynchronously for discoverable wireless controllers. The framework posts the [`GCControllerDidConnect`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/GCControllerDidConnect) (Swift) or [`GCControllerDidConnectNotification`](gccontrollerdidconnectnotification.md) (Objective-C) notification when it discovers new controllers. Implement the completion handler you pass to this method to handle when the framework finishes discovering controllers or when it times out.

If you call the [`startWirelessControllerDiscovery(completionHandler:)`](gccontroller/startwirelesscontrollerdiscovery(completionhandler:).md) method multiple times during discovery, the framework only calls the last completion handler you pass to this method.

## Parameters

- `completionHandler`: The block that the framework calls when it completes the request.

## See Also

- [class func controllers() -> [GCController]](gccontroller/controllers.md)
  Returns the connected controllers for the device.
- [class func stopWirelessControllerDiscovery()](gccontroller/stopwirelesscontrollerdiscovery.md)
  Stops searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidConnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidDisconnect.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/startwirelesscontrollerdiscovery(completionhandler:))*