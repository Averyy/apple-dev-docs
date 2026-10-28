# handleNewUDPFlow(_:initialRemoteEndpoint:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Handle a new UDP flow of network data.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func handleNewUDPFlow(_ flow: NEAppProxyUDPFlow, initialRemoteEndpoint remoteEndpoint: NWEndpoint) -> Bool
```

```objc
- (BOOL) handleNewUDPFlow:(NEAppProxyUDPFlow *) flow initialRemoteEndpoint:(NWEndpoint *) remoteEndpoint;
```

## Discussion

The framework calls this function to deliver a new UDP data flow to the proxy provider implementation. Subclasses can override this method to perform whatever steps are necessary to ready the proxy to receive data from the flow.

If you decide to handle the flow, the subclass implementation of this method should return [`true`](../../Swift/true.md). In this case, your implementation is responsible for retaining the [`NEAppProxyUDPFlow`](../neappproxyudpflow.md) object.

Your implementation indicates that it’s ready to handle flow data by calling [`open(withLocalEndpoint:completionHandler:)`](../neappproxyflow/open%28withlocalendpoint,completionhandler%29.md) on the flow.

If you decide to not handle the flow and instead terminate it, your implementation of this method should return [`false`](../../Swift/false.md). This terminates the flow.

The default implementation of this method calls [`handleNewFlow(_:)`](./handlenewflow%28_%29.md) and returns its result.

## Parameters

- `flow`: The new UDP flow.
- `remoteEndpoint`: The initial remote endpoint provided by the proxied app when the flow was opened.

## See Also

### Handling proxied flows
- [func handleNewFlow(NEAppProxyFlow) -> Bool](./handlenewflow%28_%29.md)
  Handle a new flow of network data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider/handlenewudpflow(_:initialremoteendpoint:))*