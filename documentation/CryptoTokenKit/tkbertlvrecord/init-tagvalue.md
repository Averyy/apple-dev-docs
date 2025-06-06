# init(tag:value:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a BER-TLV record with the specified tag and value.

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
init(tag: TKTLVTag, value: Data)
```

#### Return Value

A new TLV record containing the specified tag and value fields.

## Parameters

- `tag`: The tag field of the record.
- `value`: The value field of the record.

## See Also

- [init(tag: TKTLVTag, records: [TKTLVRecord])](tkbertlvrecord/init(tag:records:).md)
  Initializes a BER-TLV record with the specified tag and an array of TLV subrecords.
- [typealias TKTLVTag](tktlvtag.md)
  The type used to identify TLV format tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/init(tag:value:))*