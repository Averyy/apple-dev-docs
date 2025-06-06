# CMMetadataDataTypeRegistryDataTypeIsBaseDataType(_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a data type identifier represents a base data type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(_ dataType: CFString) -> Bool
```

#### Return Value

[`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) if first data type conforms to the second data type; [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) otherwise.

#### Discussion

This is simply a convenience method to test to see if a given data type identifier is in the array returned by [`CMMetadataDataTypeRegistryGetBaseDataTypes()`](cmmetadatadatatyperegistrygetbasedatatypes().md).

## Parameters

- `dataType`: Identifier of the data type to be queried.

## See Also

- [func CMMetadataDataTypeRegistryDataTypeIsRegistered(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisregistered(_:).md)
  Returns a Boolean value that indicates the registration status of a data type identifier.
- [func CMMetadataDataTypeRegistryGetDataTypeDescription(CFString) -> CFString](cmmetadatadatatyperegistrygetdatatypedescription(_:).md)
  Returns the data type description if it exists.
- [func CMMetadataDataTypeRegistryGetConformingDataTypes(CFString) -> CFArray](cmmetadatadatatyperegistrygetconformingdatatypes(_:).md)
  Returns the conforming data types for the data type, if any.
- [func CMMetadataDataTypeRegistryDataTypeConformsToDataType(CFString, conformsTo: CFString) -> Bool](cmmetadatadatatyperegistrydatatypeconformstodatatype(_:conformsto:).md)
  Returns a Boolean value that indicates whether a data type conforms to another data type.
- [func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(CFString) -> CFString](cmmetadatadatatyperegistrygetbasedatatypeforconformingdatatype(_:).md)
  Returns the base data type identifier that a data type conforms to.
- [func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?](cmmetadatadatatyperegistrygetbasedatatypes().md)
  Returns an array of base data type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatadatatyperegistrydatatypeisbasedatatype(_:))*