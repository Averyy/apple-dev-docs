# writeDatagrams(_:sentBy:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Write datagrams to the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func writeDatagrams(_ datagrams: [Data], sentBy remoteEndpoints: [NWEndpoint]) async throws
```

## Parameters

- `datagrams`: An array of   objects containing datagram payloads to be written.
- `remoteEndpoints`: An array of   objects containing the source endpoints of the datagram payloads in  .
- `completionHandler`: A block that will be executed by the system on an internal system thread when the data is written into the receive buffer of the socket associated with the flow. If an error occurs while writing the data then a non-nil   object is passed to the block. See   in   for a list of possible errors.

## See Also

- [func readDatagrams(completionHandler: ([Data]?, [NWEndpoint]?, (any Error)?) -> Void)](neappproxyudpflow/readdatagrams(completionhandler:)-9z8gw.md)
  Read datagrams from the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/writedatagrams(_:sentby:completionhandler:))*