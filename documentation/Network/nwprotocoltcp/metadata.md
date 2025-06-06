# NWProtocolTCP.Metadata

**Framework**: Network  
**Kind**: class

A handle you can use to inspect a connection’s TCP state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class Metadata
```

## Topics

### Inspecting TCP State
- [var availableSendBuffer: UInt32](nwprotocoltcp/metadata/availablesendbuffer.md)
  The number of available bytes in the TCP send buffer.
- [var availableReceiveBuffer: UInt32](nwprotocoltcp/metadata/availablereceivebuffer.md)
  The number of available bytes in the TCP receive buffer.

## Relationships

### Inherits From
- [NWProtocolMetadata](nwprotocolmetadata.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/metadata)*