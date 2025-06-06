# CMFormatDescription APIs

**Framework**: Core Media

A media format descriptor that describes the samples in a sample buffer.

#### Overview

`CMFormatDescriptions` are immutable Core Foundation objects that describe media data of various types, including audio, video, and muxed media data. There are two types of API: media-type-agnostic APIs (supported by all CMFormatDescriptions) and media-type-specific APIs. The media-type-agnostic APIs are prefixed with `CMFormatDescription`, and the media-type-specific APIs are prefixed with `CMAudioFormatDescription`, `CMVideoFormatDescription`, and so on.

## Topics

### Creating Format Descriptions
- [func CMFormatDescriptionCreate(allocator: CFAllocator?, mediaType: CMMediaType, mediaSubType: FourCharCode, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](cmformatdescriptioncreate(allocator:mediatype:mediasubtype:extensions:formatdescriptionout:).md)
  Creates a format description for general use.
### Comparing Format Descriptions
- [func CMFormatDescriptionEqual(CMFormatDescription?, otherFormatDescription: CMFormatDescription?) -> Bool](cmformatdescriptionequal(_:otherformatdescription:).md)
  Returns a Boolean value that indicates whether two format descriptions are equal.
- [func CMFormatDescriptionEqualIgnoringExtensionKeys(CMFormatDescription?, otherFormatDescription: CMFormatDescription?, extensionKeysToIgnore: CFTypeRef?, sampleDescriptionExtensionAtomKeysToIgnore: CFTypeRef?) -> Bool](cmformatdescriptionequalignoringextensionkeys(_:otherformatdescription:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:).md)
  Returns a Boolean value that indicates whether two format descriptions are equal, ignoring differences in the extension keys you specify.
### Inspecting Format Descriptions
- [func CMFormatDescriptionGetMediaType(CMFormatDescription) -> CMMediaType](cmformatdescriptiongetmediatype(_:).md)
  Returns the media type of a format description.
- [func CMFormatDescriptionGetMediaSubType(CMFormatDescription) -> FourCharCode](cmformatdescriptiongetmediasubtype(_:).md)
  Returns the media subtype of a format description.
- [func CMFormatDescriptionGetExtension(CMFormatDescription, extensionKey: CFString) -> CFPropertyList?](cmformatdescriptiongetextension(_:extensionkey:).md)
  Returns an extension from the format description by using an extension key.
- [func CMFormatDescriptionGetExtensions(CMFormatDescription) -> CFDictionary?](cmformatdescriptiongetextensions(_:).md)
  Returns all of the extensions for a format description.
- [func CMFormatDescriptionGetTypeID() -> CFTypeID](cmformatdescriptiongettypeid().md)
  Returns the Core Foundation type identifier that identifies format description objects.
### Working with Audio Descriptions
- [struct CMSoundDescriptionFlavor](cmsounddescriptionflavor.md)
  Types that represent sound format descriptions.
- [func CMAudioFormatDescriptionCreateSummary(allocator: CFAllocator?, formatDescriptionArray: CFArray, flags: UInt32, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](cmaudioformatdescriptioncreatesummary(allocator:formatdescriptionarray:flags:formatdescriptionout:).md)
  Creates a summary audio format description from an array of descriptions.
- [func CMAudioFormatDescriptionCreate(allocator: CFAllocator?, asbd: UnsafePointer<AudioStreamBasicDescription>, layoutSize: Int, layout: UnsafePointer<AudioChannelLayout>?, magicCookieSize: Int, magicCookie: UnsafeRawPointer?, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](cmaudioformatdescriptioncreate(allocator:asbd:layoutsize:layout:magiccookiesize:magiccookie:extensions:formatdescriptionout:).md)
  Creates a format description for an audio media stream.
- [func CMAudioFormatDescriptionEqual(CMAudioFormatDescription, otherFormatDescription: CMAudioFormatDescription, equalityMask: CMAudioFormatDescriptionMask, equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>?) -> Bool](cmaudioformatdescriptionequal(_:otherformatdescription:equalitymask:equalitymaskout:).md)
  Returns a Boolean value that indicates whether the two audio format descriptions are equal.
- [func CMAudioFormatDescriptionGetChannelLayout(CMAudioFormatDescription, sizeOut: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioChannelLayout>?](cmaudioformatdescriptiongetchannellayout(_:sizeout:).md)
  Returns a read-only pointer to, and the size of, the audio channel layout inside an audio format description.
- [func CMAudioFormatDescriptionGetFormatList(CMAudioFormatDescription, sizeOut: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioFormatListItem>?](cmaudioformatdescriptiongetformatlist(_:sizeout:).md)
  Returns a read-only pointer to, and size of, the array of audio format list item structures in an audio format description.
- [func CMAudioFormatDescriptionGetMagicCookie(CMAudioFormatDescription, sizeOut: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](cmaudioformatdescriptiongetmagiccookie(_:sizeout:).md)
  Returns a read-only pointer to, and size of, the magic cookie in an audio format description.
- [func CMAudioFormatDescriptionGetMostCompatibleFormat(CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>?](cmaudioformatdescriptiongetmostcompatibleformat(_:).md)
  Returns a read-only pointer to the appropriate audio format list item in an audio format description.
- [func CMAudioFormatDescriptionGetRichestDecodableFormat(CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>?](cmaudioformatdescriptiongetrichestdecodableformat(_:).md)
  Returns a read-only pointer to the appropriate audio format list item in an audio format description.
- [func CMAudioFormatDescriptionGetStreamBasicDescription(CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription>?](cmaudioformatdescriptiongetstreambasicdescription(_:).md)
  Returns a read-only pointer to the audio stream description in an audio format description.
- [func CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout(CMBlockBuffer, flavor: CMSoundDescriptionFlavor?) -> Bool](cmdoesbigendiansounddescriptionrequirelegacycbrsampletablelayout(_:flavor:).md)
  Returns a Boolean value that indicates whether the sample tables need to use the legacy constant bit-rate encoding layout.
- [func CMSwapBigEndianSoundDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendiansounddescriptiontohost(_:_:).md)
  Converts a sound description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianSoundDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendiansounddescriptiontobig(_:_:).md)
  Converts a sound description data structure from host-endian to big-endian, in place.
- [func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(allocator: CFAllocator?, bigEndianSoundDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMSoundDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](cmaudioformatdescriptioncreatefrombigendiansounddescriptiondata(allocator:bigendiansounddescriptiondata:size:flavor:formatdescriptionout:).md)
  Creates an audio format description from a big-endian sound description data structure.
- [func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianSoundDescriptionBlockBuffer: CMBlockBuffer, flavor: CMSoundDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](cmaudioformatdescriptioncreatefrombigendiansounddescriptionblockbuffer(allocator:bigendiansounddescriptionblockbuffer:flavor:formatdescriptionout:).md)
  Creates an audio format description from a big-endian sound description data structure in a buffer.
- [func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(allocator: CFAllocator?, audioFormatDescription: CMAudioFormatDescription, flavor: CMSoundDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmaudioformatdescriptioncopyasbigendiansounddescriptionblockbuffer(allocator:audioformatdescription:flavor:blockbufferout:).md)
  Copies the contents of an audio format description to a buffer in big-endian byte ordering.
### Working with Video Descriptions
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
### Working with Muxed Descriptions
- [func CMMuxedFormatDescriptionCreate(allocator: CFAllocator?, muxType: CMMuxedStreamType, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMMuxedFormatDescription?>) -> OSStatus](cmmuxedformatdescriptioncreate(allocator:muxtype:extensions:formatdescriptionout:).md)
  Creates a format description for a muxed media stream.
### Working with Metadata Descriptions
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
- [func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(allocator: CFAllocator?, metadataType: CMMetadataFormatType, metadataSpecifications: CFArray, formatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](cmmetadataformatdescriptioncreatewithmetadataspecifications(allocator:metadatatype:metadataspecifications:formatdescriptionout:).md)
  Creates a metadata format description with the specifications you specify.
- [func CMSwapBigEndianMetadataDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendianmetadatadescriptiontohost(_:_:).md)
  Converts a metadata description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianMetadataDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendianmetadatadescriptiontobig(_:_:).md)
  Converts a metadata description data structure from host-endian to big-endian, in place.
- [func CMMetadataFormatDescriptionGetIdentifiers(CMMetadataFormatDescription) -> CFArray?](cmmetadataformatdescriptiongetidentifiers(_:).md)
  Returns an array of metadata identifiers from a metadata format description.
### Working with Text Descriptions
- [struct CMTextDescriptionFlavor](cmtextdescriptionflavor.md)
  Types that represent text format descriptions.
- [func CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription, localFontIDOut: UnsafeMutablePointer<UInt16>?, boldOut: UnsafeMutablePointer<DarwinBoolean>?, italicOut: UnsafeMutablePointer<DarwinBoolean>?, underlineOut: UnsafeMutablePointer<DarwinBoolean>?, fontSizeOut: UnsafeMutablePointer<CGFloat>?, colorComponentsOut: UnsafeMutablePointer<CGFloat>?) -> OSStatus](cmtextformatdescriptiongetdefaultstyle(_:localfontidout:boldout:italicout:underlineout:fontsizeout:colorcomponentsout:).md)
  Returns the default text style.
- [func CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescription, originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat, defaultTextBoxOut: UnsafeMutablePointer<CGRect>) -> OSStatus](cmtextformatdescriptiongetdefaulttextbox(_:originisattopleft:heightoftexttrack:defaulttextboxout:).md)
  Returns the default text box.
- [func CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription, displayFlagsOut: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus](cmtextformatdescriptiongetdisplayflags(_:displayflagsout:).md)
  Returns the display flags.
- [func CMTextFormatDescriptionGetFontName(CMFormatDescription, localFontID: UInt16, fontNameOut: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus](cmtextformatdescriptiongetfontname(_:localfontid:fontnameout:).md)
  Returns a font name for a local font identifier.
- [func CMTextFormatDescriptionGetJustification(CMFormatDescription, horizontalOut: UnsafeMutablePointer<CMTextJustificationValue>?, verticalOut: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus](cmtextformatdescriptiongetjustification(_:horizontalout:verticalout:).md)
  Returns the horizontal and vertical justification.
- [func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, textFormatDescription: CMTextFormatDescription, flavor: CMTextDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmtextformatdescriptioncopyasbigendiantextdescriptionblockbuffer(allocator:textformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a text format description to a buffer in big-endian byte order.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianTextDescriptionBlockBuffer: CMBlockBuffer, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](cmtextformatdescriptioncreatefrombigendiantextdescriptionblockbuffer(allocator:bigendiantextdescriptionblockbuffer:flavor:mediatype:formatdescriptionout:).md)
  Creates a text format description from a big-endian text description structure inside a buffer.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(allocator: CFAllocator?, bigEndianTextDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](cmtextformatdescriptioncreatefrombigendiantextdescriptiondata(allocator:bigendiantextdescriptiondata:size:flavor:mediatype:formatdescriptionout:).md)
  Creates a text format description from a big-endian text description structure.
- [func CMSwapBigEndianTextDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendiantextdescriptiontohost(_:_:).md)
  Converts a text description structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTextDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendiantextdescriptiontobig(_:_:).md)
  Converts a text description structure from host-endian to big-endian, in place.
### Working with Time Code Descriptions
- [struct CMTimeCodeDescriptionFlavor](cmtimecodedescriptionflavor.md)
  Types that represent time code format descriptions.
- [func CMTimeCodeFormatDescriptionCreate(allocator: CFAllocator?, timeCodeFormatType: CMTimeCodeFormatType, frameDuration: CMTime, frameQuanta: UInt32, flags: UInt32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](cmtimecodeformatdescriptioncreate(allocator:timecodeformattype:frameduration:framequanta:flags:extensions:formatdescriptionout:).md)
  Creates a format description for time code media.
- [func CMTimeCodeFormatDescriptionGetFrameDuration(CMTimeCodeFormatDescription) -> CMTime](cmtimecodeformatdescriptiongetframeduration(_:).md)
  Returns the duration of each frame.
- [func CMTimeCodeFormatDescriptionGetFrameQuanta(CMTimeCodeFormatDescription) -> UInt32](cmtimecodeformatdescriptiongetframequanta(_:).md)
  Returns the frames per second for a time code, or frames per tick in counter mode.
- [func CMTimeCodeFormatDescriptionGetTimeCodeFlags(CMTimeCodeFormatDescription) -> UInt32](cmtimecodeformatdescriptiongettimecodeflags(_:).md)
  Returns time code flags.
- [func CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(allocator: CFAllocator?, timeCodeFormatDescription: CMTimeCodeFormatDescription, flavor: CMTimeCodeDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmtimecodeformatdescriptioncopyasbigendiantimecodedescriptionblockbuffer(allocator:timecodeformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a time code format description to a buffer in big-endian byte order.
- [func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianTimeCodeDescriptionBlockBuffer: CMBlockBuffer, flavor: CMTimeCodeDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](cmtimecodeformatdescriptioncreatefrombigendiantimecodedescriptionblockbuffer(allocator:bigendiantimecodedescriptionblockbuffer:flavor:formatdescriptionout:).md)
  Creates a time code format description from a big-endian time code description data structure in a buffer.
- [func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(allocator: CFAllocator?, bigEndianTimeCodeDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTimeCodeDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](cmtimecodeformatdescriptioncreatefrombigendiantimecodedescriptiondata(allocator:bigendiantimecodedescriptiondata:size:flavor:formatdescriptionout:).md)
  Creates a time code format description from a big-endian time code description structure.
- [func CMSwapBigEndianTimeCodeDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendiantimecodedescriptiontohost(_:_:).md)
  Converts a time code description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTimeCodeDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendiantimecodedescriptiontobig(_:_:).md)
  Converts a time code description data structure from host-endian to big-endian, in place.
### Working with Closed Captioning Descriptions
- [struct CMClosedCaptionDescriptionFlavor](cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer(allocator:closedcaptionformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer(allocator:bigendianclosedcaptiondescriptionblockbuffer:flavor:formatdescriptionout:).md)
  Creates a closed caption format description from a big-endian closed caption description structure in a buffer.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata(allocator:bigendianclosedcaptiondescriptiondata:size:flavor:formatdescriptionout:).md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendianclosedcaptiondescriptiontobig(_:_:).md)
  Converts a closed caption description structure from host-endian to big-endian, in place.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendianclosedcaptiondescriptiontohost(_:_:).md)
  Converts a closed caption description structure from big-endian to host-endian, in place.
### Format Description Types
- [class CMFormatDescription](cmformatdescription.md)
  An object that describes a media format descriptor.
- [typealias CMAudioFormatDescription](cmaudioformatdescription.md)
  A type you use to interact with audio format descriptions.
- [typealias CMClosedCaptionFormatDescription](cmclosedcaptionformatdescription.md)
  A type you use to interact with closed caption format descriptions.
- [typealias CMMetadataFormatDescription](cmmetadataformatdescription.md)
  A type you use to interact with metadata format descriptions.
- [typealias CMMuxedFormatDescription](cmmuxedformatdescription.md)
  A type you use to interact with muxed format descriptions.
- [typealias CMTextFormatDescription](cmtextformatdescription.md)
  A type you use to interact with text format descriptions.
- [typealias CMTimeCodeFormatDescription](cmtimecodeformatdescription.md)
  A type you use to interact with time code format descriptions.
- [typealias CMVideoFormatDescription](cmvideoformatdescription.md)
  A type you use to interact with video format descriptions.
### Format Description Extension Keys
- [let kCMFormatDescriptionExtension_ContentColorVolume: CFString](kcmformatdescriptionextension_contentcolorvolume.md)
- [let kCMFormatDescriptionExtension_HasAdditionalViews: CFString](kcmformatdescriptionextension_hasadditionalviews.md)
- [let kCMFormatDescriptionExtension_HasLeftStereoEyeView: CFString](kcmformatdescriptionextension_hasleftstereoeyeview.md)
- [let kCMFormatDescriptionExtension_HasRightStereoEyeView: CFString](kcmformatdescriptionextension_hasrightstereoeyeview.md)
- [let kCMFormatDescriptionExtension_HeroEye: CFString](kcmformatdescriptionextension_heroeye.md)
- [let kCMFormatDescriptionExtension_HorizontalDisparityAdjustment: CFString](kcmformatdescriptionextension_horizontaldisparityadjustment.md)
- [let kCMFormatDescriptionExtension_LogTransferFunction: CFString](kcmformatdescriptionextension_logtransferfunction.md)
- [let kCMFormatDescriptionExtension_StereoCameraBaseline: CFString](kcmformatdescriptionextension_stereocamerabaseline.md)
- [let kCMFormatDescriptionHeroEye_Left: CFString](kcmformatdescriptionheroeye_left.md)
- [let kCMFormatDescriptionHeroEye_Right: CFString](kcmformatdescriptionheroeye_right.md)
### Format Types
- [typealias CMClosedCaptionFormatType](cmclosedcaptionformattype.md)
  A closed caption format type.
- [typealias CMMetadataFormatType](cmmetadataformattype.md)
  A metadata format type.
- [Metadata Format Types](metadata-format-types.md)
  Constants that represent media format types.
- [typealias CMSubtitleFormatType](cmsubtitleformattype.md)
  A type that represents a text subtitle format.
- [Subtitle Format Types](subtitle-format-types.md)
  Constants that represent subtitle format types.
- [typealias CMTimeCodeFormatType](cmtimecodeformattype.md)
  A time code format type.
- [Time Code Formats](time-code-formats.md)
  Constants that represent time code format types.
- [typealias CMTextFormatType](cmtextformattype.md)
  A text format type.
- [typealias CMPixelFormatType](cmpixelformattype.md)
  A pixel format type.
- [Tagged Buffer Group Format Types](tagged-buffergroup-format-types.md)
### Data Types
- [struct CMVideoDimensions](cmvideodimensions.md)
  A structure that represents video dimensions.
- [typealias CMAudioFormatDescriptionMask](cmaudioformatdescriptionmask.md)
  A type for mask bits that represent parts of an audio format description.
- [typealias CMMediaType](cmmediatype.md)
  Constants that represent media types.
- [typealias CMAudioCodecType](cmaudiocodectype.md)
  An audio codec type.
- [typealias CMVideoCodecType](cmvideocodectype.md)
  A video codec type.
- [typealias CMTextDisplayFlags](cmtextdisplayflags.md)
  An integer value that describes the display mode flags for text media.
- [typealias CMTextJustificationValue](cmtextjustificationvalue.md)
  An integer value that describes the justification modes for text media.
- [Media Type Constants](media-type-constants.md)
  Constants that represent media types.
- [Muxed Stream Types](muxed-stream-types.md)
  Constants that represent muxed stream types.
- [Audio Codec Types](audio-codec-types.md)
  Constants that represent audio codec types.
### Constants
- [Format Description Error Codes](format-description-errors.md)
  Errors the system returns from format description calls.
- [Format Description Bridge Error Codes](format-description-bridge-errors.md)
  Bridge errors the system returns from format description calls.
- [Format Description Constants](format-description-constants.md)
  Constants that identify format descriptions.
- [Text Format Description Constants](text-format-description-constants.md)
  Constants that identify text format descriptions.
- [Metadata Format Description Constants](metadata-format-description-constants.md)
  Constants that identify metadata format descriptions.
- [Time Code Format Description Constants](time-code-format-description-constants.md)
  Constants that identify time code format descriptions.
- [Pixel Aspect Ratio Extension Constants](pixel-aspect-ratio-extension-constants.md)
  Constants that identify pixel aspect ratio extensions.
- [Chroma Location Extension Constants](chroma-location-extension-constants.md)
  Constants that identify chroma location extensions.
- [Clean Aperture Extension Constants](clean-aperture-extension-constants.md)
  Constants that identify clean aperture extensions.
- [Color Primary Extension Constants](color-primary-extension-constants.md)
  Constants that identify color primary extensions.
- [Field Detail Extension Constants](field-detail-extension-constants.md)
  Constants that identify field detail extensions.
- [Transfer Function Extension Constants](transfer-function-extension-constants.md)
  Constants that identify transfer function extensions.
- [MPEG-2-conformant Formats](mpeg-2-conformant-formats.md)
  Constants that identify MPEG-2 formats.
- [HEVC Temporal Level Info Constants](hevc-temporal-level-info-constants.md)
  Constants that identify HEVC temporal level information.
- [YCbCrMatrix Extension Constants](ycbcrmatrix-extension-constants.md)
  Constants that identify YCbCrMatrix extensions.
- [Audio Format Description Mask Codes](audio-format-desc-codes.md)
  Mask codes that identify audio formats.
- [Closed Caption Format Type Constants](closed-caption-formats.md)
  Types that identify closed caption formats.
- [Time Code Flags](time-code-flags.md)
  Flags that identify time codes.
- [Text Display Flags](text-display-flags.md)
  Flags that identify text display methods.
- [Text Format Constants](text-format-constants.md)
  Types that identify text formats.
- [Text Justification Constants](text-justification-constants.md)
  Types that identify text justifications.
- [Video Pixel Formats](video-pixel-formats.md)
  Constants that identify video pixel formats.
- [Video Profile Constants](video-profile-constants.md)
  Constants that identify video profiles.
- [Video Codec Constants](video-codec-constants.md)
  Types that identify video codecs.

## See Also

- [CMSampleBuffer APIs](cmsamplebuffer-api.md)
  An object that contains zero or more media samples of a uniform media type.
- [CMBlockBuffer APIs](cmblockbuffer-api.md)
  An object the system uses to move blocks of memory through a processing system.
- [struct CMTaggedBuffer](cmtaggedbuffer.md)
  An instance of a media buffer containing metadata tags.
- [CMTaggedBufferGroup APIs](cmtaggedbuffergroup.md)
  Objective-C types and interfaces for working with Core Media tagged buffer groups.
- [CMAttachment APIs](cmattachment-api.md)
  Add supporting metadata to sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription-api)*