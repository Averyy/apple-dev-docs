# CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(allocator:bigEndianTimeCodeDescriptionData:size:flavor:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a time code format description from a big-endian time code description structure.

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
func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(allocator: CFAllocator?, bigEndianTimeCodeDescriptionData timeCodeDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTimeCodeDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus
```

```c
extern OSStatus CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(CFAllocatorRef allocator, const uint8_t *timeCodeDescriptionData, size_t size, CMTimeCodeDescriptionFlavor flavor, CMTimeCodeFormatDescriptionRef*formatDescriptionOut);
```

## Parameters

- `allocator`: Allocator to use for allocating the CMTimeCodeFormatDescription object. May be NULL.
- `timeCodeDescriptionData`: TimeCodeDescription data structure in big-endian byte ordering.
- `size`: Size of TimeCodeDescription data structure.
- `flavor`: Reserved for future use. Pass NULL for QuickTime Movie or ISO flavor.
- `formatDescriptionOut`: Receives new CMTimeCodeFormatDescription.

## See Also

### Working with Time Code Descriptions
- [struct CMTimeCodeDescriptionFlavor](./cmtimecodedescriptionflavor.md)
  Types that represent time code format descriptions.
- [func CMTimeCodeFormatDescriptionCreate(allocator: CFAllocator?, timeCodeFormatType: CMTimeCodeFormatType, frameDuration: CMTime, frameQuanta: UInt32, flags: UInt32, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](./cmtimecodeformatdescriptioncreate%28allocator,timecodeformattype,frameduration,framequanta,flags,extensions,formatdescriptionout%29.md)
  Creates a format description for time code media.
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
- [func CMSwapBigEndianTimeCodeDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendiantimecodedescriptiontohost%28_,_%29.md)
  Converts a time code description data structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTimeCodeDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendiantimecodedescriptiontobig%28_,_%29.md)
  Converts a time code description data structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecodeformatdescriptioncreatefrombigendiantimecodedescriptiondata(allocator:bigendiantimecodedescriptiondata:size:flavor:formatdescriptionout:))*