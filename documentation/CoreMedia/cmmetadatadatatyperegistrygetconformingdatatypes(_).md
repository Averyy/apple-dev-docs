# CMMetadataDataTypeRegistryGetConformingDataTypes(_:)

**Framework**: Core Media  
**Kind**: func

Returns the conforming data types for the data type, if any.

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
func CMMetadataDataTypeRegistryGetConformingDataTypes(_ dataType: CFString) -> CFArray
```

#### Return Value

List of conforming data types registered for the given data type, or `NULL` if the data type has not been registered.

## Parameters

- `dataType`: Identifier of the data type to be queried.

## See Also

- [func CMMetadataDataTypeRegistryDataTypeIsRegistered(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisregistered(_:).md)
  Returns a Boolean value that indicates the registration status of a data type identifier.
- [func CMMetadataDataTypeRegistryGetDataTypeDescription(CFString) -> CFString](cmmetadatadatatyperegistrygetdatatypedescription(_:).md)
  Returns the data type description if it exists.
- [func CMMetadataDataTypeRegistryDataTypeConformsToDataType(CFString, conformsTo: CFString) -> Bool](cmmetadatadatatyperegistrydatatypeconformstodatatype(_:conformsto:).md)
  Returns a Boolean value that indicates whether a data type conforms to another data type.
- [func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisbasedatatype(_:).md)
  Returns a Boolean value that indicates whether a data type identifier represents a base data type.
- [func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(CFString) -> CFString](cmmetadatadatatyperegistrygetbasedatatypeforconformingdatatype(_:).md)
  Returns the base data type identifier that a data type conforms to.
- [func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?](cmmetadatadatatyperegistrygetbasedatatypes().md)
  Returns an array of base data type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatadatatyperegistrygetconformingdatatypes(_:))*