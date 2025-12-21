# Framer

**Framework**: Network  
**Kind**: struct

An instance of a Framer protocol to load into a protocol stack.

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
struct Framer<T> where T : FramerProtocol
```

## Topics

### Initializers
- [init<BelowProtocol>(() -> BelowProtocol)](framer/init(_:)-4jsj5.md)
  Create a Framer protocol for use in a protocol stack.
- [init<BelowProtocol>(() -> BelowProtocol)](framer/init(_:)-7946z.md)
  Create a Framer protocol for use in a protocol stack.
- [init<BelowProtocol>(using: T.Type, () -> BelowProtocol)](framer/init(using:_:)-16qam.md)
  Create a Framer protocol for use in a protocol stack.
- [init<BelowProtocol>(using: T.Type, () -> BelowProtocol)](framer/init(using:_:)-94t7p.md)
  Create a Framer protocol for use in a protocol stack.
### Instance Properties
- [var options: NWProtocolFramer.Options](framer/options.md)
  The framer options to use with this framer.

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/framer)*