# CMAudioFormatDescriptionGetMostCompatibleFormat(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a read-only pointer to the appropriate audio format list item in an audio format description.

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
func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>?
```

```c
extern const AudioFormatListItem *CMAudioFormatDescriptionGetMostCompatibleFormat(CMAudioFormatDescriptionRef desc);
```

## Return Value

A read-only pointer to the appropriate `AudioFormatListItem` inside the audio format description.

## Discussion

This property returns a pointer to the most compatible `AudioFormatListItem` in the `kAudioFormatProperty_FormatList`. This API is specific to audio format descriptions, and returns `NULL` if called with a non-audio format description.

## Parameters

- `desc`: `CMFormatDescription` being interrogated.

## See Also

### Working with Audio Descriptions
- [struct CMSoundDescriptionFlavor](./cmsounddescriptionflavor.md)
  Types that represent sound format descriptions.
- [func CMAudioFormatDescriptionCreateSummary(allocator: CFAllocator?, formatDescriptionArray: CFArray, flags: UInt32, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](./cmaudioformatdescriptioncreatesummary%28allocator,formatdescriptionarray,flags,formatdescriptionout%29.md)
  Creates a summary audio format description from an array of descriptions.
- [func CMAudioFormatDescriptionCreate(allocator: CFAllocator?, asbd: UnsafePointer<AudioStreamBasicDescription>, layoutSize: Int, layout: UnsafePointer<AudioChannelLayout>?, magicCookieSize: Int, magicCookie: UnsafeRawPointer?, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](./cmaudioformatdescriptioncreate%28allocator,asbd,layoutsize,layout,magiccookiesize,magiccookie,extensions,formatdescriptionout%29.md)
  Creates a format description for an audio media stream.
- [func CMAudioFormatDescriptionEqual(CMAudioFormatDescription, otherFormatDescription: CMAudioFormatDescription, equalityMask: CMAudioFormatDescriptionMask, equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>?) -> Bool](./cmaudioformatdescriptionequal%28_,otherformatdescription,equalitymask,equalitymaskout%29.md)
  Returns a Boolean value that indicates whether the two audio format descriptions are equal.
- [func CMAudioFormatDescriptionGetChannelLayout(CMAudioFormatDescription, sizeOut: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioChannelLayout>?](./cmaudioformatdescriptiongetchannellayout%28_,sizeout%29.md)
  Returns a read-only pointer to, and the size of, the audio channel layout inside an audio format description.
- [func CMAudioFormatDescriptionGetFormatList(CMAudioFormatDescription, sizeOut: UnsafeMutablePointer<Int>?) -> UnsafePointer<AudioFormatListItem>?](./cmaudioformatdescriptiongetformatlist%28_,sizeout%29.md)
  Returns a read-only pointer to, and size of, the array of audio format list item structures in an audio format description.
- [func CMAudioFormatDescriptionGetMagicCookie(CMAudioFormatDescription, sizeOut: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](./cmaudioformatdescriptiongetmagiccookie%28_,sizeout%29.md)
  Returns a read-only pointer to, and size of, the magic cookie in an audio format description.
- [func CMAudioFormatDescriptionGetRichestDecodableFormat(CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>?](./cmaudioformatdescriptiongetrichestdecodableformat%28_%29.md)
  Returns a read-only pointer to the appropriate audio format list item in an audio format description.
- [func CMAudioFormatDescriptionGetStreamBasicDescription(CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription>?](./cmaudioformatdescriptiongetstreambasicdescription%28_%29.md)
  Returns a read-only pointer to the audio stream description in an audio format description.
- [func CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout(CMBlockBuffer, flavor: CMSoundDescriptionFlavor?) -> Bool](./cmdoesbigendiansounddescriptionrequirelegacycbrsampletablelayout%28_,flavor%29.md)
  Returns a Boolean value that indicates whether the sample tables need to use the legacy constant bit-rate encoding layout.
- [func CMSwapBigEndianSoundDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendiansounddescriptiontohost%28_,_%29.md)
  Converts a sound description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianSoundDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendiansounddescriptiontobig%28_,_%29.md)
  Converts a sound description data structure from host-endian to big-endian, in place.
- [func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(allocator: CFAllocator?, bigEndianSoundDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMSoundDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](./cmaudioformatdescriptioncreatefrombigendiansounddescriptiondata%28allocator,bigendiansounddescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates an audio format description from a big-endian sound description data structure.
- [func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianSoundDescriptionBlockBuffer: CMBlockBuffer, flavor: CMSoundDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](./cmaudioformatdescriptioncreatefrombigendiansounddescriptionblockbuffer%28allocator,bigendiansounddescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates an audio format description from a big-endian sound description data structure in a buffer.
- [func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(allocator: CFAllocator?, audioFormatDescription: CMAudioFormatDescription, flavor: CMSoundDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmaudioformatdescriptioncopyasbigendiansounddescriptionblockbuffer%28allocator,audioformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of an audio format description to a buffer in big-endian byte ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudioformatdescriptiongetmostcompatibleformat(_:))*