# historicalRecords

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSArray<TKCompactTLVRecord *> * historicalRecords;
```

## See Also

### Accessing ATR Attributes
- [var protocols: [NSNumber]](./protocols.md)
  An array of protocols indicated in the ATR
- [var bytes: Data](./bytes.md)
  The ATR message data.
- [var historicalBytes: Data](./historicalbytes.md)
  The ATR historical bytes, not including interface bytes or the TCK (check byte).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/historicalrecords)*