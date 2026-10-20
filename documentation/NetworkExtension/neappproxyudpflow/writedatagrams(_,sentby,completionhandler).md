# writeDatagrams(_:sentBy:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Write datagrams to the flow.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func writeDatagrams(_ datagrams: [Data], sentBy remoteEndpoints: [NWEndpoint], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeDatagrams(_ datagrams: [Data], sentBy remoteEndpoints: [NWEndpoint]) async throws
```

```objc
- (void) writeDatagrams:(NSArray<NSData *> *) datagrams sentByEndpoints:(NSArray<NWEndpoint *> *) remoteEndpoints completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `datagrams`: An array of [`NSData`](../../Foundation/nsdata.md) objects containing datagram payloads to be written.
- `remoteEndpoints`: An array of [`NWEndpoint`](../nwendpoint.md) objects containing the source endpoints of the datagram payloads in `datagrams`.
- `completionHandler`: A block that will be executed by the system on an internal system thread when the data is written into the receive buffer of the socket associated with the flow. If an error occurs while writing the data then a non-nil [`NSError`](../../Foundation/nserror.md) object is passed to the block. See `NEAppProxyFlowError` in [`NEAppProxyFlow`](../neappproxyflow.md) for a list of possible errors.

## See Also

### Handling flow data
- [func readDatagrams(completionHandler: ([Data]?, [NWEndpoint]?, (any Error)?) -> Void)](./readdatagrams%28completionhandler%29-9z8gw.md)
  Read datagrams from the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/writedatagrams(_:sentby:completionhandler:))*