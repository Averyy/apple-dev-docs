# borderStyle

**Framework**: PDFKit  
**Kind**: property  
**Role**: Type Property

A dictionary that contains the properties of the annotation’s border.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let borderStyle: PDFAnnotationKey
```

```c
extern PDFAnnotationKey PDFAnnotationKeyBorderStyle;
```

## See Also

### Configuring Annotation Appearance
- [static let appearanceDictionary: PDFAnnotationKey](./appearancedictionary.md)
  A dictionary that contains properties for controlling the annotation’s visual appearance.
- [static let appearanceState: PDFAnnotationKey](./appearancestate.md)
  A string that specifies the appearance stream for the annotation.
- [static let border: PDFAnnotationKey](./border.md)
  An array of integers or border objects that describes the border of the annotation.
- [static let color: PDFAnnotationKey](./color.md)
  An array of floats or a color object that specifies the annotation’s color.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey/borderstyle)*