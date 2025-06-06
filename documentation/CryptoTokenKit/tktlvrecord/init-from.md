# init(from:)

**Framework**: CryptoTokenKit  
**Kind**: init

Creates and returns a TLV record from by parsing the specified data.

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
convenience init?(from data: Data)
```

#### Return Value

A TLV record, or `nil` if `data` does not specify a valid record.

## Parameters

- `data`: A data object containing the serialized representation of a TLV record.

## See Also

- [class func sequenceOfRecords(from: Data) -> [TKTLVRecord]?](tktlvrecord/sequenceofrecords(from:).md)
  Creates and returns an array of TLV records from the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/init(from:))*