# Framer

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
struct Framer<T> where T : FramerProtocol
```

## Topics

### Initializers
- [init<BelowProtocol>(() -> BelowProtocol)](framer/init(_:)-4jsj5.md)
- [init<BelowProtocol>(() -> BelowProtocol)](framer/init(_:)-7946z.md)
- [init(using: T.Type)](framer/init(using:).md)
- [init<BelowProtocol>(using: T.Type, () -> BelowProtocol)](framer/init(using:_:)-16qam.md)
- [init<BelowProtocol>(using: T.Type, () -> BelowProtocol)](framer/init(using:_:)-94t7p.md)
### Instance Properties
- [let belowProtocol: any NetworkProtocolOptions](framer/belowprotocol.md)
- [var options: NWProtocolFramer.Options](framer/options.md)
### Type Methods
- [static func receive<ConnectionType>(connection: ConnectionType) async throws -> Framer<T>.Message<Data>](framer/receive(connection:).md)
- [static func send<ConnectionType>(connection: ConnectionType, content: Data, metadata: Framer<T>.Metadata) async throws](framer/send(connection:content:metadata:).md)

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/framer)*