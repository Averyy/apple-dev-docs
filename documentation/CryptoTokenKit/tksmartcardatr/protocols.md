# protocols

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

An array of protocols indicated in the ATR

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
var protocols: [NSNumber] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * protocols;
```

#### Discussion

Each element in the returned array is an `NSNumber` object containing an `NSUInteger` value corresponding to a member of the [`TKSmartCardProtocol`](../tksmartcardprotocol.md) enumeration.

The returned protocols are ordered such that the default protocol is at index `0`, and any duplicate values are removed.

## See Also

### Accessing ATR Attributes
- [var bytes: Data](./bytes.md)
  The ATR message data.
- [var historicalBytes: Data](./historicalbytes.md)
  The ATR historical bytes, not including interface bytes or the TCK (check byte).
- [var historicalRecords: [TKCompactTLVRecord]?](./historicalrecords.md)
  A list of compact TLV records parsed from historical bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/protocols)*