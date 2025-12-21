# TLV

**Framework**: Network  
**Kind**: struct

A Type-Length-Value (TLV) framing protocol.

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
struct TLV
```

#### Overview

This protocol will infer the length of the data based on the content passed to it in send.

Supports sending and receiving messages.

## Topics

### Initializers
- [init<BelowProtocol>(() -> BelowProtocol)](tlv/init(_:)-8ka4w.md)
- [init<BelowProtocol>(() -> BelowProtocol)](tlv/init(_:)-8qsbh.md)
- [init<T, L, BelowProtocol>(type: T.Type, length: L.Type, () -> BelowProtocol)](tlv/init(type:length:_:)-7awe.md)
  Create TLV with the specified sizes for the type and length fields.
- [init<T, L, BelowProtocol>(type: T.Type, length: L.Type, () -> BelowProtocol)](tlv/init(type:length:_:)-h8s.md)
  Create TLV with the specified sizes for the type and length fields.

## Relationships

### Conforms To
- [MessageProtocol](messageprotocol.md)
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tlv)*