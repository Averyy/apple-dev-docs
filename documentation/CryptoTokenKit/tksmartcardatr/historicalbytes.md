# historicalBytes

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The ATR historical bytes, not including interface bytes or the TCK (check byte).

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
var historicalBytes: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * historicalBytes;
```

## See Also

### Accessing ATR Attributes
- [var protocols: [NSNumber]](./protocols.md)
  An array of protocols indicated in the ATR
- [var bytes: Data](./bytes.md)
  The ATR message data.
- [var historicalRecords: [TKCompactTLVRecord]?](./historicalrecords.md)
  A list of compact TLV records parsed from historical bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/historicalbytes)*