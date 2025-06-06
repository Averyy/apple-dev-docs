# TKTLVRecord

**Framework**: CryptoTokenKit  
**Kind**: class

The base class encapsulating a Tag-Length-Value record.

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
class TKTLVRecord
```

#### Overview

The CryptoTokenKit framework provides the following concrete subclasses for various TLV record encodings:

- [`TKBERTLVRecord`](tkbertlvrecord.md) for BER-TLV encoding rules
- [`TKSimpleTLVRecord`](tksimpletlvrecord.md) for Simple-TLV encoding according to ISO 7816-4
- [`TKCompactTLVRecord`](tkcompacttlvrecord.md) for Compact-TLV encoding according to ISO 7816-4

## Topics

### Creating Records
- [class func sequenceOfRecords(from: Data) -> [TKTLVRecord]?](tktlvrecord/sequenceofrecords(from:).md)
  Creates and returns an array of TLV records from the specified data.
- [convenience init?(from: Data)](tktlvrecord/init(from:).md)
  Creates and returns a TLV record from by parsing the specified data.
### Accessing the Tag Field
- [var tag: TKTLVTag](tktlvrecord/tag.md)
  The tag field of the record.
- [typealias TKTLVTag](tktlvtag.md)
  The type used to identify TLV format tags.
### Accessing the Value Field
- [var value: Data](tktlvrecord/value.md)
  The value field of the record.
### Accessing Record Data
- [var data: Data](tktlvrecord/data.md)
  The record data, including the tag, length, and value fields.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TKBERTLVRecord](tkbertlvrecord.md)
- [TKCompactTLVRecord](tkcompacttlvrecord.md)
- [TKSimpleTLVRecord](tksimpletlvrecord.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TKBERTLVRecord](tkbertlvrecord.md)
  An object that parses BER-encoded data and produces DER-encoded data for TLV records.
- [class TKCompactTLVRecord](tkcompacttlvrecord.md)
  An object that implements encoding using Compact-TLV encoding according to ISO 7816-4.
- [class TKSimpleTLVRecord](tksimpletlvrecord.md)
  An object that implements encoding using Simple-TLV encoding according to ISO 7816-4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord)*