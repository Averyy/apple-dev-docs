# start(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Indicates that the framework has started the provider, and provides a completion handler for subclasses to signal their readiness.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func start(completionHandler: @escaping ((any Error)?) -> Void)
```

## Mentions

- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)

#### Discussion

An [`NEAppPushProvider`](neapppushprovider.md) subclass must override this method to create a connection with its server.

## Parameters

- `completionHandler`: A Swift closure or ObjectiveC block for your provider subclass to call after it begins connecting to the server. If you can’t connect, pass a non-nil   that describes the error, otherwise pass  .

## See Also

- [func start()](neapppushprovider/start.md)
  Indicates that the framework has started the provider.
- [func stop(with: NEProviderStopReason, completionHandler: () -> Void)](neapppushprovider/stop(with:completionhandler:).md)
  Indicates that the framework needs to stop the provider.
- [func handleTimerEvent()](neapppushprovider/handletimerevent.md)
  Indicates a periodic status check from the framework to the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/start(completionhandler:))*