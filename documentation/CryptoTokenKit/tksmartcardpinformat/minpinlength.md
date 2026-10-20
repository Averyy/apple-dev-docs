# minPINLength

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The minimum number of characters to form a valid PIN. `4` by default.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var minPINLength: Int { get set }
```

```objc
@property NSInteger minPINLength;
```

## See Also

### Configuring PIN Formatting
- [var charset: TKSmartCardPINFormat.Charset](./charset-swift.property.md)
  The format of PIN characters. `TKSmartCardPINCharsetNumeric` by default.
- [var encoding: TKSmartCardPINFormat.Encoding](./encoding-swift.property.md)
  The encoding of PIN characters. `TKSmartCardPINEncodingASCII` by default.
- [var maxPINLength: Int](./maxpinlength.md)
  The maximum number of characters to form a valid PIN. `8` by default.
- [var pinBlockByteLength: Int](./pinblockbytelength.md)
  The total length of the PIN block in bytes. `8` by default.
- [var pinJustification: TKSmartCardPINFormat.Justification](./pinjustification.md)
  The justification within the PIN block. `TKSmartCardPINJustificationLeft` by default.
- [var pinBitOffset: Int](./pinbitoffset.md)
  The offset, in bits, within the PIN block to mark a location for filling in the formatted PIN, which is justified with respect to the [`pinJustification`](./pinjustification.md) property value. `0` by default.
- [var pinLengthBitOffset: Int](./pinlengthbitoffset.md)
  The offset, in bits, within the PIN block to mark a location for filling in the PIN length, which is always left justified. `0` by default.
- [var pinLengthBitSize: Int](./pinlengthbitsize.md)
  The size, in bits, of the PIN length field. If set to `0`, PIN length is not written. `0` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/minpinlength)*