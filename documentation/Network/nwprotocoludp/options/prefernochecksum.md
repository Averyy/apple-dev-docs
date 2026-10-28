# preferNoChecksum

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean that configures the connection to not send UDP checksums.

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
var preferNoChecksum: Bool { get set }
```

## Discussion

UDP checksums are optional when the datagrams are sent over IPv4. This option configures UDP to not set checksums on these datagrams, but has no effect on IPv6.

## See Also

### Customizing UDP Connections
- [init()](./init%28%29.md)
  Initializes a default set of UDP connection options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoludp/options/prefernochecksum)*