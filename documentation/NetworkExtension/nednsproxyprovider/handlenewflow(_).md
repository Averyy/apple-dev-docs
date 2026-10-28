# handleNewFlow(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Handles a new flow of DNS traffic.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func handleNewFlow(_ flow: NEAppProxyFlow) -> Bool
```

```objc
- (BOOL) handleNewFlow:(NEAppProxyFlow *) flow;
```

## Return Value

A Boolean value set to [`true`](../../Swift/true.md) if the proxy implementation decides to handle the flow, or [`false`](../../Swift/false.md) if it instead decides to terminate the flow.

## Discussion

The system calls this method to deliver a new network data flow to the proxy provider implementation. Subclasses must override this method to perform whatever steps are necessary to ready the proxy to receive data from the flow.

The proxy provider indicates that the proxy is ready to handle flow data by calling the flow’s [`open(withLocalEndpoint:completionHandler:)`](../neappproxyflow/open%28withlocalendpoint,completionhandler%29.md) method.

If the proxy implementation decides to handle the flow, it’s responsible for retaining a reference to the flow instance.

## Parameters

- `flow`: The flow representing the DNS traffic that the proxy should handle.

## See Also

### Handling proxied DNS flow
- [func handleNewUDPFlow(NEAppProxyUDPFlow, initialRemoteEndpoint: NWEndpoint) -> Bool](./handlenewudpflow%28_,initialremoteendpoint%29.md)
  Handles a new flow of UDP traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyprovider/handlenewflow(_:))*