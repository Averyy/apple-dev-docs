# CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator:bigEndianClosedCaptionDescriptionBlockBuffer:flavor:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

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

## Parameters

- `allocator`: Allocator to use for allocating the   object. May be  .
- `closedCaptionDescriptionBlockBuffer`:   containing ClosedCaptionDescription data structure in big-endian byte ordering.
- `flavor`: Reserved for future use. Pass   for QuickTime Movie or ISO flavor.
- `formatDescriptionOut`: Receives new  .

## See Also

- [struct CMClosedCaptionDescriptionFlavor](cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer(allocator:closedcaptionformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata(allocator:bigendianclosedcaptiondescriptiondata:size:flavor:formatdescriptionout:).md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendianclosedcaptiondescriptiontobig(_:_:).md)
  Converts a closed caption description structure from host-endian to big-endian, in place.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendianclosedcaptiondescriptiontohost(_:_:).md)
  Converts a closed caption description structure from big-endian to host-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer(allocator:bigendianclosedcaptiondescriptionblockbuffer:flavor:formatdescriptionout:))*