# init(upgradeFor:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

This convenience initializer can be used to create a new session based on the original session’s endpoint and parameters.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_create(_:_:)`](../../Network/nw_connection_create%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
init(upgradeFor session: NWUDPSession)
```

```objc
- (instancetype) initWithUpgradeForSession:(NWUDPSession *) session;
```

#### Discussion

The caller should watch the `hasBetterPath` property on an existing [`NWUDPSession`](../nwudpsession.md) object. When `hasBetterPath` is [`true`](../../Swift/true.md), the caller should call `initWithUpgradeForSession:` to create a new session, then start transferring data on the new session as soon as possible to reduce power and and avoid expensive networks. When the new session is ready, the application can start using the new session and tear down the original one.

## See Also

### Responding to network changes
- [var hasBetterPath: Bool](./hasbetterpath.md)
  If a session has a better path, new session would use a different interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/init(upgradefor:))*