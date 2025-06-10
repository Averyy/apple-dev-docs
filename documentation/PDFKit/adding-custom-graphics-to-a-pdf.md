# Adding Custom Graphics to a PDF

**Framework**: PDFKit

Create and add custom annotation and page graphics to your PDF document.

#### Overview

You can add custom annotation and page graphics to a PDF by overriding the `draw` method for [`PDFAnnotation`](pdfannotation.md) or [`PDFPage`](pdfpage.md). If the graphic applies to the whole page, like a watermark, custom border, or logo, you add it to the page using [`PDFPage`](pdfpage.md). If the graphic is something small, such as circling or highlighting a particular element on the page, or a repeatable custom graphic, such as a heart, club, spade, or diamond, then it should be added using [`PDFAnnotation`](pdfannotation.md). Some graphics, like lines, can work as annotations or page elements.

Drawings are static, unlike interactive annotation types like widgets. To learn more about widgets, see [`Adding Widgets to a PDF Document`](adding-widgets-to-a-pdf-document.md).

![Add a custom watermark annotation to a PDF. ](https://docs-assets.developer.apple.com/published/e70d9ea8cae1183c2c613784170717c7/media-3039566%402x.png)

##### Register a Delegate for the Document

Register a [`PDFDocumentDelegate`](pdfdocumentdelegate.md) to the [`PDFDocument`](pdfdocument.md) loaded in the current [`PDFView`](pdfview.md). This delegate will allow you to specify a method for building PDF annotations or PDF pages. The [`PDFDocument`](pdfdocument.md) is called `document`.

```swift
document.delegate = self
pdfView?.document = document
```

##### Implement a Custom Subclass

Create a custom subclass for your custom graphics, one that will include your drawing. This example shows how to add a custom line graphic to a PDF, either through a PDF annotation or a PDF page.

###### Implement a Custom Annotation Subclass

Create a custom annotation subclass for your line graphic.

```swift
class LineAnnotation: PDFAnnotation {

}
```

Implement the [`class(forAnnotationType:)`](pdfdocumentdelegate/class(forannotationtype:).md) function in the document’s delegate. This method returns the subclass type for [`PDFAnnotation`](pdfannotation.md) for a given annotation subtype string.  In this case you return the `LineAnnotation` class for a `Line` type annotation.

```swift
func `class`(forAnnotationType annotationType: String) -> AnyClass {
    if annotationType == "Line" {
        return LineAnnotation.self
    } else {
        return PDFAnnotation.self
    }
}
```

###### Implement a Custom Page Subclass

Create a custom subclass for [`PDFPage`](pdfpage.md) that includes your line graphic.

```swift
class LinePage: PDFPage {

}
```

Implement the [`classForPage()`](pdfdocumentdelegate/classforpage().md) function in the document delegate. This class returns the subclass type for [`PDFPage`](pdfpage.md), the `LinePage` class:

```swift
func classForPage() -> AnyClass {
    return LinePage.self
}
```

##### Override the Draw Method and Add Your Custom Graphic

Override the `draw` method in your subclass to draw your custom graphic, the line. Draw the original content by calling the superclass version of the `draw` method. The `draw` methods for pages and annotations are nearly identical, the only difference being the `in context` parameter for annotations and the `to context` parameter for pages:

 [`draw(with:)`](pdfannotation/draw(with:).md) 

```swift
override func draw(with box: PDFDisplayBox, in context: CGContext) {
    // Draw original content.
    super.draw(with: box, in: context)
}
```

 [`draw(with:)`](pdfpage/draw(with:).md) 

```swift
override func draw(with box: PDFDisplayBox, to context: CGContext) {
    // Draw original content.
    super.draw(with: box, to: context)
}
```

In the appropriate `draw` method, add your custom drawing, in this case the line. To ensure that your drawing maintains its [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) properties and doesn’t affect other contexts in your PDF, make sure to save and restore your graphics state (before and after, respectively) you add your custom drawing code.

> ❗ **Important**:  Ensure that you draw your content with respect to the PDF page coordinate system. The origin is at the bottom left corner, with the Y axis increasing from bottom to top and the X axis increasing from left to right.

```swift
class LineAnnotation: PDFAnnotation {
    override func draw(with box: PDFDisplayBox, in context: CGContext) {
        // Draw original content under the new content.
        super.draw(with: box, in: context)
        
        // Draw a custom purple line.
        UIGraphicsPushContext(context)
        context.saveGState()
        
        let path = UIBezierPath()
        path.lineWidth = 10
        path.move(to: CGPoint(x: bounds.minX + startPoint.x, y: bounds.minY + startPoint.y))
        path.addLine(to: CGPoint(x: bounds.minX + endPoint.x, y: bounds.minY + endPoint.y))
        UIColor.systemPurple.setStroke()
        path.stroke()

        context.restoreGState()
        UIGraphicsPopContext()
    }
}
```

> **Note**:  PDFAnnotation also allows custom drawing for annotations with a type unknown to PDFKit,  but only if the annotation has an appearance stream ([`hasAppearanceStream`](pdfannotation/hasappearancestream.md)).

## See Also

- [Adding Widgets to a PDF Document](adding-widgets-to-a-pdf-document.md)
  Add text, button, and choice widgets to a PDF document.
- [Custom Graphics](custom-graphics.md)
  Demonstrates adding a watermark to a PDF page.
- [PDF Widgets](pdf-widgets.md)
  Demonstrates adding widgets—interactive form elements—to a PDF document.
- [class PDFAnnotation](pdfannotation.md)
  An annotation in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/adding-custom-graphics-to-a-pdf)*