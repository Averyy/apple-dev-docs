# historicalRecords

**Framework**: CryptoTokenKit  
**Kind**: property

A list of compact TLV records parsed from historical bytes.

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
var historicalRecords: [TKCompactTLVRecord]? { get }
```

## See Also

- [var protocols: [NSNumber]](tksmartcardatr/protocols.md)
  An array of protocols indicated in the ATR
- [var bytes: Data](tksmartcardatr/bytes.md)
  The ATR message data.
- [var historicalBytes: Data](tksmartcardatr/historicalbytes.md)
  The ATR historical bytes, not including interface bytes or the TCK (check byte).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/historicalrecords)*