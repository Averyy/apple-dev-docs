# CMVideoFormatDescriptionMatchesImageBuffer(_:imageBuffer:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a format description matches an image buffer.

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
func CMVideoFormatDescriptionMatchesImageBuffer(_ desc: CMVideoFormatDescription, imageBuffer: CVImageBuffer) -> Bool
```

#### Return Value

A Boolean indicating whether the format description matches the image buffer.

#### Discussion

This function uses the keys returned by `CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers` to compare the extensions of the given format description to the attachments of the given image buffer (if an attachment is absent in either it must be absent in both). It also checks `kCMFormatDescriptionExtension_BytesPerRow` against `CVPixelBufferGetBytesPerRow`, if applicable.

## Parameters

- `desc`: CMVideoFormatDescription to validate.
- `imageBuffer`: Image buffer to validate against.

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
- [func CMVideoFormatDescriptionCreateFromH264ParameterSets(allocator: CFAllocator?, parameterSetCount: Int, parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, parameterSetSizes: UnsafePointer<Int>, nalUnitHeaderLength: Int32, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](cmvideoformatdescriptioncreatefromh264parametersets(allocator:parametersetcount:parametersetpointers:parametersetsizes:nalunitheaderlength:formatdescriptionout:).md)
  Creates a format description for a video media stream that the parameter set describes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmvideoformatdescriptionmatchesimagebuffer(_:imagebuffer:))*