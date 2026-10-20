# init(tag:records:)

**Framework**: CryptoTokenKit  
**Kind**: init  
**Role**: Initializer

Initializes a BER-TLV record with the specified tag and an array of TLV subrecords.

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
init(tag: TKTLVTag, records: [TKTLVRecord])
```

```objc
- (instancetype) initWithTag:(TKTLVTag) tag records:(NSArray<TKTLVRecord *> *) records;
```

#### Return Value

A new TLV record containing the specified tag field and subrecords.

## Parameters

- `tag`: The tag field of the record.
- `records`: The TLV subrecords of the record.

## See Also

### Creating TLV Records
- [init(tag: TKTLVTag, value: Data)](./init%28tag,value%29.md)
  Initializes a BER-TLV record with the specified tag and value.
- [typealias TKTLVTag](../tktlvtag.md)
  The type used to identify TLV format tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/init(tag:records:))*