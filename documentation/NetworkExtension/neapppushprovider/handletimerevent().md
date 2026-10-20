# handleTimerEvent()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Indicates a periodic status check from the framework to the provider.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func handleTimerEvent()
```

```objc
- (void) handleTimerEvent;
```

## Mentions

- [Maintaining a Reliable Network Connection](../maintaining-a-reliable-network-connection.md)

#### Discussion

Implement this method to have your extension check its connection to the server, and trigger a reconnect if necessary.

## See Also

### Implementing provider life cycle
- [func start()](./start%28%29.md)
  Indicates that the framework has started the provider.
- [func start(completionHandler: ((any Error)?) -> Void)](./start%28completionhandler%29.md)
  Indicates that the framework has started the provider, and provides a completion handler for subclasses to signal their readiness.
- [func stop(with: NEProviderStopReason, completionHandler: () -> Void)](./stop%28with,completionhandler%29.md)
  Indicates that the framework needs to stop the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/handletimerevent())*