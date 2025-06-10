# CMTimeCodeDescriptionFlavor

**Framework**: Core Media  
**Kind**: struct

Types that represent time code format descriptions.

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
struct CMTimeCodeDescriptionFlavor
```

## Topics

### Creating a Timecode Description Flavor
- [init(CFString)](cmtimecodedescriptionflavor/init(_:).md)
  Creates a time code description flavor.
- [init(rawValue: CFString)](cmtimecodedescriptionflavor/init(rawvalue:).md)
  Creates a time code description flavor.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecodedescriptionflavor)*