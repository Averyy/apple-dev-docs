# keepaliveCount

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The number of keepalive probes that TCP sends before terminating the connection.

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
var keepaliveCount: Int { get set }
```

## See Also

### Configuring Keepalives
- [var enableKeepalive: Bool](./enablekeepalive.md)
  A Boolean that enables TCP keepalives.
- [var keepaliveIdle: Int](./keepaliveidle.md)
  The number of seconds of idleness that TCP waits before sending keepalive probes.
- [var keepaliveInterval: Int](./keepaliveinterval.md)
  The number of seconds that TCP waits between sending keepalive probes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options/keepalivecount)*