# QUICStream

**Framework**: Network  
**Kind**: struct

A QUIC stream that runs over a QUIC connection.

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
struct QUICStream
```

#### Overview

Connections using QUICStream have a similar stream interface to TLS and TCP.

> **Note**: This type is not intended to be inserted into the protocol stack manually; it is vended by connections that use QUIC.

## Topics

### Enumerations
- [QUICStream.Directionality](quicstream/directionality.md)
- [QUICStream.Initiator](quicstream/initiator.md)

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
- [StreamProtocol](streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quicstream)*