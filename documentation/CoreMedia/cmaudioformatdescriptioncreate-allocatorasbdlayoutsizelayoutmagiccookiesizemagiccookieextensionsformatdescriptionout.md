# CMAudioFormatDescriptionCreate(allocator:asbd:layoutSize:layout:magicCookieSize:magicCookie:extensions:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates a format description for an audio media stream.

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
func CMAudioFormatDescriptionCreate(allocator: CFAllocator?, asbd: UnsafePointer<AudioStreamBasicDescription>, layoutSize: Int, layout: UnsafePointer<AudioChannelLayout>?, magicCookieSize: Int, magicCookie: UnsafeRawPointer?, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

The `absd` is required, the channel layout is optional, and the magic cookie is required  for some compression formats (and must be NULL for all others). The caller owns the returned `CMFormatDescription`, and must release it when done with it.  The `ASBD`, magic cookie, channel layout, and extensions are all copied (the extensions are deep-copied).  The caller can deallocate them or re-use them after making this call.

## Parameters

- `allocator`:   to be used. Pass   or   to use the default allocator.
- `asbd`: Audio format description (see  ). This information is required.
- `layoutSize`: Size, in bytes, of audio channel layout. 0 if layout is  .
- `layout`: Audio channel layout (see CoreAudioTypes.h). Can be  .
- `magicCookieSize`: Size, in bytes, of magic cookie. 0 if   is  .
- `magicCookie`: Magic cookie. This information is required for some formats, and must be   for all others.
- `extensions`: Dictionary of extension key/value pairs.  Keys are always  .                                                                            Values are always property list objects (ie.  ,  ,  ,  ,  ,  , or  ). Can be  .
- `formatDescriptionOut`: On output, returns the newly created audio  .

## See Also

- [struct CMSoundDescriptionFlavor](cmsounddescriptionflavor.md)
  Types that represent sound format descriptions.
- [func CMAudioFormatDescriptionCreateSummary(allocator: CFAllocator?, formatDescriptionArray: CFArray, flags: UInt32, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](cmaudioformatdescriptioncreatesummary(allocator:formatdescriptionarray:flags:formatdescriptionout:).md)
  Creates a summary audio format description from an array of descriptions.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudioformatdescriptioncreate(allocator:asbd:layoutsize:layout:magiccookiesize:magiccookie:extensions:formatdescriptionout:))*