# CMTextFormatDescriptionGetFontName(_:localFontID:fontNameOut:)

**Framework**: Core Media  
**Kind**: func

Returns a font name for a local font identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTextFormatDescriptionGetFontName(_ desc: CMFormatDescription, localFontID: UInt16, fontNameOut: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus
```

#### Return Value

A result code. Returns `noErr` if successful.

## Parameters

- `desc`:   being interrogated.
- `localFontID`: Font number, local to the FormatDescription.
- `fontNameOut`: On output, returns name of the font. The returned font is not retained by this call, so clients are required to retain it if they need to keep it longer.

## See Also

- [struct CMTextDescriptionFlavor](cmtextdescriptionflavor.md)
  Types that represent text format descriptions.
- [func CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription, localFontIDOut: UnsafeMutablePointer<UInt16>?, boldOut: UnsafeMutablePointer<DarwinBoolean>?, italicOut: UnsafeMutablePointer<DarwinBoolean>?, underlineOut: UnsafeMutablePointer<DarwinBoolean>?, fontSizeOut: UnsafeMutablePointer<CGFloat>?, colorComponentsOut: UnsafeMutablePointer<CGFloat>?) -> OSStatus](cmtextformatdescriptiongetdefaultstyle(_:localfontidout:boldout:italicout:underlineout:fontsizeout:colorcomponentsout:).md)
  Returns the default text style.
- [func CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescription, originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat, defaultTextBoxOut: UnsafeMutablePointer<CGRect>) -> OSStatus](cmtextformatdescriptiongetdefaulttextbox(_:originisattopleft:heightoftexttrack:defaulttextboxout:).md)
  Returns the default text box.
- [func CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription, displayFlagsOut: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus](cmtextformatdescriptiongetdisplayflags(_:displayflagsout:).md)
  Returns the display flags.
- [func CMTextFormatDescriptionGetJustification(CMFormatDescription, horizontalOut: UnsafeMutablePointer<CMTextJustificationValue>?, verticalOut: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus](cmtextformatdescriptiongetjustification(_:horizontalout:verticalout:).md)
  Returns the horizontal and vertical justification.
- [func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, textFormatDescription: CMTextFormatDescription, flavor: CMTextDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmtextformatdescriptioncopyasbigendiantextdescriptionblockbuffer(allocator:textformatdescription:flavor:blockbufferout:).md)
  Copies the contents of a text format description to a buffer in big-endian byte order.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianTextDescriptionBlockBuffer: CMBlockBuffer, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](cmtextformatdescriptioncreatefrombigendiantextdescriptionblockbuffer(allocator:bigendiantextdescriptionblockbuffer:flavor:mediatype:formatdescriptionout:).md)
  Creates a text format description from a big-endian text description structure inside a buffer.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(allocator: CFAllocator?, bigEndianTextDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](cmtextformatdescriptioncreatefrombigendiantextdescriptiondata(allocator:bigendiantextdescriptiondata:size:flavor:mediatype:formatdescriptionout:).md)
  Creates a text format description from a big-endian text description structure.
- [func CMSwapBigEndianTextDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswapbigendiantextdescriptiontohost(_:_:).md)
  Converts a text description structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTextDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](cmswaphostendiantextdescriptiontobig(_:_:).md)
  Converts a text description structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtextformatdescriptiongetfontname(_:localfontid:fontnameout:))*