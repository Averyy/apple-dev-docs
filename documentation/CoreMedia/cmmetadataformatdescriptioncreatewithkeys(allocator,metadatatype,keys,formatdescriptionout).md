# CMMetadataFormatDescriptionCreateWithKeys(allocator:metadataType:keys:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a metadata format description with the metadata keys you specify.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMMetadataFormatDescriptionCreateWithKeys(allocator: CFAllocator?, metadataType: CMMetadataFormatType, keys: CFArray?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus
```

```c
extern OSStatus CMMetadataFormatDescriptionCreateWithKeys(CFAllocatorRef allocator, CMMetadataFormatType metadataType, CFArrayRef keys, CMMetadataFormatDescriptionRef*formatDescriptionOut);
```

#### Return Value

A result code. Returns `noErr` if successful.

## Parameters

- `allocator`: `CFAllocator` to be used. Pass `NULL` or `kCFAllocatorDefault` to use the default allocator.
- `metadataType`: The type of metadata (kCMMetadataFormatType_Boxed).
- `keys`: Array of metadata keys. Each key is a dictionary of key properties. The required properties are:

  - `kCMMetadataFormatDescriptionKey_Namespace`
  - `kCMMetadataFormatDescriptionKey_Value`
  - `kCMMetadataFormatDescriptionKey_LocalID`
- `formatDescriptionOut`: Returns newly created metadata `CMFormatDescription`.

## See Also

### Working with Metadata Descriptions
- [struct CMMetadataDescriptionFlavor](./cmmetadatadescriptionflavor.md)
  Types that represent metadata format descriptions.
- [func CMMetadataFormatDescriptionGetKeyWithLocalID(CMMetadataFormatDescription, localKeyID: OSType) -> CFDictionary?](./cmmetadataformatdescriptiongetkeywithlocalid%28_,localkeyid%29.md)
  Returns the key for the local identifier.
- [func CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(allocator: CFAllocator?, metadataFormatDescription: CMMetadataFormatDescription, flavor: CMMetadataDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmmetadataformatdescriptioncopyasbigendianmetadatadescriptionblockbuffer%28allocator,metadataformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a metadata format description to a buffer in big-endian byte order.
- [func CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(allocator: CFAllocator?, sourceDescription: CMMetadataFormatDescription, otherSourceDescription: CMMetadataFormatDescription, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](./cmmetadataformatdescriptioncreatebymergingmetadataformatdescriptions%28allocator,sourcedescription,othersourcedescription,formatdescriptionout%29.md)
  Creates a metadata format description object by merging with another description.
- [func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianMetadataDescriptionBlockBuffer: CMBlockBuffer, flavor: CMMetadataDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](./cmmetadataformatdescriptioncreatefrombigendianmetadatadescriptionblockbuffer%28allocator,bigendianmetadatadescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates a metadata format description from a big-endian metadata description structure inside a buffer.
- [func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(allocator: CFAllocator?, bigEndianMetadataDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMMetadataDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](./cmmetadataformatdescriptioncreatefrombigendianmetadatadescriptiondata%28allocator,bigendianmetadatadescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates a metadata format description from a big-endian metadata description structure.
- [func CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(allocator: CFAllocator?, sourceDescription: CMMetadataFormatDescription, metadataSpecifications: CFArray, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](./cmmetadataformatdescriptioncreatewithmetadataformatdescriptionandmetadataspecifications%28allocator,sourcedescription,metadataspecifications,formatdescriptionout%29.md)
  Creates a metadata format description by extending an existing description with the values you specify.
- [func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(allocator: CFAllocator?, metadataType: CMMetadataFormatType, metadataSpecifications: CFArray, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](./cmmetadataformatdescriptioncreatewithmetadataspecifications%28allocator,metadatatype,metadataspecifications,formatdescriptionout%29.md)
  Creates a metadata format description with the specifications you specify.
- [func CMSwapBigEndianMetadataDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendianmetadatadescriptiontohost%28_,_%29.md)
  Converts a metadata description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianMetadataDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianmetadatadescriptiontobig%28_,_%29.md)
  Converts a metadata description data structure from host-endian to big-endian, in place.
- [func CMMetadataFormatDescriptionGetIdentifiers(CMMetadataFormatDescription) -> CFArray?](./cmmetadataformatdescriptiongetidentifiers%28_%29.md)
  Returns an array of metadata identifiers from a metadata format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadataformatdescriptioncreatewithkeys(allocator:metadatatype:keys:formatdescriptionout:))*