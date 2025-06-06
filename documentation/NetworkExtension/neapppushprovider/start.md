# start()

**Framework**: Network Extension  
**Kind**: method

Indicates that the framework has started the provider.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
func start()
```

#### Discussion

An [`NEAppPushProvider`](neapppushprovider.md) subclass must override this method to create a connection with its server.

## See Also

- [func start(completionHandler: ((any Error)?) -> Void)](neapppushprovider/start(completionhandler:).md)
  Indicates that the framework has started the provider, and provides a completion handler for subclasses to signal their readiness.
- [func stop(with: NEProviderStopReason, completionHandler: () -> Void)](neapppushprovider/stop(with:completionhandler:).md)
  Indicates that the framework needs to stop the provider.
- [func handleTimerEvent()](neapppushprovider/handletimerevent.md)
  Indicates a periodic status check from the framework to the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/start())*