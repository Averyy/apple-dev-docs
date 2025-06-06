# CMVideoFormatDescriptionCreateFromH264ParameterSets(allocator:parameterSetCount:parameterSetPointers:parameterSetSizes:nalUnitHeaderLength:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates a format description for a video media stream that the parameter set describes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMVideoFormatDescriptionCreateFromH264ParameterSets(allocator: CFAllocator?, parameterSetCount: Int, parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, parameterSetSizes: UnsafePointer<Int>, nalUnitHeaderLength NALUnitHeaderLength: Int32, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus
```

#### Discussion

This function parses the dimensions provided by the parameter sets and creates a format description suitable for a raw H.264 stream. The parameter sets’ data can come from raw NAL units and must have any emulation prevention bytes needed.The supported NAL unit types to be included in the format description are 7 (sequence parameter set), 8 (picture parameter set) and 13 (sequence parameter set extension). At least one sequence parameter set and one picture parameter set must be provided.

## Parameters

- `allocator`: CFAllocator to be used when creating the CMFormatDescription. Pass NULL to use the default allocator.
- `parameterSetCount`: The number of parameter sets to include in the format description. This parameter must be at least 2.
- `parameterSetPointers`: Points to a C array containing parameterSetCount pointers to parameter sets.
- `parameterSetSizes`: Points to a C array containing the size, in bytes, of each of the parameter sets.
- `NALUnitHeaderLength`: Size, in bytes, of the NALUnitLength field in an AVC video sample or AVC parameter set sample. Pass 1, 2, or 4.
- `formatDescriptionOut`: Returned newly created video CMFormatDescription.

## See Also

- [struct CMImageDescriptionFlavor](cmimagedescriptionflavor.md)
  Types that represent image format descriptions.
- [func CMVideoFormatDescriptionCreate(allocator: CFAllocator?, codecType: CMVideoCodecType, width: Int32, height: Int32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](cmvideoformatdescriptioncreate(allocator:codectype:width:height:extensions:formatdescriptionout:).md)
  Creates a format description for a video media stream.
- [func CMVideoFormatDescriptionCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](cmvideoformatdescriptioncreateforimagebuffer(allocator:imagebuffer:formatdescriptionout:).md)
  Creates a format description for a video media stream by using an image buffer.
- [func CMVideoFormatDescriptionGetCleanAperture(CMVideoFormatDescription, originIsAtTopLeft: Bool) -> CGRect](cmvideoformatdescriptiongetcleanaperture(_:originisattopleft:).md)
  Returns a rectangle that defines the portion of the encoded pixel dimensions that represent the image data that’s valid for displaying.
- [func CMVideoFormatDescriptionGetDimensions(CMVideoFormatDescription) -> CMVideoDimensions](cmvideoformatdescriptiongetdimensions(_:).md)
  Returns the video dimensions, in encoded pixels.
- [func CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> CFArray](cmvideoformatdescriptiongetextensionkeyscommonwithimagebuffers().md)
  Returns an array of keys that you use for video format description extensions, image buffer attachments, and attributes.
- [func CMVideoFormatDescriptionGetPresentationDimensions(CMVideoFormatDescription, usePixelAspectRatio: Bool, useCleanAperture: Bool) -> CGSize](cmvideoformatdescriptiongetpresentationdimensions(_:usepixelaspectratio:usecleanaperture:).md)
  Returns the dimensions after taking the pixel aspect ratio and clean aperture into account.
- [func CMVideoFormatDescriptionMatchesImageBuffer(CMVideoFormatDescription, imageBuffer: CVImageBuffer) -> Bool](cmvideoformatdescriptionmatchesimagebuffer(_:imagebuffer:).md)
  Returns a Boolean value that indicates whether a format description matches an image buffer.
- [func CMVideoFormatDescriptionCreateFromHEVCParameterSets(allocator: CFAllocator?, parameterSetCount: Int, parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, parameterSetSizes: UnsafePointer<Int>, nalUnitHeaderLength: Int32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](cmvideoformatdescriptioncreatefromhevcparametersets(allocator:parametersetcount:parametersetpointers:parametersetsizes:nalunitheaderlength:extensions:formatdescriptionout:).md)
  Creates a format description for a video media stream using HEVC (H.265) parameter set NAL units.
- [func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(CMFormatDescription, parameterSetIndex: Int, parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, parameterSetSizeOut: UnsafeMutablePointer<Int>?, parameterSetCountOut: UnsafeMutablePointer<Int>?, nalUnitHeaderLengthOut: UnsafeMutablePointer<Int32>?) -> OSStatus](cmvideoformatdescriptiongeth264parametersetatindex(_:parametersetindex:parametersetpointerout:parametersetsizeout:parametersetcountout:nalunitheaderlengthout:).md)
  Returns a parameter set that an H.264 format description contains.
- [func CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(allocator: CFAllocator?, videoFormatDescription: CMVideoFormatDescription, stringEncoding: CFStringEncoding, flavor: CMImageDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmvideoformatdescriptioncopyasbigendianimagedescriptionblockbuffer(allocator:videoformatdescription:stringencoding:flavor:blockbufferout:).md)
  Copies the contents of a video format description to a buffer in big-endian byte ordering.
- [func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianImageDescriptionBlockBuffer: CMBlockBuffer, stringEncoding: CFStringEncoding, flavor: CMImageDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](cmvideoformatdescriptioncreatefrombigendianimagedescriptionblockbuffer(allocator:bigendianimagedescriptionblockbuffer:stringencoding:flavor:formatdescriptionout:).md)
  Creates a video format description from a big-endian image description inside a buffer.
- [func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(allocator: CFAllocator?, bigEndianImageDescriptionData: UnsafePointer<UInt8>, size: Int, stringEncoding: CFStringEncoding, flavor: CMImageDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](cmvideoformatdescriptioncreatefrombigendianimagedescriptiondata(allocator:bigendianimagedescriptiondata:size:stringencoding:flavor:formatdescriptionout:).md)
  Creates a video format description from a big-endian image description structure.
- [func CMSwapBigEndianImageDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendianimagedescriptiontohost(_:_:).md)
  Converts an image description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianImageDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendianimagedescriptiontobig(_:_:).md)
  Converts an image description data structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmvideoformatdescriptioncreatefromh264parametersets(allocator:parametersetcount:parametersetpointers:parametersetsizes:nalunitheaderlength:formatdescriptionout:))*