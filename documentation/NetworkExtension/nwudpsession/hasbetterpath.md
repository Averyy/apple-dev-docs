# hasBetterPath

**Framework**: Network Extension  
**Kind**: property

If a session has a better path, new session would use a different interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var hasBetterPath: Bool { get }
```

#### Discussion

Evaluates to [`true`](https://developer.apple.com/documentation/swift/true) if a new session to the remote endpoint would use a different and preferred path. If the current session is not viable, this can be used as a hint to try again. If the current session is still viable, this can indicate that the system or user has a preference for the newly available network path. For example, if the session is established over a cellular data network and Wi-Fi is now available, then the session has a better path available and this property is set to [`true`](https://developer.apple.com/documentation/swift/true). Use the `initWithUpgradeForSession:` initializer to create a new session with the same parameters as the current session. Use Key-Value Observing to watch this property.

## See Also

- [var isViable: Bool](nwudpsession/isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.
- [init(upgradeFor: NWUDPSession)](nwudpsession/init(upgradefor:).md)
  This convenience initializer can be used to create a new session based on the original session’s endpoint and parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/hasbetterpath)*