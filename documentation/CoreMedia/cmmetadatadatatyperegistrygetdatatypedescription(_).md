# CMMetadataDataTypeRegistryGetDataTypeDescription(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the data type description if it exists.

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
func CMMetadataDataTypeRegistryGetDataTypeDescription(_ dataType: CFString) -> CFString
```

```c
extern CFStringRefCMMetadataDataTypeRegistryGetDataTypeDescription(CFStringRef dataType);
```

## Return Value

The description of the requested data type.

## Parameters

- `dataType`: Identifier of the data type to be queried.

## See Also

### Inspecting Metadata
- [func CMMetadataDataTypeRegistryDataTypeIsRegistered(CFString) -> Bool](./cmmetadatadatatyperegistrydatatypeisregistered%28_%29.md)
  Returns a Boolean value that indicates the registration status of a data type identifier.
- [func CMMetadataDataTypeRegistryGetConformingDataTypes(CFString) -> CFArray](./cmmetadatadatatyperegistrygetconformingdatatypes%28_%29.md)
  Returns the conforming data types for the data type, if any.
- [func CMMetadataDataTypeRegistryDataTypeConformsToDataType(CFString, conformsTo: CFString) -> Bool](./cmmetadatadatatyperegistrydatatypeconformstodatatype%28_,conformsto%29.md)
  Returns a Boolean value that indicates whether a data type conforms to another data type.
- [func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(CFString) -> Bool](./cmmetadatadatatyperegistrydatatypeisbasedatatype%28_%29.md)
  Returns a Boolean value that indicates whether a data type identifier represents a base data type.
- [func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(CFString) -> CFString](./cmmetadatadatatyperegistrygetbasedatatypeforconformingdatatype%28_%29.md)
  Returns the base data type identifier that a data type conforms to.
- [func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?](./cmmetadatadatatyperegistrygetbasedatatypes%28%29.md)
  Returns an array of base data type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatadatatyperegistrygetdatatypedescription(_:))*