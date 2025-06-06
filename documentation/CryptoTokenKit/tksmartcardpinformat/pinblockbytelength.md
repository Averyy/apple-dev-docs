# pinBlockByteLength

**Framework**: CryptoTokenKit  
**Kind**: property

The total length of the PIN block in bytes. `8` by default.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var pinBlockByteLength: Int { get set }
```

## See Also

- [var charset: TKSmartCardPINFormat.Charset](tksmartcardpinformat/charset-swift.property.md)
  The format of PIN characters. `TKSmartCardPINCharsetNumeric` by default.
- [var encoding: TKSmartCardPINFormat.Encoding](tksmartcardpinformat/encoding-swift.property.md)
  The encoding of PIN characters. `TKSmartCardPINEncodingASCII` by default.
- [var minPINLength: Int](tksmartcardpinformat/minpinlength.md)
  The minimum number of characters to form a valid PIN. `4` by default.
- [var maxPINLength: Int](tksmartcardpinformat/maxpinlength.md)
  The maximum number of characters to form a valid PIN. `8` by default.
- [var pinJustification: TKSmartCardPINFormat.Justification](tksmartcardpinformat/pinjustification.md)
  The justification within the PIN block. `TKSmartCardPINJustificationLeft` by default.
- [var pinBitOffset: Int](tksmartcardpinformat/pinbitoffset.md)
  The offset, in bits, within the PIN block to mark a location for filling in the formatted PIN, which is justified with respect to the [`pinJustification`](tksmartcardpinformat/pinjustification.md) property value. `0` by default.
- [var pinLengthBitOffset: Int](tksmartcardpinformat/pinlengthbitoffset.md)
  The offset, in bits, within the PIN block to mark a location for filling in the PIN length, which is always left justified. `0` by default.
- [var pinLengthBitSize: Int](tksmartcardpinformat/pinlengthbitsize.md)
  The size, in bits, of the PIN length field. If set to `0`, PIN length is not written. `0` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/pinblockbytelength)*