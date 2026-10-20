# CMSwapBigEndianClosedCaptionDescriptionToHost(_:_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Converts a closed caption description structure from big-endian to host-endian, in place.

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
func CMSwapBigEndianClosedCaptionDescriptionToHost(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: Int) -> OSStatus
```

```c
extern OSStatus CMSwapBigEndianClosedCaptionDescriptionToHost(uint8_t *closedCaptionDescriptionData, size_t closedCaptionDescriptionSize);
```

## Parameters

- `closedCaptionDescriptionData`: ClosedCaptionDescription data structure in big-endian byte ordering to be converted to host-endian byte ordering.
- `closedCaptionDescriptionSize`: Size of ClosedCaptionDescription data structure.

## See Also

### Working with Closed Captioning Descriptions
- [struct CMClosedCaptionDescriptionFlavor](./cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer%28allocator,closedcaptionformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer%28allocator,bigendianclosedcaptiondescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure in a buffer.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata%28allocator,bigendianclosedcaptiondescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianclosedcaptiondescriptiontobig%28_,_%29.md)
  Converts a closed caption description structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmswapbigendianclosedcaptiondescriptiontohost(_:_:))*