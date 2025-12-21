# CMMetadata

**Framework**: Core Media

The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.

#### Overview

The Core Media framework provides two services: Metadata Identifier Services and the Metadata Data Type Registry.

Metadata Identifier Services provide a means of encoding the metadata identifying tuple (four-byte key namespace and N-byte key value) into [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString), and back again.

The Metadata Data Type Registry allows a process to register metadata data types that conform to a base data type and (optionally) other registered data types. The registry simplifies the process of creating format descriptions for nontrivial metadata values and allowing clients to indicate how to interpret metadata.

## Topics

### Creating Metadata Identifiers
- [func CMMetadataCreateIdentifierForKeyAndKeySpace(allocator: CFAllocator?, key: CFTypeRef, keySpace: CFString, identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus](cmmetadatacreateidentifierforkeyandkeyspace(allocator:key:keyspace:identifierout:).md)
  Creates a URL-like string identifier that represents a key or keyspace tuple.
- [func CMMetadataCreateKeyFromIdentifier(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFTypeRef?>) -> OSStatus](cmmetadatacreatekeyfromidentifier(allocator:identifier:keyout:).md)
  Creates a copy of the key by using an identifier.
- [func CMMetadataCreateKeyFromIdentifierAsCFData(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFData?>) -> OSStatus](cmmetadatacreatekeyfromidentifierascfdata(allocator:identifier:keyout:).md)
  Creates a copy of the key by using an identifier, and results in a core foundation data object.
- [func CMMetadataCreateKeySpaceFromIdentifier(allocator: CFAllocator?, identifier: CFString, keySpaceOut: UnsafeMutablePointer<CFString?>) -> OSStatus](cmmetadatacreatekeyspacefromidentifier(allocator:identifier:keyspaceout:).md)
  Creates a copy of the keyspace by using an identifier.
### Registering Metadata
- [func CMMetadataDataTypeRegistryRegisterDataType(CFString, description: CFString, conformingDataTypes: CFArray) -> OSStatus](cmmetadatadatatyperegistryregisterdatatype(_:description:conformingdatatypes:).md)
  Register a data type with the data type registry.
### Inspecting Metadata
- [func CMMetadataDataTypeRegistryDataTypeIsRegistered(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisregistered(_:).md)
  Returns a Boolean value that indicates the registration status of a data type identifier.
- [func CMMetadataDataTypeRegistryGetDataTypeDescription(CFString) -> CFString](cmmetadatadatatyperegistrygetdatatypedescription(_:).md)
  Returns the data type description if it exists.
- [func CMMetadataDataTypeRegistryGetConformingDataTypes(CFString) -> CFArray](cmmetadatadatatyperegistrygetconformingdatatypes(_:).md)
  Returns the conforming data types for the data type, if any.
- [func CMMetadataDataTypeRegistryDataTypeConformsToDataType(CFString, conformsTo: CFString) -> Bool](cmmetadatadatatyperegistrydatatypeconformstodatatype(_:conformsto:).md)
  Returns a Boolean value that indicates whether a data type conforms to another data type.
- [func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(CFString) -> Bool](cmmetadatadatatyperegistrydatatypeisbasedatatype(_:).md)
  Returns a Boolean value that indicates whether a data type identifier represents a base data type.
- [func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(CFString) -> CFString](cmmetadatadatatyperegistrygetbasedatatypeforconformingdatatype(_:).md)
  Returns the base data type identifier that a data type conforms to.
- [func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?](cmmetadatadatatyperegistrygetbasedatatypes().md)
  Returns an array of base data type identifiers.
### Constants
- [Metadata Identifier Error Codes](metadata-identifier-errors.md)
  Error codes that indicate metadata identifier errors.
- [Metadata Registry Error Codes](metadata-registry-errors.md)
  Error codes that indicate metadata registry errors.
- [Metadata Identifier Keyspaces](metadata-identifier-keyspaces.md)
  Constants that describe metadata identifier keyspaces.
- [Metadata Identifiers](metadata-identifiers.md)
  Constants that describe metadata identifiers.
- [Metadata Base Data Types](metadata-base-data-types.md)
  Constants that describe metadata base data types.
- [Metadata Data Types](metadata-data-types.md)
  Constants that describe metadata data types.

## See Also

- [CMTag](cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTag](cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
- [class CMTypedTag](cmtypedtag.md)
  A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- [CMTagCollection](cmtagcollection.md)
  Objective-C types and interfaces for working with Core Media tag collections.
- [enum CMProjectionType](cmprojectiontype.md)
  Constants describing the projection surface information in a 3D video buffer or channel.
- [struct CMStereoViewComponents](cmstereoviewcomponents.md)
  Constants describing the stereo views contained within a buffer or channel.
- [struct CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions.md)
  Create a set of stereo view interpretation options from a constant.
- [enum CMPackingType](cmpackingtype.md)
  The type of packing within each video frame, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadata)*