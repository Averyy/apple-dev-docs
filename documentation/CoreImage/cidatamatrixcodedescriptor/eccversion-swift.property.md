# eccVersion

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The error correction version of the Data Matrix code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion { get }
```

```objc
@property (readonly) CIDataMatrixCodeECCVersion eccVersion;
```

## Discussion

The possible error correction version are enumerated in [`CIDataMatrixCodeDescriptor.ECCVersion`](./eccversion-swift.enum.md). Any symbol with an even number of rows and columns will be ECC 200.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [var rowCount: Int](./rowcount-swift.property.md)
  The number of rows in the Data Matrix code symbol.
- [var columnCount: Int](./columncount-swift.property.md)
  The number of columns in the Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.property)*