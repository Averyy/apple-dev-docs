# startWirelessControllerDiscovery(completionHandler:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Type Method

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
class func startWirelessControllerDiscovery(completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
class func startWirelessControllerDiscovery() async
```

```objc
+ (void) startWirelessControllerDiscoveryWithCompletionHandler:(void (^)()) completionHandler;
```

#### Discussion

Call this method when the user chooses to discover wireless controllers from your interface. The framework searches asynchronously for discoverable wireless controllers. The framework posts the [`GCControllerDidConnect`](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidconnect.md) (Swift) or [`GCControllerDidConnectNotification`](../gccontrollerdidconnectnotification.md) (Objective-C) notification when it discovers new controllers. Implement the completion handler you pass to this method to handle when the framework finishes discovering controllers or when it times out.

If you call the [`startWirelessControllerDiscovery(completionHandler:)`](./startwirelesscontrollerdiscovery%28completionhandler%29.md) method multiple times during discovery, the framework only calls the last completion handler you pass to this method.

## Parameters

- `completionHandler`: The block that the framework calls when it completes the request.

## See Also

### Discovering controllers
- [class func controllers() -> [GCController]](./controllers%28%29.md)
  Returns the connected controllers for the device.
- [class func stopWirelessControllerDiscovery()](./stopwirelesscontrollerdiscovery%28%29.md)
  Stops searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.
- [GCControllerDidConnectNotification](../gccontrollerdidconnectnotification.md)
  A notification that posts after a controller connects to the device.
- [GCControllerDidDisconnectNotification](../gccontrollerdiddisconnectnotification.md)
  A notification that posts after a controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/startwirelesscontrollerdiscovery(completionhandler:))*