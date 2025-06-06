# fontName(localFontID:)

**Framework**: Core Media  
**Kind**: method

Returns the font name for the local font identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func fontName(localFontID: Int) throws -> String
```

## See Also

- [func defaultStyle() throws -> (localFontID: Int, bold: Bool, italic: Bool, underline: Bool, fontSize: CGFloat, colorComponents: [CGFloat])](cmformatdescription/defaultstyle.md)
  Returns the default text style.
- [func defaultTextBox(originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat) throws -> CGRect](cmformatdescription/defaulttextbox(originisattopleft:heightoftexttrack:).md)
  Returns the default text box.
- [func displayFlags() throws -> CMFormatDescription.Extensions.Value.TextDisplayFlags](cmformatdescription/displayflags.md)
  Returns the display mode flags for the text media.
- [func justification() throws -> (horizontal: CMFormatDescription.Extensions.Value.TextJustification, vertical: CMFormatDescription.Extensions.Value.TextJustification)](cmformatdescription/justification.md)
  Returns the horizontal and vertical justification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/fontname(localfontid:))*