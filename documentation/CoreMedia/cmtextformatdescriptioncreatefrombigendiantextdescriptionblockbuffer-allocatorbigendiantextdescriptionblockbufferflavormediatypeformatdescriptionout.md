# CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(allocator:bigEndianTextDescriptionBlockBuffer:flavor:mediaType:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates a text format description from a big-endian text description structure inside a buffer.

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
func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianTextDescriptionBlockBuffer textDescriptionBlockBuffer: CMBlockBuffer, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus
```

## Parameters

- `allocator`: Allocator to use for allocating the CMTextFormatDescription object. May be NULL.
- `textDescriptionBlockBuffer`: CMBlockBuffer containing TextDescription data structure in big-endian byte ordering.
- `flavor`: Reserved for future use. Pass NULL for QuickTime Movie or ISO flavor.
- `mediaType`: Pass kCMMediaType_Text or kCMMediaType_Subtitle.
- `formatDescriptionOut`: Receives new CMTextFormatDescription.

## See Also

- [struct CMTextDescriptionFlavor](cmtextdescriptionflavor.md)
  Types that represent text format descriptions.
- [func CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription, localFontIDOut: UnsafeMutablePointer<UInt16>?, boldOut: UnsafeMutablePointer<DarwinBoolean>?, italicOut: UnsafeMutablePointer<DarwinBoolean>?, underlineOut: UnsafeMutablePointer<DarwinBoolean>?, fontSizeOut: UnsafeMutablePointer<CGFloat>?, colorComponentsOut: UnsafeMutablePointer<CGFloat>?) -> OSStatus](cmtextformatdescriptiongetdefaultstyle(_:localfontidout:boldout:italicout:underlineout:fontsizeout:colorcomponentsout:).md)
  Returns the default text style.
- [func CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescription, originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat, defaultTextBoxOut: UnsafeMutablePointer<CGRect>) -> OSStatus](cmtextformatdescriptiongetdefaulttextbox(_:originisattopleft:heightoftexttrack:defaulttextboxout:).md)
  Returns the default text box.
- [func CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription, displayFlagsOut: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus](cmtextformatdescriptiongetdisplayflags(_:displayflagsout:).md)
  Returns the display flags.
- [func CMTextFormatDescriptionGetFontName(CMFormatDescription, localFontID: UInt16, fontNameOut: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus](cmtextformatdescriptiongetfontname(_:localfontid:fontnameout:).md)
  Returns a font name for a local font identifier.
- [func CMTextFormatDescriptionGetJustification(CMFormatDescription, horizontalOut: UnsafeMutablePointer<CMTextJustificationValue>?, verticalOut: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus](cmtextformatdescriptiongetjustification(_:horizontalout:verticalout:).md)
  Returns the horizontal and vertical justification.
- [func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, textFormatDescription: CMTextFormatDescription, flavor: CMTextDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmtextformatdescriptioncopyasbigendiantextdescriptionblockbuffer(allocator:textformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a text format description to a buffer in big-endian byte order.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(allocator: CFAllocator?, bigEndianTextDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](cmtextformatdescriptioncreatefrombigendiantextdescriptiondata(allocator:bigendiantextdescriptiondata:size:flavor:mediatype:formatdescriptionout:).md)
  Creates a text format description from a big-endian text description structure.
- [func CMSwapBigEndianTextDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendiantextdescriptiontohost(_:_:).md)
  Converts a text description structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTextDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendiantextdescriptiontobig(_:_:).md)
  Converts a text description structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtextformatdescriptioncreatefrombigendiantextdescriptionblockbuffer(allocator:bigendiantextdescriptionblockbuffer:flavor:mediatype:formatdescriptionout:))*