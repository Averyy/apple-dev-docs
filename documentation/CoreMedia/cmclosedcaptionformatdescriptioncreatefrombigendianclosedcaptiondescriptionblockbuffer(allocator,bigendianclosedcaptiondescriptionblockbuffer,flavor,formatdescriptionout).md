# CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator:bigEndianClosedCaptionDescriptionBlockBuffer:flavor:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a closed caption format description from a big-endian closed caption description structure in a buffer.

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
func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer closedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus
```

```c
extern OSStatus CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(CFAllocatorRef allocator, CMBlockBufferRef closedCaptionDescriptionBlockBuffer, CMClosedCaptionDescriptionFlavor flavor, CMClosedCaptionFormatDescriptionRef*formatDescriptionOut);
```

## Parameters

- `allocator`: Allocator to use for allocating the `CMClosedCaptionFormatDescription` object. May be `NULL`.
- `closedCaptionDescriptionBlockBuffer`: `CMBlockBuffer` containing ClosedCaptionDescription data structure in big-endian byte ordering.
- `flavor`: Reserved for future use. Pass `NULL` for QuickTime Movie or ISO flavor.
- `formatDescriptionOut`: Receives new `CMClosedCaptionFormatDescription`.

## See Also

### Working with Closed Captioning Descriptions
- [struct CMClosedCaptionDescriptionFlavor](./cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer%28allocator,closedcaptionformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata%28allocator,bigendianclosedcaptiondescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianclosedcaptiondescriptiontobig%28_,_%29.md)
  Converts a closed caption description structure from host-endian to big-endian, in place.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendianclosedcaptiondescriptiontohost%28_,_%29.md)
  Converts a closed caption description structure from big-endian to host-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer(allocator:bigendianclosedcaptiondescriptionblockbuffer:flavor:formatdescriptionout:))*