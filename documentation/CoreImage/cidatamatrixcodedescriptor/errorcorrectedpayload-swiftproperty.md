# errorCorrectedPayload

**Framework**: Core Image  
**Kind**: property

The error-corrected payload containing the data encoded in the Data Matrix code symbol.

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

DataMatrix symbols are specified bn ISO/IEC 16022:2006(E). ECC 200-type symbols will always have an even number of rows and columns.

For ECC 200-type symbols, the phases of encoding data into a symbol are described in section 5.1 – Encode procedure overview. The error corrected payload comprises the de-interleaved bits of the message described at the end of Step 1: Data encodation.

## See Also

- [var rowCount: Int](cidatamatrixcodedescriptor/rowcount-swift.property.md)
  The number of rows in the Data Matrix code symbol.
- [var columnCount: Int](cidatamatrixcodedescriptor/columncount-swift.property.md)
  The number of columns in the Data Matrix code symbol.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](cidatamatrixcodedescriptor/eccversion-swift.property.md)
  The error correction version of the Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property)*