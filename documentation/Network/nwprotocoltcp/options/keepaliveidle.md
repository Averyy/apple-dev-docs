# keepaliveIdle

**Framework**: Network  
**Kind**: property

The number of seconds of idleness that TCP waits before sending keepalive probes.

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
var keepaliveIdle: Int { get set }
```

## See Also

- [var enableKeepalive: Bool](nwprotocoltcp/options/enablekeepalive.md)
  A Boolean that enables TCP keepalives.
- [var keepaliveCount: Int](nwprotocoltcp/options/keepalivecount.md)
  The number of keepalive probes that TCP sends before terminating the connection.
- [var keepaliveInterval: Int](nwprotocoltcp/options/keepaliveinterval.md)
  The number of seconds that TCP waits between sending keepalive probes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options/keepaliveidle)*