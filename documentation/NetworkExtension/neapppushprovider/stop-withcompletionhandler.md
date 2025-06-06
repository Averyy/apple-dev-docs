# stop(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Indicates that the framework needs to stop the provider.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func stop(with reason: NEProviderStopReason) async
```

## Mentions

- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)

#### Discussion

An [`NEAppPushProvider`](neapppushprovider.md) subclass must override this method to perform any necessary tasks when stopping communication with the server.

## Parameters

- `reason`: An   that indicates why the provider needs to stop.
- `completionHandler`: A block that your provider subclass calls after it completely stops.

## See Also

- [func start()](neapppushprovider/start.md)
  Indicates that the framework has started the provider.
- [func start(completionHandler: ((any Error)?) -> Void)](neapppushprovider/start(completionhandler:).md)
  Indicates that the framework has started the provider, and provides a completion handler for subclasses to signal their readiness.
- [func handleTimerEvent()](neapppushprovider/handletimerevent.md)
  Indicates a periodic status check from the framework to the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/stop(with:completionhandler:))*