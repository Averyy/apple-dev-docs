# TKSimpleTLVRecord

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

An object that implements encoding using Simple-TLV encoding according to ISO 7816-4.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class TKSimpleTLVRecord
```

```objc
@interface TKSimpleTLVRecord : TKTLVRecord
```

## Topics

### Creating TLV Records
- [init(tag: UInt8, value: Data)](./tksimpletlvrecord/init%28tag,value%29.md)
  Initializes a TLV record with the specified tag and value.

## Relationships

### Inherits From
- [TKTLVRecord](./tktlvrecord.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with Tag-Length-Value Records
- [class TKTLVRecord](./tktlvrecord.md)
  The base class encapsulating a Tag-Length-Value record.
- [class TKBERTLVRecord](./tkbertlvrecord.md)
  An object that parses BER-encoded data and produces DER-encoded data for TLV records.
- [class TKCompactTLVRecord](./tkcompacttlvrecord.md)
  An object that implements encoding using Compact-TLV encoding according to ISO 7816-4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksimpletlvrecord)*