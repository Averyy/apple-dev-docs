# cancel()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Cancel the session.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_cancel(_:)`](../../Network/nw_connection_cancel%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## Discussion

Move into the `NWUDPSessionStateCancelled` state. The connection will be terminated, and all handlers will be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/cancel())*