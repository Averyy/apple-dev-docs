# receive()

**Framework**: Network  
**Kind**: method

Receive an object from a connection.

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
func receive<Sending, Receiving, CoderType>() async throws -> ApplicationProtocol.Message<Receiving> where ApplicationProtocol == Coder<Sending, Receiving, CoderType>, Sending : Encodable, Receiving : Decodable, CoderType : NetworkCoder
```

#### Discussion

The object will be decoded and returned. An error will be thrown if the object cannot be decoded.

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/receive()-5p11z)*