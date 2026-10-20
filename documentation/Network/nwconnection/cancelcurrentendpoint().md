# cancelCurrentEndpoint()

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Causes the current endpoint to be rejected, allowing the connection to try another resolved address.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
final func cancelCurrentEndpoint()
```

#### Discussion

Protocols that do not have handshakes, such as UDP, do not allow connections to validate connectivity on their own. Cancelling an endpoint allows you to indicate that a certain endpoint should be rejected due to a lack of valid response. If other addresses were resolved for the remote endpoint, those will be attempted next.

## See Also

### Canceling Connections
- [func cancel()](./cancel%28%29.md)
  Cancels the connection and gracefully disconnects any established network protocols.
- [func forceCancel()](./forcecancel%28%29.md)
  Cancels the connection and immediately disconnects any established network protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/cancelcurrentendpoint())*