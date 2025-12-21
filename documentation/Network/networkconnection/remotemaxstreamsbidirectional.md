# remoteMaxStreamsBidirectional

**Framework**: Network  
**Kind**: property

Get the maximum number of bidirectional streams advertised by peer that an application is allowed to create.

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
final var remoteMaxStreamsBidirectional: Int { get }
```

#### Discussion

Note that while attempts to create streams above this limit will be blocked until the server increases the limit, these blocked attempts will cause a STREAMS_BLOCKED frame to be sent to the server. This informs the server that the client has more streams it would like to create. As a result, the caller should attempt to create streams over this limit if it desires more streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/remotemaxstreamsbidirectional)*