# CMMetadataFormatDescriptionCreateWithMetadataSpecifications(allocator:metadataType:metadataSpecifications:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates a metadata format description with the specifications you specify.

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
func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(allocator: CFAllocator?, metadataType: CMMetadataFormatType, metadataSpecifications: CFArray, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus
```

## Parameters

- `allocator`: CFAllocator to be used. kCFAllocatorDefault if you don’t care.
- `metadataType`: Currently the type must be kCMMetadataFormatType_Boxed.
- `metadataSpecifications`: An array of dictionaries, each dictionary supplies a metadata identifier, a datatype, and an optional language tag.
- `formatDescriptionOut`: Returned newly created metadata CMFormatDescription

## See Also

- [struct CMMetadataDescriptionFlavor](cmmetadatadescriptionflavor.md)
  Types that represent metadata format descriptions.
- [func CMMetadataFormatDescriptionCreateWithKeys(allocator: CFAllocator?, metadataType: CMMetadataFormatType, keys: CFArray?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](cmmetadataformatdescriptioncreatewithkeys(allocator:metadatatype:keys:formatdescriptionout:).md)
  Creates a metadata format description with the metadata keys you specify.
- [func CMMetadataFormatDescriptionGetKeyWithLocalID(CMMetadataFormatDescription, localKeyID: OSType) -> CFDictionary?](cmmetadataformatdescriptiongetkeywithlocalid(_:localkeyid:).md)
  Returns the key for the local identifier.
- [func CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(allocator: CFAllocator?, metadataFormatDescription: CMMetadataFormatDescription, flavor: CMMetadataDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmmetadataformatdescriptioncopyasbigendianmetadatadescriptionblockbuffer(allocator:metadataformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a metadata format description to a buffer in big-endian byte order.
- [func CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(allocator: CFAllocator?, sourceDescription: CMMetadataFormatDescription, otherSourceDescription: CMMetadataFormatDescription, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](cmmetadataformatdescriptioncreatebymergingmetadataformatdescriptions(allocator:sourcedescription:othersourcedescription:formatdescriptionout:).md)
  Creates a metadata format description object by merging with another description.
- [func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianMetadataDescriptionBlockBuffer: CMBlockBuffer, flavor: CMMetadataDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](cmmetadataformatdescriptioncreatefrombigendianmetadatadescriptionblockbuffer(allocator:bigendianmetadatadescriptionblockbuffer:flavor:formatdescriptionout:).md)
  Creates a metadata format description from a big-endian metadata description structure inside a buffer.
- [func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(allocator: CFAllocator?, bigEndianMetadataDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMMetadataDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](cmmetadataformatdescriptioncreatefrombigendianmetadatadescriptiondata(allocator:bigendianmetadatadescriptiondata:size:flavor:formatdescriptionout:).md)
  Creates a metadata format description from a big-endian metadata description structure.
- [func CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(allocator: CFAllocator?, sourceDescription: CMMetadataFormatDescription, metadataSpecifications: CFArray, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](cmmetadataformatdescriptioncreatewithmetadataformatdescriptionandmetadataspecifications(allocator:sourcedescription:metadataspecifications:formatdescriptionout:).md)
  Creates a metadata format description by extending an existing description with the values you specify.
- [func CMSwapBigEndianMetadataDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendianmetadatadescriptiontohost(_:_:).md)
  Converts a metadata description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianMetadataDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendianmetadatadescriptiontobig(_:_:).md)
  Converts a metadata description data structure from host-endian to big-endian, in place.
- [func CMMetadataFormatDescriptionGetIdentifiers(CMMetadataFormatDescription) -> CFArray?](cmmetadataformatdescriptiongetidentifiers(_:).md)
  Returns an array of metadata identifiers from a metadata format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadataformatdescriptioncreatewithmetadataspecifications(allocator:metadatatype:metadataspecifications:formatdescriptionout:))*