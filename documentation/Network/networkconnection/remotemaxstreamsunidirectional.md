# remoteMaxStreamsUnidirectional

**Framework**: Network  
**Kind**: property

Get the maximum number of unidirectional streams advertised by peer that an application is allowed to create.

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
final var remoteMaxStreamsUnidirectional: Int { get }
```

#### Discussion

Note that while attempts to create streams above this limit will be blocked until the server increases the limit, these blocked attempts will cause a STREAMS_BLOCKED frame to be sent to the server. This informs the server that the client has more streams it would like to create. As a result, the caller should attempt to create streams over this limit if it desires more streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/remotemaxstreamsunidirectional)*