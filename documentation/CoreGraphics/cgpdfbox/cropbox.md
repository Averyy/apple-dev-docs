# CGPDFBox.cropBox

**Framework**: Core Graphics  
**Kind**: case

The page crop box—a rectangle, expressed in default user space units, that defines the visible region of default user space. When the page is displayed or printed, its contents are to be clipped to this rectangle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case cropBox
```

## See Also

- [CGPDFBox.mediaBox](cgpdfbox/mediabox.md)
  The page media box—a rectangle, expressed in default user space units, that defines the boundaries of the physical medium on which the page is intended to be displayed or printed
- [CGPDFBox.bleedBox](cgpdfbox/bleedbox.md)
  The page bleed box—a rectangle, expressed in default user space units, that defines the region to which the contents of the page should be clipped when output in a production environment.
- [CGPDFBox.trimBox](cgpdfbox/trimbox.md)
  The page trim box—a rectangle, expressed in default user space units, that defines the intended dimensions of the finished page after trimming.
- [CGPDFBox.artBox](cgpdfbox/artbox.md)
  The page art box—a rectangle, expressed in default user space units, defining the extent of the page’s meaningful content (including potential white space) as intended by the page’s creator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfbox/cropbox)*