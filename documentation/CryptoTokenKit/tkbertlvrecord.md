# TKBERTLVRecord

**Framework**: CryptoTokenKit  
**Kind**: class

An object that parses BER-encoded data and produces DER-encoded data for TLV records.

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
class TKBERTLVRecord
```

## Topics

### Creating TLV Records
- [init(tag: TKTLVTag, value: Data)](tkbertlvrecord/init(tag:value:).md)
  Initializes a BER-TLV record with the specified tag and value.
- [init(tag: TKTLVTag, records: [TKTLVRecord])](tkbertlvrecord/init(tag:records:).md)
  Initializes a BER-TLV record with the specified tag and an array of TLV subrecords.
- [typealias TKTLVTag](tktlvtag.md)
  The type used to identify TLV format tags.
### Encoding Data
- [class func data(forTag: TKTLVTag) -> Data](tkbertlvrecord/data(fortag:).md)
  Encodes a specified tag using BER-TLV tag encoding rules.

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
- [class TKCompactTLVRecord](tkcompacttlvrecord.md)
  An object that implements encoding using Compact-TLV encoding according to ISO 7816-4.
- [class TKSimpleTLVRecord](tksimpletlvrecord.md)
  An object that implements encoding using Simple-TLV encoding according to ISO 7816-4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord)*