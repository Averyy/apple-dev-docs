# CMSwapHostEndianClosedCaptionDescriptionToBig(_:_:)

**Framework**: Core Media  
**Kind**: func

Converts a closed caption description structure from host-endian to big-endian, in place.

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
func CMSwapHostEndianClosedCaptionDescriptionToBig(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: Int) -> OSStatus
```

## Parameters

- `closedCaptionDescriptionData`: ClosedCaptionDescription data structure in host-endian byte ordering to be converted to big-endian byte ordering.
- `closedCaptionDescriptionSize`: Size of ClosedCaptionDescription data structure.

## See Also

- [struct CMClosedCaptionDescriptionFlavor](cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer(allocator:closedcaptionformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer(allocator:bigendianclosedcaptiondescriptionblockbuffer:flavor:formatdescriptionout:).md)
  Creates a closed caption format description from a big-endian closed caption description structure in a buffer.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata(allocator:bigendianclosedcaptiondescriptiondata:size:flavor:formatdescriptionout:).md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendianclosedcaptiondescriptiontohost(_:_:).md)
  Converts a closed caption description structure from big-endian to host-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmswaphostendianclosedcaptiondescriptiontobig(_:_:))*