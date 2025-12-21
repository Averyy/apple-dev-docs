# init(type:length:_:)

**Framework**: Network  
**Kind**: init

Create TLV with the specified sizes for the type and length fields.

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
init<T, L, BelowProtocol>(type: T.Type, length: L.Type, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where T : Sendable, T : UnsignedInteger, L : Sendable, L : UnsignedInteger, BelowProtocol : StreamProtocol
```

## Parameters

- `type`: The object type to use for the   field.
- `length`: The object type to use for the   field.
- `builder`: The protocol stack below TLV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tlv/init(type:length:_:)-h8s)*