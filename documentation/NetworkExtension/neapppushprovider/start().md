# start()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) start;
```

## Discussion

An [`NEAppPushProvider`](../neapppushprovider.md) subclass must override this method to create a connection with its server.

## See Also

### Implementing provider life cycle
- [func start(completionHandler: ((any Error)?) -> Void)](./start%28completionhandler%29.md)
  Indicates that the framework has started the provider, and provides a completion handler for subclasses to signal their readiness.
- [func stop(with: NEProviderStopReason, completionHandler: () -> Void)](./stop%28with,completionhandler%29.md)
  Indicates that the framework needs to stop the provider.
- [func handleTimerEvent()](./handletimerevent%28%29.md)
  Indicates a periodic status check from the framework to the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/start())*