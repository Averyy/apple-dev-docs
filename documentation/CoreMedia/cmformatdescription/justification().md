# justification()

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns the horizontal and vertical justification.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func justification() throws -> (horizontal: CMFormatDescription.Extensions.Value.TextJustification, vertical: CMFormatDescription.Extensions.Value.TextJustification)
```

## See Also

### Working with Text Descriptions
- [func defaultStyle() throws -> (localFontID: Int, bold: Bool, italic: Bool, underline: Bool, fontSize: CGFloat, colorComponents: [CGFloat])](./defaultstyle%28%29.md)
  Returns the default text style.
- [func defaultTextBox(originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat) throws -> CGRect](./defaulttextbox%28originisattopleft,heightoftexttrack%29.md)
  Returns the default text box.
- [func displayFlags() throws -> CMFormatDescription.Extensions.Value.TextDisplayFlags](./displayflags%28%29.md)
  Returns the display mode flags for the text media.
- [func fontName(localFontID: Int) throws -> String](./fontname%28localfontid%29.md)
  Returns the font name for the local font identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/justification())*