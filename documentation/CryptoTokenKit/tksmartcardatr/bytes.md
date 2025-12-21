# bytes

**Framework**: CryptoTokenKit  
**Kind**: property

The ATR message data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var bytes: Data { get }
```

## See Also

- [var protocols: [NSNumber]](tksmartcardatr/protocols.md)
  An array of protocols indicated in the ATR
- [var historicalBytes: Data](tksmartcardatr/historicalbytes.md)
  The ATR historical bytes, not including interface bytes or the TCK (check byte).
- [var historicalRecords: [TKCompactTLVRecord]?](tksmartcardatr/historicalrecords.md)
  A list of compact TLV records parsed from historical bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/bytes)*