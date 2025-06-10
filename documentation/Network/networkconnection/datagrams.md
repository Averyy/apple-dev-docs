# datagrams

**Framework**: Network  
**Kind**: property

Access a `SubConnection` object to send connection-wide unreliable datagrams over QUIC. Subsequent accesses to this object will return the same reference. All incoming datagrams for the entire QUIC connection will be received on this `SubConnection` once invoked.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final var datagrams: NetworkConnection<QUIC>.SubConnection<QUICDatagram> { get async throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/datagrams)*