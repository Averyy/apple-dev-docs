# init(_:using:_:)

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
init<BelowProtocol>(_ type: Sending.Type, using: CoderType, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : DatagramProtocol
```

## Parameters

- `type`: The Codable type that will be sent and received.
- `builder`: The protocol stack below Coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/coder/init(_:using:_:)-61vdl)*