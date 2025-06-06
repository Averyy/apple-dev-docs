# sequenceOfRecords(from:)

**Framework**: CryptoTokenKit  
**Kind**: method

Creates and returns an array of TLV records from the specified data.

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
class func sequenceOfRecords(from data: Data) -> [TKTLVRecord]?
```

#### Return Value

A sequence of TLV records, or `nil` if `data` does not specify a sequence of valid records.

## Parameters

- `data`: A data object containing the serialized representation of zero or more TLV records.

## See Also

- [convenience init?(from: Data)](tktlvrecord/init(from:).md)
  Creates and returns a TLV record from by parsing the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/sequenceofrecords(from:))*