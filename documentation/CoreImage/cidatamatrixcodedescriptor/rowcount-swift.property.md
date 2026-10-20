# rowCount

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The number of rows in the Data Matrix code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var rowCount: Int { get }
```

```objc
@property (readonly) NSInteger rowCount;
```

#### Discussion

Refer to ISO/IEC 16022:2006(E) for valid module row and column count combinations.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [var columnCount: Int](./columncount-swift.property.md)
  The number of columns in the Data Matrix code symbol.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](./eccversion-swift.property.md)
  The error correction version of the Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/rowcount-swift.property)*