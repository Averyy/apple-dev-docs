# color

**Framework**: PDFKit  
**Kind**: property  
**Role**: Type Property

An array of floats or a color object that specifies the annotation’s color.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let color: PDFAnnotationKey
```

```c
extern PDFAnnotationKey PDFAnnotationKeyColor;
```

#### Discussion

Annotations use the color for the following:

- The background of the annotation’s icon when it’s in a closed state
- The title bar of the annotation’s pop-up window
- The border of a link annotation
- The stroke of a circle, square, or line shape annotation

## See Also

### Configuring Annotation Appearance
- [static let appearanceDictionary: PDFAnnotationKey](./appearancedictionary.md)
  A dictionary that contains properties for controlling the annotation’s visual appearance.
- [static let appearanceState: PDFAnnotationKey](./appearancestate.md)
  A string that specifies the appearance stream for the annotation.
- [static let border: PDFAnnotationKey](./border.md)
  An array of integers or border objects that describes the border of the annotation.
- [static let borderStyle: PDFAnnotationKey](./borderstyle.md)
  A dictionary that contains the properties of the annotation’s border.
- [static let defaultAppearance: PDFAnnotationKey](./defaultappearance.md)
  A string value a free text annotation uses to format the text.
- [static let highlightingMode: PDFAnnotationKey](./highlightingmode.md)
  A string value that defines the way an annotation highlights when the user activates it, such as when clicking or tapping a link.
- [struct PDFAnnotationHighlightingMode](../pdfannotationhighlightingmode.md)
- [static let iconName: PDFAnnotationKey](./iconname.md)
  A string value that specifies the name of an icon for a text or stamp annotation.
- [static let interiorColor: PDFAnnotationKey](./interiorcolor.md)
  An array of floating point values or a PDF color object that annotations use to fill interior space, such as line endings, squares, or circles.
- [static let quadding: PDFAnnotationKey](./quadding.md)
  An integer value that specifies left, right, or center justification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey/color)*