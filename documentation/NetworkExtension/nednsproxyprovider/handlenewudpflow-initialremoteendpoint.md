# handleNewUDPFlow(_:initialRemoteEndpoint:)

**Framework**: Network Extension  
**Kind**: method

Handles a new flow of UDP traffic.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func handleNewUDPFlow(_ flow: NEAppProxyUDPFlow, initialRemoteEndpoint remoteEndpoint: NWEndpoint) -> Bool
```

#### Discussion

The framework calls this function to deliver a new UDP data flow to the proxy provider implementation. Subclasses can override this method to perform whatever steps are necessary to ready the proxy to receive data from the flow.

If you decide to handle the flow, the subclass implementation of this method should return [`true`](https://developer.apple.com/documentation/swift/true). In this case, your implementation is responsible for retaining the [`NEAppProxyUDPFlow`](neappproxyudpflow.md) object.

Your implementation indicates that it’s ready to handle flow data by calling [`open(withLocalEndpoint:completionHandler:)`](neappproxyflow/open(withlocalendpoint:completionhandler:).md) on the flow.

If you decide to not handle the flow and instead terminate it, your implementation of this method should return [`false`](https://developer.apple.com/documentation/swift/false). This terminates the flow.

The default implementation of this method calls [`handleNewFlow(_:)`](neappproxyprovider/handlenewflow(_:).md) and returns its result.

## Parameters

- `flow`: The new UDP flow.
- `remoteEndpoint`: The initial remote endpoint provided by the proxied app when the flow was opened.

## See Also

- [func handleNewFlow(NEAppProxyFlow) -> Bool](nednsproxyprovider/handlenewflow(_:).md)
  Handles a new flow of DNS traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyprovider/handlenewudpflow(_:initialremoteendpoint:))*