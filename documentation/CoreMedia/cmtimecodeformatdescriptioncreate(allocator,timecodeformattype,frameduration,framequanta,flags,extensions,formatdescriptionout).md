# CMTimeCodeFormatDescriptionCreate(allocator:timeCodeFormatType:frameDuration:frameQuanta:flags:extensions:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a format description for time code media.

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
func CMTimeCodeFormatDescriptionCreate(allocator: CFAllocator?, timeCodeFormatType: CMTimeCodeFormatType, frameDuration: CMTime, frameQuanta: UInt32, flags: UInt32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus
```

```c
extern OSStatus CMTimeCodeFormatDescriptionCreate(CFAllocatorRef allocator, CMTimeCodeFormatType timeCodeFormatType, CMTime frameDuration, uint32_t frameQuanta, uint32_t flags, CFDictionaryRef extensions, CMTimeCodeFormatDescriptionRef*formatDescriptionOut);
```

#### Return Value

A result code. Returns `noErr` if successful.

#### Discussion

The caller owns the returned `CMFormatDescription`, and must release it when done with it. All input parameters are copied (the extensions are deep-copied).  The caller can deallocate them or re-use them after making this call.

## Parameters

- `allocator`: Allocator to be used for creating the `CMFormatDescription` object.
- `timeCodeFormatType`: One of the [`CMTimeCodeFormatType`](./cmtimecodeformattype.md).
- `frameDuration`: Duration of each frame (e.g. `100/2997`).
- `frameQuanta`: Frames/sec for timecode (e.g. 30) OR frames/tick for counter mode.
- `flags`: `kCMTimeCodeFlag_DropFrame`, `kCMTimeCodeFlag_24HourMax`, `kCMTimeCodeFlag_NegTimesOK`. For possible values, see [Video Profile Constants](./video-profile-constants.md).
- `extensions`: Keys are always `CFStrings`. Values are always property list objects (i.e. `CFData`). May be NULL.
- `formatDescriptionOut`: Receives the newly-created `CMFormatDescription`.

## See Also

### Working with Time Code Descriptions
- [struct CMTimeCodeDescriptionFlavor](./cmtimecodedescriptionflavor.md)
  Types that represent time code format descriptions.
- [func CMTimeCodeFormatDescriptionGetFrameDuration(CMTimeCodeFormatDescription) -> CMTime](./cmtimecodeformatdescriptiongetframeduration%28_%29.md)
  Returns the duration of each frame.
- [func CMTimeCodeFormatDescriptionGetFrameQuanta(CMTimeCodeFormatDescription) -> UInt32](./cmtimecodeformatdescriptiongetframequanta%28_%29.md)
  Returns the frames per second for a time code, or frames per tick in counter mode.
- [func CMTimeCodeFormatDescriptionGetTimeCodeFlags(CMTimeCodeFormatDescription) -> UInt32](./cmtimecodeformatdescriptiongettimecodeflags%28_%29.md)
  Returns time code flags.
- [func CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(allocator: CFAllocator?, timeCodeFormatDescription: CMTimeCodeFormatDescription, flavor: CMTimeCodeDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmtimecodeformatdescriptioncopyasbigendiantimecodedescriptionblockbuffer%28allocator,timecodeformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a time code format description to a buffer in big-endian byte order.
- [func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianTimeCodeDescriptionBlockBuffer: CMBlockBuffer, flavor: CMTimeCodeDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](./cmtimecodeformatdescriptioncreatefrombigendiantimecodedescriptionblockbuffer%28allocator,bigendiantimecodedescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates a time code format description from a big-endian time code description data structure in a buffer.
- [func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(allocator: CFAllocator?, bigEndianTimeCodeDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTimeCodeDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](./cmtimecodeformatdescriptioncreatefrombigendiantimecodedescriptiondata%28allocator,bigendiantimecodedescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates a time code format description from a big-endian time code description structure.
- [func CMSwapBigEndianTimeCodeDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendiantimecodedescriptiontohost%28_,_%29.md)
  Converts a time code description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTimeCodeDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendiantimecodedescriptiontobig%28_,_%29.md)
  Converts a time code description data structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecodeformatdescriptioncreate(allocator:timecodeformattype:frameduration:framequanta:flags:extensions:formatdescriptionout:))*