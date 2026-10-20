# CMMetadataDataTypeRegistryGetBaseDataTypes()

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns an array of base data type identifiers.

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
func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?
```

```c
extern CFArrayRefCMMetadataDataTypeRegistryGetBaseDataTypes();
```

#### Return Value

An array of the base data types to which all others must conform.

#### Discussion

There are a set of base data types that seed the data type registry. All valid data types will have their conformance search end with a base data type.

## See Also

### Inspecting Metadata
- [func CMMetadataDataTypeRegistryDataTypeIsRegistered(CFString) -> Bool](./cmmetadatadatatyperegistrydatatypeisregistered%28_%29.md)
  Returns a Boolean value that indicates the registration status of a data type identifier.
- [func CMMetadataDataTypeRegistryGetDataTypeDescription(CFString) -> CFString](./cmmetadatadatatyperegistrygetdatatypedescription%28_%29.md)
  Returns the data type description if it exists.
- [func CMMetadataDataTypeRegistryGetConformingDataTypes(CFString) -> CFArray](./cmmetadatadatatyperegistrygetconformingdatatypes%28_%29.md)
  Returns the conforming data types for the data type, if any.
- [func CMMetadataDataTypeRegistryDataTypeConformsToDataType(CFString, conformsTo: CFString) -> Bool](./cmmetadatadatatyperegistrydatatypeconformstodatatype%28_,conformsto%29.md)
  Returns a Boolean value that indicates whether a data type conforms to another data type.
- [func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(CFString) -> Bool](./cmmetadatadatatyperegistrydatatypeisbasedatatype%28_%29.md)
  Returns a Boolean value that indicates whether a data type identifier represents a base data type.
- [func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(CFString) -> CFString](./cmmetadatadatatyperegistrygetbasedatatypeforconformingdatatype%28_%29.md)
  Returns the base data type identifier that a data type conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatadatatyperegistrygetbasedatatypes())*