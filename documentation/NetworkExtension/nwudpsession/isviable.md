# isViable

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The viability of a UDP session represents whether or not data can be transferred.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_set_viability_changed_handler(_:_:)`](../../Network/nw_connection_set_viability_changed_handler%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var isViable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isViable) BOOL viable;
```

## Discussion

Evaluates to [`true`](../../Swift/true.md) if the session can read and write data, [`false`](../../Swift/false.md) otherwise. Use Key-Value Observing to watch this property.

## See Also

### Monitoring the session state
- [var state: NWUDPSessionState](./state.md)
  The current state of the UDP session.
- [enum NWUDPSessionState](../nwudpsessionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/isviable)*