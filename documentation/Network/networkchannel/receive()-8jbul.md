# receive()

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Receive data on a connection.

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
func receive<T>() async throws -> ApplicationProtocol.Message<Data> where ApplicationProtocol == Framer<T>, T : FramerProtocol
```

Available when `ApplicationProtocol` conforms to `NetworkProtocolOptions`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/receive()-8jbul)*