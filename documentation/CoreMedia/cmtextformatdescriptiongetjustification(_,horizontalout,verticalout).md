# CMTextFormatDescriptionGetJustification(_:horizontalOut:verticalOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the horizontal and vertical justification.

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
func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription, horizontalOut horizontaJustificationlOut: UnsafeMutablePointer<CMTextJustificationValue>?, verticalOut verticalJustificationOut: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus
```

```c
extern OSStatus CMTextFormatDescriptionGetJustification(CMFormatDescriptionRef desc, CMTextJustificationValue *horizontaJustificationlOut, CMTextJustificationValue *verticalJustificationOut);
```

#### Return Value

A result code. Returns `noErr` if successful.

#### Discussion

For possible values see [`CMTextJustificationValue`](./cmtextjustificationvalue.md).

## Parameters

- `desc`: `CMFormatDescription` being interrogated.
- `horizontaJustificationlOut`: Horizontal justification mode. May be `NULL`.
- `verticalJustificationOut`: Vertical justification mode. May be `NULL`.

## See Also

### Working with Text Descriptions
- [struct CMTextDescriptionFlavor](./cmtextdescriptionflavor.md)
  Types that represent text format descriptions.
- [func CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription, localFontIDOut: UnsafeMutablePointer<UInt16>?, boldOut: UnsafeMutablePointer<DarwinBoolean>?, italicOut: UnsafeMutablePointer<DarwinBoolean>?, underlineOut: UnsafeMutablePointer<DarwinBoolean>?, fontSizeOut: UnsafeMutablePointer<CGFloat>?, colorComponentsOut: UnsafeMutablePointer<CGFloat>?) -> OSStatus](./cmtextformatdescriptiongetdefaultstyle%28_,localfontidout,boldout,italicout,underlineout,fontsizeout,colorcomponentsout%29.md)
  Returns the default text style.
- [func CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescription, originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat, defaultTextBoxOut: UnsafeMutablePointer<CGRect>) -> OSStatus](./cmtextformatdescriptiongetdefaulttextbox%28_,originisattopleft,heightoftexttrack,defaulttextboxout%29.md)
  Returns the default text box.
- [func CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription, displayFlagsOut: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus](./cmtextformatdescriptiongetdisplayflags%28_,displayflagsout%29.md)
  Returns the display flags.
- [func CMTextFormatDescriptionGetFontName(CMFormatDescription, localFontID: UInt16, fontNameOut: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus](./cmtextformatdescriptiongetfontname%28_,localfontid,fontnameout%29.md)
  Returns a font name for a local font identifier.
- [func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, textFormatDescription: CMTextFormatDescription, flavor: CMTextDescriptionFlavor?, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmtextformatdescriptioncopyasbigendiantextdescriptionblockbuffer%28allocator,textformatdescription,flavor,blockbufferout%29.md)
  Copies the contents of a text format description to a buffer in big-endian byte order.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(allocator: CFAllocator?, bigEndianTextDescriptionBlockBuffer: CMBlockBuffer, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](./cmtextformatdescriptioncreatefrombigendiantextdescriptionblockbuffer%28allocator,bigendiantextdescriptionblockbuffer,flavor,mediatype,formatdescriptionout%29.md)
  Creates a text format description from a big-endian text description structure inside a buffer.
- [func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(allocator: CFAllocator?, bigEndianTextDescriptionData: UnsafePointer<UInt8>, size: Int, flavor: CMTextDescriptionFlavor?, mediaType: CMMediaType, formatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](./cmtextformatdescriptioncreatefrombigendiantextdescriptiondata%28allocator,bigendiantextdescriptiondata,size,flavor,mediatype,formatdescriptionout%29.md)
  Creates a text format description from a big-endian text description structure.
- [func CMSwapBigEndianTextDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswapbigendiantextdescriptiontohost%28_,_%29.md)
  Converts a text description structure from big-endian to host-endian, in place.
- [func CMSwapHostEndianTextDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus](./cmswaphostendiantextdescriptiontobig%28_,_%29.md)
  Converts a text description structure from host-endian to big-endian, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtextformatdescriptiongetjustification(_:horizontalout:verticalout:))*