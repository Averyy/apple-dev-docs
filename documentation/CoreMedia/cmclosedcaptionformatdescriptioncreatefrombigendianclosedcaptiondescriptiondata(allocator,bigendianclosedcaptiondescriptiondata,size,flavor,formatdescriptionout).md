# CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator:bigEndianClosedCaptionDescriptionData:size:flavor:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a closed caption format description from a big-endian closed caption description structure.

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
func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData closedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus
```

```c
extern OSStatus CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(CFAllocatorRef allocator, const uint8_t *closedCaptionDescriptionData, size_t size, CMClosedCaptionDescriptionFlavor flavor, CMClosedCaptionFormatDescriptionRef*formatDescriptionOut);
```

## Parameters

- `allocator`: Allocator to use for allocating the `CMClosedCaptionFormatDescription` object. May be `NULL`.
- `closedCaptionDescriptionData`: ClosedCaptionDescription data structure in big-endian byte ordering.
- `size`: Size of ClosedCaptionDescription data structure.
- `flavor`: Reserved for future use. Pass `NULL` for QuickTime Movie or ISO flavor.
- `formatDescriptionOut`: Receives new `CMClosedCaptionFormatDescription`.

## See Also

### Working with Closed Captioning Descriptions
- [struct CMClosedCaptionDescriptionFlavor](./cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer%28allocator,closedcaptionformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer%28allocator,bigendianclosedcaptiondescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure in a buffer.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianclosedcaptiondescriptiontobig%28_,_%29.md)
  Converts a closed caption description structure from host-endian to big-endian, in place.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendianclosedcaptiondescriptiontohost%28_,_%29.md)
  Converts a closed caption description structure from big-endian to host-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata(allocator:bigendianclosedcaptiondescriptiondata:size:flavor:formatdescriptionout:))*