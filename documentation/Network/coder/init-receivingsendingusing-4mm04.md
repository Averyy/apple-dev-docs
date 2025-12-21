# init(receiving:sending:using:_:)

**Framework**: Network  
**Kind**: init

Create a Coder protocol.

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
init<BelowProtocol>(receiving: Receiving.Type, sending: Sending.Type, using: CoderType, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : StreamProtocol
```

## Parameters

- `receiving`: The Codable type that will be received.
- `sending`: The Codable type that will be sent.
- `using`: The NetworkCoder that will be used to encode and decode.
- `builder`: The protocol stack below Coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/coder/init(receiving:sending:using:_:)-4mm04)*