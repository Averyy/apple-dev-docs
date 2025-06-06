# CMMetadataDataTypeRegistryDataTypeConformsToDataType(_:conformsTo:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a data type conforms to another data type.

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
func CMMetadataDataTypeRegistryDataTypeConformsToDataType(_ dataType: CFString, conformsTo conformsToDataType: CFString) -> Bool
```

#### Return Value

[`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) if first data type conforms to the second data type; [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) otherwise.

#### Discussion

A given data type will conform to a second data type if any of the following are true:

1. The data type identifiers are the same.
2. The first data type identifier’s conformance list contains the second data type identifier.
3. A recursive search of the conforming data types for each element in the first data type’s conformance list yields the second data type identifier.

## Parameters

- `dataType`: Identifier of the data type to be tested.
- `conformsToDataType`: Identifier of the data type against which to test for conformance.

## See Also

- [func CMMetadataDataTypeRegistryDataTypeIsRegistered(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisregistered(_:).md)
  Returns a Boolean value that indicates the registration status of a data type identifier.
- [func CMMetadataDataTypeRegistryGetDataTypeDescription(CFString) -> CFString](cmmetadatadatatyperegistrygetdatatypedescription(_:).md)
  Returns the data type description if it exists.
- [func CMMetadataDataTypeRegistryGetConformingDataTypes(CFString) -> CFArray](cmmetadatadatatyperegistrygetconformingdatatypes(_:).md)
  Returns the conforming data types for the data type, if any.
- [func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisbasedatatype(_:).md)
  Returns a Boolean value that indicates whether a data type identifier represents a base data type.
- [func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(CFString) -> CFString](cmmetadatadatatyperegistrygetbasedatatypeforconformingdatatype(_:).md)
  Returns the base data type identifier that a data type conforms to.
- [func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?](cmmetadatadatatyperegistrygetbasedatatypes().md)
  Returns an array of base data type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatadatatyperegistrydatatypeconformstodatatype(_:conformsto:))*