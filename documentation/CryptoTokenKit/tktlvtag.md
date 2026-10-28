# TKTLVTag

**Framework**: CryptoTokenKit  
**Kind**: typealias  
**Role**: Type Alias

The type used to identify TLV format tags.

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
typealias TKTLVTag = UInt64
```

```c
typedef UInt64 TKTLVTag;
```

## Discussion

Although some encodings tags do not have any size restrictions, the CryptoTokenKit framework supports tag lengths only up to 64-bits.

## See Also

### Creating TLV Records
- [init(tag: TKTLVTag, value: Data)](./tkbertlvrecord/init%28tag,value%29.md)
  Initializes a BER-TLV record with the specified tag and value.
- [init(tag: TKTLVTag, records: [TKTLVRecord])](./tkbertlvrecord/init%28tag,records%29.md)
  Initializes a BER-TLV record with the specified tag and an array of TLV subrecords.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktlvtag)*