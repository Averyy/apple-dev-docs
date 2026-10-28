# CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator:closedCaptionFormatDescription:flavor:blockBufferOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Copies the contents of a closed caption format description to a buffer in big-endian byte order.

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
func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus
```

```c
extern OSStatus CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(CFAllocatorRef allocator, CMClosedCaptionFormatDescriptionRef closedCaptionFormatDescription, CMClosedCaptionDescriptionFlavor flavor, CMBlockBufferRef*blockBufferOut);
```

## Discussion

On return, the caller owns the returned CMBlockBuffer, and must release it when done with it.

> **Note**:  The `dataRefIndex` field of the SampleDescription is intentionally filled with placeholder values (`0xFFFF`). The caller must overwrite these values with a valid `dataRefIndex` if writing the SampleDescription to a QuickTime/ISO file.

## Parameters

- `allocator`: Allocator to use for allocating the `CMBlockBuffer` object. May be `NULL`.
- `closedCaptionFormatDescription`: The `CMClosedCaptionFormatDescription` to be copied.
- `flavor`: Reserved for future use. Pass `NULL` for QuickTime Movie or ISO flavor.
- `blockBufferOut`: Receives new `CMBlockBuffer` containing ClosedCaptionDescription data structure in big-endian byte ordering.

## See Also

### Working with Closed Captioning Descriptions
- [struct CMClosedCaptionDescriptionFlavor](./cmclosedcaptiondescriptionflavor.md)
  Types that represent closed caption format descriptions.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer%28allocator,bigendianclosedcaptiondescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure in a buffer.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata%28allocator,bigendianclosedcaptiondescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianclosedcaptiondescriptiontobig%28_,_%29.md)
  Converts a closed caption description structure from host-endian to big-endian, in place.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendianclosedcaptiondescriptiontohost%28_,_%29.md)
  Converts a closed caption description structure from big-endian to host-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer(allocator:closedcaptionformatdescription:flavor:blockbufferout:))*