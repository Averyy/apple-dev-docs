# tryNextResolvedEndpoint()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Mark the current value of resolvedEndpoint as unusable, and try to switch to the next available endpoint.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_cancel_current_endpoint(_:)`](../../Network/nw_connection_cancel_current_endpoint%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func tryNextResolvedEndpoint()
```

```objc
- (void) tryNextResolvedEndpoint;
```

#### Discussion

This should be used when the caller has attempted to communicate with the current `resolvedEndpoint`, and the caller has determined that it is unusable. If there are no other resolved endpoints, the session will move to the failed state.

## See Also

### Selecting remote endpoints
- [var resolvedEndpoint: NWEndpoint?](./resolvedendpoint.md)
  The currently targeted remote endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/trynextresolvedendpoint())*