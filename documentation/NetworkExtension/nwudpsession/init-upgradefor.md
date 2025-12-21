# init(upgradeFor:)

**Framework**: Network Extension  
**Kind**: init

This convenience initializer can be used to create a new session based on the original session’s endpoint and parameters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(upgradeFor session: NWUDPSession)
```

#### Discussion

The caller should watch the `hasBetterPath` property on an existing [`NWUDPSession`](nwudpsession.md) object. When `hasBetterPath` is [`true`](https://developer.apple.com/documentation/Swift/true), the caller should call `initWithUpgradeForSession:` to create a new session, then start transferring data on the new session as soon as possible to reduce power and and avoid expensive networks. When the new session is ready, the application can start using the new session and tear down the original one.

## See Also

- [var hasBetterPath: Bool](nwudpsession/hasbetterpath.md)
  If a session has a better path, new session would use a different interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/init(upgradefor:))*