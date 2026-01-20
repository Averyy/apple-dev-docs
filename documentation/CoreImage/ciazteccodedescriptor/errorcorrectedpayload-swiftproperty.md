# errorCorrectedPayload

**Framework**: Core Image  
**Kind**: property

The error-corrected payload that comprises the the Aztec code symbol.

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

Aztec Codes are formally specified in ISO/IEC 24778:2008(E).

The error corrected payload consists of the 6-, 8-, 10-, or 12-bit message codewords produced at the end of the step described in section 7.3.1.2 “Formation of data codewords”, which exists immediately prior to adding error correction. These codewords have dummy bits inserted to ensure that an entire codeword isn’t all 0’s or all 1’s. Clients will need to remove these extra bits as part of interpreting the payload.

## See Also

- [var isCompact: Bool](ciazteccodedescriptor/iscompact-swift.property.md)
  A Boolean value telling if the Aztec code is compact.
- [var layerCount: Int](ciazteccodedescriptor/layercount-swift.property.md)
  The number of data layers in the Aztec code symbol.
- [var dataCodewordCount: Int](ciazteccodedescriptor/datacodewordcount-swift.property.md)
  The number of non-error-correction codewords carried by the Aztec code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/errorcorrectedpayload-swift.property)*