# PDFPage

**Framework**: PDFKit  
**Kind**: class

`PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFPage
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)

#### Overview

`PDFPage` objects are flexible and powerful. With them you can render PDF content onscreen or to a printer, add annotations, count characters, define selections, and get the textual content of a page as an `NSString` object.

Your application instantiates a `PDFPage` object by asking for one from a `PDFDocument` object.

For simple display and navigation of PDF documents within your application, you don’t need to use `PDFPage`. You need only use `PDFView`.

## Topics

### Initializing a Page
- [convenience init?(image: UIImage)](pdfpage/init(image:).md)
  Creates a new `PDFPage` object and initializes it with the specified `NSImage` object.
### Getting Information About a Page
- [var document: PDFDocument?](pdfpage/document.md)
  Returns the `PDFDocument` object with which the page is associated.
- [var label: String?](pdfpage/label.md)
  Returns the label for the page.
- [func bounds(for: PDFDisplayBox) -> CGRect](pdfpage/bounds(for:).md)
  Returns the bounds for the specified PDF display box.
- [func setBounds(CGRect, for: PDFDisplayBox)](pdfpage/setbounds(_:for:).md)
  Sets the bounds for the specified box.
- [var rotation: Int](pdfpage/rotation.md)
  Sets the rotation angle for the page in degrees.
### Working with Annotations
- [var annotations: [PDFAnnotation]](pdfpage/annotations.md)
  Returns an array containing the page’s annotations.
- [var displaysAnnotations: Bool](pdfpage/displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
- [func addAnnotation(PDFAnnotation)](pdfpage/addannotation(_:).md)
  Adds the specified annotation object to the page.
- [func removeAnnotation(PDFAnnotation)](pdfpage/removeannotation(_:).md)
  Removes the specified annotation from the page.
- [func annotation(at: CGPoint) -> PDFAnnotation?](pdfpage/annotation(at:).md)
  Returns the annotation, if there is one, at the specified point.
### Rendering Pages
- [func draw(with: PDFDisplayBox)](pdfpage/draw(with:).md)
  Draws the page within the specified box.
- [func transformContext(for: PDFDisplayBox)](pdfpage/transformcontext(for:).md)
  Transforms the current context, given the specified box.
### Working with Textual Content
- [var numberOfCharacters: Int](pdfpage/numberofcharacters.md)
  Returns the number of characters on the page, including whitespace characters.
- [var string: String?](pdfpage/string.md)
  Returns an `NSString` object representing the text on the page.
- [var attributedString: NSAttributedString?](pdfpage/attributedstring.md)
  Returns an `NSAttributedString` object representing the text on the page.
- [func characterBounds(at: Int) -> CGRect](pdfpage/characterbounds(at:).md)
  Returns the bounds, in page space, of the character at the specified index.
- [func characterIndex(at: CGPoint) -> Int](pdfpage/characterindex(at:).md)
  Returns the character index value for the specified point in page space.
### Working with Selections
- [func selection(for: CGRect) -> PDFSelection?](pdfpage/selection(for:)-2ckpi.md)
  Returns the text enclosed within the specified rectangle, expressed in page (user) coordinates.
- [func selectionForWord(at: CGPoint) -> PDFSelection?](pdfpage/selectionforword(at:).md)
  Returns the whole word that includes the specified point.
- [func selectionForLine(at: CGPoint) -> PDFSelection?](pdfpage/selectionforline(at:).md)
  Returns the whole line of text that includes the specified point.
- [func selection(from: CGPoint, to: CGPoint) -> PDFSelection?](pdfpage/selection(from:to:).md)
  Returns the text between the two specified points in page space.
- [func selection(for: NSRange) -> PDFSelection?](pdfpage/selection(for:)-20y9d.md)
  Returns the text contained within the specified range.
### Supporting Types
- [enum PDFDisplayBox](pdfdisplaybox.md)
  The following box types may be used with `PDFPage` drawing and bounds-setting methods. See the Adobe PDF Specification for more information on box types, units, and coordinate systems.
- [enum PDFDisplayDirection](pdfdisplaydirection.md)
### Type Aliases
- [PDFPage.ImageInitializationOption](pdfpage/imageinitializationoption.md)
### Initializers
- [init()](pdfpage/init.md)
- [init?(image: UIImage, options: [PDFPage.ImageInitializationOption : Any])](pdfpage/init(image:options:).md)
### Instance Properties
- [var dataRepresentation: Data?](pdfpage/datarepresentation.md)
  Returns the PDF data (that is, a PDF document) representing this page. This method does not preserve external page links.
- [var pageRef: CGPDFPage?](pdfpage/pageref.md)
### Instance Methods
- [func draw(with: PDFDisplayBox, to: CGContext)](pdfpage/draw(with:to:).md)
- [func thumbnail(of: CGSize, for: PDFDisplayBox) -> UIImage](pdfpage/thumbnail(of:for:).md)
- [func transform(CGContext, for: PDFDisplayBox)](pdfpage/transform(_:for:).md)
- [func transform(for: PDFDisplayBox) -> CGAffineTransform](pdfpage/transform(for:).md)
- [func selection(forTableRect: CGRect) -> PDFSelection?](pdfpage/selection(fortablerect:).md)
- [func tableSelection(from: CGPoint, to: CGPoint) -> PDFSelection?](pdfpage/tableselection(from:to:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PDFDocument](pdfdocument.md)
  An object that represents PDF data or a PDF file and defines methods for writing, searching, and selecting PDF data.
- [class PDFOutline](pdfoutline.md)
  A `PDFOutline` object is an element in a tree-structured hierarchy that can represent the structure of a PDF document.
- [class PDFSelection](pdfselection.md)
  A `PDFSelection` object identifies a contiguous or noncontiguous selection of text in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage)*