# handleNewFlow(_:)

**Framework**: Network Extension  
**Kind**: method

Handle a new flow of network data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func handleNewFlow(_ flow: NEAppProxyFlow) -> Bool
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

#### Return Value

Return [`true`](https://developer.apple.com/documentation/Swift/true) to indicate that the App Proxy Provider will handle the flow. Return [`false`](https://developer.apple.com/documentation/Swift/false) to indicate that the flow should be closed.

#### Discussion

This method is called by the system whenever an app which matches the current App Proxy configuration’s app rules opens a new network connection.

`NEAppProxyProvider` subclasses must override this method.

New flows are initially in an unopened state. The App Proxy Provider should take whatever steps are necessary to ready itself to handle the flow data and then open the flow.

## Parameters

- `flow`: The new   object. If the App Proxy Provider decides to proxy the flow, it should create a reference to the flow in its data structures.

## See Also

- [func handleNewUDPFlow(NEAppProxyUDPFlow, initialRemoteEndpoint: NWEndpoint) -> Bool](neappproxyprovider/handlenewudpflow(_:initialremoteendpoint:).md)
  Handle a new UDP flow of network data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider/handlenewflow(_:))*