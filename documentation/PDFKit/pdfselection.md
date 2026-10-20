# PDFSelection

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFSelection
```

```objc
@interface PDFSelection : NSObject
```

## Topics

### Initializing a Selection
- [init(document: PDFDocument)](./pdfselection/init%28document%29.md)
  Returns an empty `PDFSelection` object.
### Getting Information About a Selection
- [var pages: [PDFPage]](./pdfselection/pages.md)
  Returns the array of pages contained in the selection.
- [var string: String?](./pdfselection/string.md)
  Returns an `NSString` object representing the text contained in the selection (may contain linefeed characters).
- [var attributedString: NSAttributedString?](./pdfselection/attributedstring.md)
  Returns an `NSAttributedString` object representing the text contained in the selection (may contain linefeed characters).
- [func bounds(for: PDFPage) -> CGRect](./pdfselection/bounds%28for%29.md)
  Returns the bounds of the selection on the specified page.
- [func selectionsByLine() -> [PDFSelection]](./pdfselection/selectionsbyline%28%29.md)
  Returns an array of selections, one for each line of text covered by the receiver.
- [var color: UIColor?](./pdfselection/color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.
### Modifying a Selection
- [func add(PDFSelection)](./pdfselection/add%28_%29-8c2r.md)
  Adds the specified selection to the receiving selection.
- [func add([PDFSelection])](./pdfselection/add%28_%29-3fyld.md)
  Adds the specified array of selections to the receiving selection.
- [func extend(atEnd: Int)](./pdfselection/extend%28atend%29.md)
  Extends the selection from its end toward the end of the document.
- [func extend(atStart: Int)](./pdfselection/extend%28atstart%29.md)
  Extends the selection from its start toward the beginning of the document.
### Managing Selection Drawing
- [func draw(for: PDFPage, active: Bool)](./pdfselection/draw%28for,active%29.md)
  Calls [`draw(for:with:active:)`](./pdfselection/draw%28for,with,active%29.md) with a default value for box parameter.
- [func draw(for: PDFPage, with: PDFDisplayBox, active: Bool)](./pdfselection/draw%28for,with,active%29.md)
  Draws the selection relative to the origin of the specified box in page space.
- [var color: UIColor?](./pdfselection/color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.
### Instance Methods
- [func extendForLineBoundaries()](./pdfselection/extendforlineboundaries%28%29.md)
- [func numberOfTextRanges(on: PDFPage) -> Int](./pdfselection/numberoftextranges%28on%29.md)
- [func range(at: Int, on: PDFPage) -> NSRange](./pdfselection/range%28at,on%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Content Model
- [class PDFDocument](./pdfdocument.md)
  An object that represents PDF data or a PDF file and defines methods for writing, searching, and selecting PDF data.
- [class PDFPage](./pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
- [class PDFOutline](./pdfoutline.md)
  A `PDFOutline` object is an element in a tree-structured hierarchy that can represent the structure of a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection)*