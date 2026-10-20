# hasBetterPath

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

If a session has a better path, new session would use a different interface.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_set_better_path_available_handler(_:_:)`](../../Network/nw_connection_set_better_path_available_handler%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var hasBetterPath: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasBetterPath;
```

#### Discussion

Evaluates to [`true`](../../Swift/true.md) if a new session to the remote endpoint would use a different and preferred path. If the current session is not viable, this can be used as a hint to try again. If the current session is still viable, this can indicate that the system or user has a preference for the newly available network path. For example, if the session is established over a cellular data network and Wi-Fi is now available, then the session has a better path available and this property is set to [`true`](../../Swift/true.md). Use the `initWithUpgradeForSession:` initializer to create a new session with the same parameters as the current session. Use Key-Value Observing to watch this property.

## See Also

### Related Documentation
- [var isViable: Bool](./isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.
### Responding to network changes
- [init(upgradeFor: NWUDPSession)](./init%28upgradefor%29.md)
  This convenience initializer can be used to create a new session based on the original session’s endpoint and parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/hasbetterpath)*