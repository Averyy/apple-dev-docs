# messages

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

Receive data from a connection as an async stream.

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
var messages: AsyncThrowingStream<ApplicationProtocol.Message<ApplicationProtocol.ContentType>, any Error> { get }
```

Available when `ApplicationProtocol` conforms to `MessageProtocol`.

## Discussion

This may be called before the connection is ready, in which case the receive requests will be enqueued until the connection is ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/messages)*