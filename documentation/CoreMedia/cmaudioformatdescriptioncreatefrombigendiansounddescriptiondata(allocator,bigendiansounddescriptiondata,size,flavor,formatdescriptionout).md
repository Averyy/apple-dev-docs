# CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(allocator:bigEndianSoundDescriptionData:size:flavor:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates an audio format description from a big-endian sound description data structure.

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
func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(allocator: CFAllocator?, bigEndianSoundDescriptionData soundDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMSoundDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus
```

## Parameters

- `allocator`: Allocator to use for allocating the CMAudioFormatDescription object. May be NULL.
- `soundDescriptionData`: SoundDescription data structure in big-endian byte ordering.
- `size`: Size of SoundDescription data structure.
- `flavor`: kCMSoundDescriptionFlavor constant or NULL for QuickTimeMovie flavor.
- `formatDescriptionOut`: Receives new CMAudioFormatDescription.

## See Also

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
- [func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianSoundDescriptionBlockBuffer: CMBlockBuffer, flavor: CMSoundDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](cmaudioformatdescriptioncreatefrombigendiansounddescriptionblockbuffer(allocator:bigendiansounddescriptionblockbuffer:flavor:formatdescriptionout:).md)
  Creates an audio format description from a big-endian sound description data structure in a buffer.
- [func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(allocator: CFAllocator?, audioFormatDescription: CMAudioFormatDescription, flavor: CMSoundDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmaudioformatdescriptioncopyasbigendiansounddescriptionblockbuffer(allocator:audioformatdescription:flavor:blockbufferout:).md)
  Copies the contents of an audio format description to a buffer in big-endian byte ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudioformatdescriptioncreatefrombigendiansounddescriptiondata(allocator:bigendiansounddescriptiondata:size:flavor:formatdescriptionout:))*