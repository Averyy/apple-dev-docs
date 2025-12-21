# Coder

**Framework**: Network  
**Kind**: struct

A protocol that frames and encodes/decodes Codable types.

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
struct Coder<Sending, Receiving, CoderType> where Sending : Encodable, Receiving : Decodable, CoderType : NetworkCoder
```

#### Overview

Supports sending and receiving Codable types using a specified format.

## Topics

### Initializers
- [init<BelowProtocol>(Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(_:using:_:)-61vdl.md)
  Create a Coder protocol.
- [init<BelowProtocol>(Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(_:using:_:)-8o8kw.md)
  Create a Coder protocol.
- [init<BelowProtocol>(receiving: Receiving.Type, sending: Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(receiving:sending:using:_:)-4mm04.md)
  Create a Coder protocol.
- [init<BelowProtocol>(receiving: Receiving.Type, sending: Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(receiving:sending:using:_:)-7d2qd.md)
  Create a Coder protocol
- [init<BelowProtocol>(sending: Sending.Type, receiving: Receiving.Type, using: CoderType, () -> BelowProtocol)](coder/init(sending:receiving:using:_:)-1579q.md)
  Create a Coder protocol
- [init<BelowProtocol>(sending: Sending.Type, receiving: Receiving.Type, using: CoderType, () -> BelowProtocol)](coder/init(sending:receiving:using:_:)-7ox25.md)
  Create a Coder protocol.

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/coder)*