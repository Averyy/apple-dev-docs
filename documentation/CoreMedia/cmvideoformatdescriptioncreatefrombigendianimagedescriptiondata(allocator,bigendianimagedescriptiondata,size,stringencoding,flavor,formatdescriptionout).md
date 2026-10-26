# CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(allocator:bigEndianImageDescriptionData:size:stringEncoding:flavor:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a video format description from a big-endian image description structure.

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
func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(allocator: CFAllocator?, bigEndianImageDescriptionData imageDescriptionData: UnsafePointer<UInt8>, size: Int, stringEncoding: CFStringEncoding, flavor: CMImageDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus
```

```c
extern OSStatus CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(CFAllocatorRef allocator, const uint8_t *imageDescriptionData, size_t size, CFStringEncoding stringEncoding, CMImageDescriptionFlavor flavor, CMVideoFormatDescriptionRef*formatDescriptionOut);
```

## Parameters

- `allocator`: Allocator to use for allocating the `CMVideoFormatDescription` object. May be `NULL`.
- `imageDescriptionData`: ImageDescription data structure in big-endian byte ordering.
- `size`: Size of ImageDescription data structure.
- `stringEncoding`: Pass [`CFStringGetSystemEncoding()`](../CoreFoundation/cfstringgetsystemencoding%28%29.md) or `GetApplicationTextEncoding()`.
- `flavor`: `kCMImageDescriptionFlavor` constant or `NULL` for QuickTimeMovie flavor.
- `formatDescriptionOut`: Receives new `CMVideoFormatDescription`.

## See Also

### Working with Video Descriptions
- [struct CMImageDescriptionFlavor](./cmimagedescriptionflavor.md)
  Types that represent image format descriptions.
- [func CMVideoFormatDescriptionCreate(allocator: CFAllocator?, codecType: CMVideoCodecType, width: Int32, height: Int32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](./cmvideoformatdescriptioncreate%28allocator,codectype,width,height,extensions,formatdescriptionout%29.md)
  Creates a format description for a video media stream.
- [func CMVideoFormatDescriptionCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](./cmvideoformatdescriptioncreateforimagebuffer%28allocator,imagebuffer,formatdescriptionout%29.md)
  Creates a format description for a video media stream by using an image buffer.
- [func CMVideoFormatDescriptionGetCleanAperture(CMVideoFormatDescription, originIsAtTopLeft: Bool) -> CGRect](./cmvideoformatdescriptiongetcleanaperture%28_,originisattopleft%29.md)
  Returns a rectangle that defines the portion of the encoded pixel dimensions that represent the image data that’s valid for displaying.
- [func CMVideoFormatDescriptionGetDimensions(CMVideoFormatDescription) -> CMVideoDimensions](./cmvideoformatdescriptiongetdimensions%28_%29.md)
  Returns the video dimensions, in encoded pixels.
- [func CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> CFArray](./cmvideoformatdescriptiongetextensionkeyscommonwithimagebuffers%28%29.md)
  Returns an array of keys that you use for video format description extensions, image buffer attachments, and attributes.
- [func CMVideoFormatDescriptionGetPresentationDimensions(CMVideoFormatDescription, usePixelAspectRatio: Bool, useCleanAperture: Bool) -> CGSize](./cmvideoformatdescriptiongetpresentationdimensions%28_,usepixelaspectratio,usecleanaperture%29.md)
  Returns the dimensions after taking the pixel aspect ratio and clean aperture into account.
- [func CMVideoFormatDescriptionMatchesImageBuffer(CMVideoFormatDescription, imageBuffer: CVImageBuffer) -> Bool](./cmvideoformatdescriptionmatchesimagebuffer%28_,imagebuffer%29.md)
  Returns a Boolean value that indicates whether a format description matches an image buffer.
- [func CMVideoFormatDescriptionCreateFromH264ParameterSets(allocator: CFAllocator?, parameterSetCount: Int, parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, parameterSetSizes: UnsafePointer<Int>, nalUnitHeaderLength: Int32, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](./cmvideoformatdescriptioncreatefromh264parametersets%28allocator,parametersetcount,parametersetpointers,parametersetsizes,nalunitheaderlength,formatdescriptionout%29.md)
  Creates a format description for a video media stream that the parameter set describes.
- [func CMVideoFormatDescriptionCreateFromHEVCParameterSets(allocator: CFAllocator?, parameterSetCount: Int, parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, parameterSetSizes: UnsafePointer<Int>, nalUnitHeaderLength: Int32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](./cmvideoformatdescriptioncreatefromhevcparametersets%28allocator,parametersetcount,parametersetpointers,parametersetsizes,nalunitheaderlength,extensions,formatdescriptionout%29.md)
  Creates a format description for a video media stream using HEVC (H.265) parameter set NAL units.
- [func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(CMFormatDescription, parameterSetIndex: Int, parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, parameterSetSizeOut: UnsafeMutablePointer<Int>?, parameterSetCountOut: UnsafeMutablePointer<Int>?, nalUnitHeaderLengthOut: UnsafeMutablePointer<Int32>?) -> OSStatus](./cmvideoformatdescriptiongeth264parametersetatindex%28_,parametersetindex,parametersetpointerout,parametersetsizeout,parametersetcountout,nalunitheaderlengthout%29.md)
  Returns a parameter set that an H.264 format description contains.
- [func CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(allocator: CFAllocator?, videoFormatDescription: CMVideoFormatDescription, stringEncoding: CFStringEncoding, flavor: CMImageDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmvideoformatdescriptioncopyasbigendianimagedescriptionblockbuffer%28allocator,videoformatdescription,stringencoding,flavor,blockbufferout%29.md)
  Copies the contents of a video format description to a buffer in big-endian byte ordering.
- [func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianImageDescriptionBlockBuffer: CMBlockBuffer, stringEncoding: CFStringEncoding, flavor: CMImageDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](./cmvideoformatdescriptioncreatefrombigendianimagedescriptionblockbuffer%28allocator,bigendianimagedescriptionblockbuffer,stringencoding,flavor,formatdescriptionout%29.md)
  Creates a video format description from a big-endian image description inside a buffer.
- [func CMSwapBigEndianImageDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendianimagedescriptiontohost%28_,_%29.md)
  Converts an image description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianImageDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianimagedescriptiontobig%28_,_%29.md)
  Converts an image description data structure from host-endian to big-endian, in place.
- [CMVideoFormatDescriptionCopyTagCollectionArray](./cmvideoformatdescriptioncopytagcollectionarray.md)
  Copies the multi-image encoding properties as an array of CMTagCollections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmvideoformatdescriptioncreatefrombigendianimagedescriptiondata(allocator:bigendianimagedescriptiondata:size:stringencoding:flavor:formatdescriptionout:))*