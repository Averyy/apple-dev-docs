# Coder

**Framework**: Network  
**Kind**: struct

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
struct Coder<Sending, _Receiving, CoderType> where Sending : Encodable, _Receiving : Decodable, CoderType : NetworkCoder
```

## Topics

### Initializers
- [init(Sending.Type, using: CoderType)](coder/init(_:using:).md)
- [init<BelowProtocol>(Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(_:using:_:)-61vdl.md)
- [init<BelowProtocol>(Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(_:using:_:)-8o8kw.md)
- [init<BelowProtocol>(receiving: Coder<Sending, _Receiving, CoderType>.Receiving.Type, sending: Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(receiving:sending:using:_:)-4mm04.md)
- [init<BelowProtocol>(receiving: Coder<Sending, _Receiving, CoderType>.Receiving.Type, sending: Sending.Type, using: CoderType, () -> BelowProtocol)](coder/init(receiving:sending:using:_:)-7d2qd.md)
- [init(sending: Sending.Type, receiving: Coder<Sending, _Receiving, CoderType>.Receiving.Type, using: CoderType)](coder/init(sending:receiving:using:).md)
- [init<BelowProtocol>(sending: Sending.Type, receiving: Coder<Sending, _Receiving, CoderType>.Receiving.Type, using: CoderType, () -> BelowProtocol)](coder/init(sending:receiving:using:_:)-1579q.md)
- [init<BelowProtocol>(sending: Sending.Type, receiving: Coder<Sending, _Receiving, CoderType>.Receiving.Type, using: CoderType, () -> BelowProtocol)](coder/init(sending:receiving:using:_:)-7ox25.md)
### Instance Properties
- [let belowProtocol: any NetworkProtocolOptions](coder/belowprotocol.md)

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/coder)*