# CMClosedCaptionDescriptionFlavor

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

Types that represent closed caption format descriptions.

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
struct CMClosedCaptionDescriptionFlavor
```

```c
typedef CFStringRef CMClosedCaptionDescriptionFlavor;
```

## Topics

### Initializers
- [init(CFString)](./cmclosedcaptiondescriptionflavor/init%28_%29.md)
  Creates a closed caption description flavor.
- [init(rawValue: CFString)](./cmclosedcaptiondescriptionflavor/init%28rawvalue%29.md)
  Creates a closed caption description flavor.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Closed Captioning Descriptions
- [func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, closedCaptionFormatDescription: CMClosedCaptionFormatDescription, flavor: CMClosedCaptionDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmclosedcaptionformatdescriptioncopyasbigendianclosedcaptiondescriptionblockbuffer%28allocator,closedcaptionformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a closed caption format description to a buffer in big-endian byte order.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionBlockBuffer: CMBlockBuffer, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptionblockbuffer%28allocator,bigendianclosedcaptiondescriptionblockbuffer,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure in a buffer.
- [func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(allocator: CFAllocator?, bigEndianClosedCaptionDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMClosedCaptionDescriptionFlavor?, formatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](./cmclosedcaptionformatdescriptioncreatefrombigendianclosedcaptiondescriptiondata%28allocator,bigendianclosedcaptiondescriptiondata,size,flavor,formatdescriptionout%29.md)
  Creates a closed caption format description from a big-endian closed caption description structure.
- [func CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendianclosedcaptiondescriptiontobig%28_,_%29.md)
  Converts a closed caption description structure from host-endian to big-endian, in place.
- [func CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendianclosedcaptiondescriptiontohost%28_,_%29.md)
  Converts a closed caption description structure from big-endian to host-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclosedcaptiondescriptionflavor)*