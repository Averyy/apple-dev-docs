# CMMetadataDataTypeRegistryRegisterDataType(_:description:conformingDataTypes:)

**Framework**: Core Media  
**Kind**: func

Register a data type with the data type registry.

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
func CMMetadataDataTypeRegistryRegisterDataType(_ dataType: CFString, description: CFString, conformingDataTypes: CFArray) -> OSStatus
```

#### Return Value

If successful, a nonzero result code. See [`Metadata Registry Error Codes`](metadata-registry-errors.md).

#### Discussion

This routine is called by clients to register a data type with the data type registry. The list of conforming data type identifiers must include a base data type. If the data type has already been registered, then it is not considered an error to re-register it as long as the list of conforming data type identifiers has the same entries as the original; otherwise an error will be returned.

## Parameters

- `dataType`: Identifier of data type being registered.
- `description`: Human-readable description of data type being registered (for aiding debugging operations).
- `conformingDataTypes`: Data types that this data type conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatadatatyperegistryregisterdatatype(_:description:conformingdatatypes:))*