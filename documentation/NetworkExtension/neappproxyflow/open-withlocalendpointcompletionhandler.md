# open(withLocalEndpoint:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Opens the flow, indicating to the system that the caller is ready to start receiving and sending data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func open(withLocalEndpoint localEndpoint: NWHostEndpoint?) async throws
```

#### Discussion

An [`NEAppProxyFlow`](neappproxyflow.md) object starts out in the unopened state. When the system passes a flow to your app proxy provider by calling [`handleNewFlow(_:)`](neappproxyprovider/handlenewflow(_:).md), to need to set up the state necessary to handle the flow’s data, and then call this method.

## Parameters

- `localEndpoint`: An [`NWHostEndpoint`](nwhostendpoint.md) object that contains the address and port to set as the local address and local port of the flow. The system supplies this information to the app that triggered the creation of this flow in different ways, depending on the networking API the app used. For example, if the app used the Network framework, it gets this information from the [`localEndpoint`](https://developer.apple.com/documentation/network/nwpath/localendpoint) property of the current path. If it used BSD Sockets, it gets this information by calling `getsockname`. Pass `nil` to have the system derive a value based on the address of the current primary physical interface.
- `completionHandler`: Called when the open operation is complete. This block has no return value and takes the following parameter: - **error**: A `nil` value indicates the flow opened successfully. A non-`nil` value indicates the flow could not be opened. See [`NEAppProxyFlowError`](neappproxyflowerror-swift.struct.md) for a list of expected error codes.

## See Also

- [func closeReadWithError((any Error)?)](neappproxyflow/closereadwitherror(_:).md)
  Close the flow for further read operations.
- [func closeWriteWithError((any Error)?)](neappproxyflow/closewritewitherror(_:).md)
  Close the flow for further write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/open(withlocalendpoint:completionhandler:))*