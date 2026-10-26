# descriptorWithPayload:rowCount:columnCount:eccVersion:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a Data Matrix code descriptor for the given payload and parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) descriptorWithPayload:(NSData *) errorCorrectedPayload rowCount:(NSInteger) rowCount columnCount:(NSInteger) columnCount eccVersion:(CIDataMatrixCodeECCVersion) eccVersion;
```

#### Return Value

 An autoreleased [`CIAztecCodeDescriptor`](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## Parameters

- `errorCorrectedPayload`: The data to encode in the Data Matrix code symbol.
- `rowCount`: The number of rows in the Data Matrix code symbol.
- `columnCount`: The number of columns in the Data Matrix code symbol.
- `eccVersion`: The [`CIDataMatrixCodeDescriptor.ECCVersion`](./eccversion-swift.enum.md) for the Data Matrix code symbol.

## See Also

### Creating a Descriptor
- [init?(payload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)](./init%28payload,rowcount,columncount,eccversion%29.md)
  Initializes a Data Matrix code descriptor for the given payload and parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/descriptorwithpayload:rowcount:columncount:eccversion:)*