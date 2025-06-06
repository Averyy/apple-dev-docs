# TKCompactTLVRecord

**Framework**: CryptoTokenKit  
**Kind**: class

An object that implements encoding using Compact-TLV encoding according to ISO 7816-4.

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
class TKCompactTLVRecord
```

## Topics

### Creating TLV Records
- [init(tag: UInt8, value: Data)](tkcompacttlvrecord/init(tag:value:).md)
  Initializes a TLV record with the specified tag and value.

## Relationships

### Inherits From
- [TKTLVRecord](tktlvrecord.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TKTLVRecord](tktlvrecord.md)
  The base class encapsulating a Tag-Length-Value record.
- [class TKBERTLVRecord](tkbertlvrecord.md)
  An object that parses BER-encoded data and produces DER-encoded data for TLV records.
- [class TKSimpleTLVRecord](tksimpletlvrecord.md)
  An object that implements encoding using Simple-TLV encoding according to ISO 7816-4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkcompacttlvrecord)*