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

- `localEndpoint`: Pass   to have the system derive a value based on the address of the current primary physical interface.
- `completionHandler`: Called when the open operation is complete. This block has no return value and takes the following parameter:

## See Also

- [func closeReadWithError((any Error)?)](neappproxyflow/closereadwitherror(_:).md)
  Close the flow for further read operations.
- [func closeWriteWithError((any Error)?)](neappproxyflow/closewritewitherror(_:).md)
  Close the flow for further write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/open(withlocalendpoint:completionhandler:))*