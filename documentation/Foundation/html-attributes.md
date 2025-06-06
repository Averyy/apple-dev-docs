# HTML attributes

**Framework**: Foundation

Documentwide attributes that provide control over the form of generated HTML.

#### Overview

You use these attributes only for writing HTML. [`excludedElements`](nsattributedstring/documentattributekey/excludedelements.md) allows control over the tags used. The recognized values in the [`excludedElements`](nsattributedstring/documentattributekey/excludedelements.md) array are (case-insensitive) HTML tags, plus DOCTYPE (representing a doctype declaration) and XML (representing an XML declaration). By default, if this attribute is not present, the excluded elements will be those deprecated in HTML 4 (APPLET, BASEFONT, CENTER, DIR, FONT, ISINDEX, MENU, S, STRIKE, and U) plus XML. If XML is on the list, HTML forms are used; if XML is not on the list, XHTML forms are used where there is a distinction. Either [`characterEncoding`](nsattributedstring/documentattributekey/characterencoding.md) or [`textEncodingName`](nsattributedstring/documentattributekey/textencodingname.md) may be used to control the encoding used for generated HTML; character entities are used for characters not representable in the specified encoding. [`prefixSpaces`](nsattributedstring/documentattributekey/prefixspaces.md) allows some control over formatting.

## Topics

### Getting the attributes
- [static let excludedElements: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/excludedelements.md)
  The HTML elements to exclude in generated HTML.
- [static let textEncodingName: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/textencodingname.md)
  The name of the text encoding to use.
- [static let prefixSpaces: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/prefixspaces.md)
  The number of spaces for indenting nested HTML elements.

## See Also

- [NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey.md)
  The attributes you apply to an entire document.
- [NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [NSAttributedString.DocumentType](nsattributedstring/documenttype.md)
  Constants for the document type document attribute key.
- [NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../UIKit/NSTextScalingType.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/html-attributes)*