# datagrams

**Framework**: Network  
**Kind**: property

Access connection-wide unreliable datagrams over QUIC. Subsequent accesses to this object will return the same reference. All incoming datagrams for the entire QUIC connection will be received on this `SubConnection` once invoked.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final var datagrams: QUIC.Datagrams<QUICDatagram> { get async throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/datagrams)*