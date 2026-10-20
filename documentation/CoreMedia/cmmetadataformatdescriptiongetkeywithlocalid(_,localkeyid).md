# CMMetadataFormatDescriptionGetKeyWithLocalID(_:localKeyID:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the key for the local identifier.

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
func CMMetadataFormatDescriptionGetKeyWithLocalID(_ desc: CMMetadataFormatDescription, localKeyID: OSType) -> CFDictionary?
```

```c
extern CFDictionaryRefCMMetadataFormatDescriptionGetKeyWithLocalID(CMMetadataFormatDescriptionRef desc, OSType localKeyID);
```

#### Return Value

A new dictionary containing the key specified by the localKeyID, or `NULL` if there is no key corresponding to the localKeyID.

#### Discussion

When writing a metadata track to a QuickTime movie, you can store many different kinds of metadata in one track. The format description for the track describes all of the kinds of metadata that might be present in that track.  And each kind of metadata has an id assigned to it which is unique from the others in the group.  So when individual samples of metadata are written (or read back later), they don’t contain their full description, instead they just contain the unique id (called the local id) that was assigned to them.  For instance, GPS might be local id 1, and face data might be local id 2. When someone pulls such a sample from a movie and wants to do a reverse lookup, they can call `CMMetadataFormatDescriptionGetKeyWithLocalID`, using the local id they’ve got, to get the Key associated with this metadata.

## Parameters

- `desc`: Format description being interrogated.
- `localKeyID`: Local Id identifying the key associated with the metadata description.

## See Also

### Working with Metadata Descriptions
- [struct CMMetadataDescriptionFlavor](./cmmetadatadescriptionflavor.md)
  Types that represent metadata format descriptions.
- [func CMMetadataFormatDescriptionCreateWithKeys(allocator: CFAllocator?, metadataType: CMMetadataFormatType, keys: CFArray?, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](./cmmetadataformatdescriptioncreatewithkeys%28allocator,metadatatype,keys,formatdescriptionout%29.md)
  Creates a metadata format description with the metadata keys you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadataformatdescriptiongetkeywithlocalid(_:localkeyid:))*