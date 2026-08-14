# isViable

**Framework**: Network Extension  
**Kind**: property

The viability of a UDP session represents whether or not data can be transferred.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isViable: Bool { get }
```

#### Discussion

Evaluates to [`true`](https://developer.apple.com/documentation/swift/true) if the session can read and write data, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. Use Key-Value Observing to watch this property.

## See Also

- [var state: NWUDPSessionState](nwudpsession/state.md)
  The current state of the UDP session.
- [enum NWUDPSessionState](nwudpsessionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/isviable)*