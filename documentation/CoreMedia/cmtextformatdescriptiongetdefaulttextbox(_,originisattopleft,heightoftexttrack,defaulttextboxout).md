# CMTextFormatDescriptionGetDefaultTextBox(_:originIsAtTopLeft:heightOfTextTrack:defaultTextBoxOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the default text box.

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
func CMTextFormatDescriptionGetDefaultTextBox(_ desc: CMFormatDescription, originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat, defaultTextBoxOut: UnsafeMutablePointer<CGRect>) -> OSStatus
```

```c
extern OSStatus CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescriptionRef desc, Boolean originIsAtTopLeft, CGFloat heightOfTextTrack, CGRect *defaultTextBoxOut);
```

#### Return Value

A result code. Returns `noErr` if successful.

#### Discussion

Within a text track, text is rendered within a text box.  There is a default text box set, which can be over-ridden by a sample.

## Parameters

- `desc`: FormatDescription being interrogated.
- `originIsAtTopLeft`: Pass true if the `CGRect` will be used in an environment where (0,0) is at the top-left corner of an enclosing rectangle and y coordinates increase as you go down.

  Pass false if the `CGRect` will be used in an environment where (0,0) is at the bottom-left corner of an enclosing rectangle and y coordinates increase as you go up.
- `heightOfTextTrack`: If `originIsAtTopLeft` is false, pass the height of the enclosing text track or destination.                                    This value will be used to properly compute the default text box for the given origin. Ignored if `originIsAtTopLeft` is true.
- `defaultTextBoxOut`: On output, receives the default text box.

## See Also

### Working with Text Descriptions
- [struct CMTextDescriptionFlavor](./cmtextdescriptionflavor.md)
  Types that represent text format descriptions.
- [func CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription, localFontIDOut: UnsafeMutablePointer<UInt16>?, boldOut: UnsafeMutablePointer<DarwinBoolean>?, italicOut: UnsafeMutablePointer<DarwinBoolean>?, underlineOut: UnsafeMutablePointer<DarwinBoolean>?, fontSizeOut: UnsafeMutablePointer<CGFloat>?, colorComponentsOut: UnsafeMutablePointer<CGFloat>?) -> OSStatus](./cmtextformatdescriptiongetdefaultstyle%28_,localfontidout,boldout,italicout,underlineout,fontsizeout,colorcomponentsout%29.md)
  Returns the default text style.
- [func CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription, displayFlagsOut: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus](./cmtextformatdescriptiongetdisplayflags%28_,displayflagsout%29.md)
  Returns the display flags.
- [func CMTextFormatDescriptionGetFontName(CMFormatDescription, localFontID: UInt16, fontNameOut: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus](./cmtextformatdescriptiongetfontname%28_,localfontid,fontnameout%29.md)
  Returns a font name for a local font identifier.
- [func CMTextFormatDescriptionGetJustification(CMFormatDescription, horizontalOut: UnsafeMutablePointer<CMTextJustificationValue>?, verticalOut: UnsafeMutablePointer<CMTextJustificationValue>?) -> OSStatus](./cmtextformatdescriptiongetjustification%28_,horizontalout,verticalout%29.md)
  Returns the horizontal and vertical justification.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtextformatdescriptiongetdefaulttextbox(_:originisattopleft:heightoftexttrack:defaulttextboxout:))*