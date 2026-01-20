# errorCorrectedPayload

**Framework**: Core Image  
**Kind**: property

The error-corrected payload containing the data encoded in the PDF417 code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var errorCorrectedPayload: Data { get }
```

#### Discussion

The first codeword indicates the number of data codewords in the errorCorrectedPayload.

PDF417 codes are comprised of a start character on the left and a stop character on the right. Each row begins and ends with special characters indicating the current row as well as information about the dimensions of the PDF417 symbol. The errorCorrectedPayload represents the sequence of PDF417 codewords that make up the body of the message. The first codeword indicates the number of codewords in the message. This count includes the “count” codeword and any padding codewords, but does not include the error correction codewords. Each codeword is a 16-bit value in the range of 0…928. The sequence is to be interpreted as described in the PDF417 bar code symbology specification – ISO/IEC 15438:2006(E).

## See Also

- [var isCompact: Bool](cipdf417codedescriptor/iscompact-swift.property.md)
  A boolean value telling if the PDF417 code is compact.
- [var rowCount: Int](cipdf417codedescriptor/rowcount-swift.property.md)
  The number of rows in the PDF417 code symbol.
- [var columnCount: Int](cipdf417codedescriptor/columncount-swift.property.md)
  The number of columns in the PDF417 code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/errorcorrectedpayload-swift.property)*