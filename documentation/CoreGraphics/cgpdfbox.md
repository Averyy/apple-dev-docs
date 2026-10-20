# CGPDFBox

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Box types for a PDF page.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CGPDFBox
```

```c
enum CGPDFBox : int32_t;
```

## Topics

### Constants
- [CGPDFBox.mediaBox](./cgpdfbox/mediabox.md)
  The page media box—a rectangle, expressed in default user space units, that defines the boundaries of the physical medium on which the page is intended to be displayed or printed
- [CGPDFBox.cropBox](./cgpdfbox/cropbox.md)
  The page crop box—a rectangle, expressed in default user space units, that defines the visible region of default user space. When the page is displayed or printed, its contents are to be clipped to this rectangle.
- [CGPDFBox.bleedBox](./cgpdfbox/bleedbox.md)
  The page bleed box—a rectangle, expressed in default user space units, that defines the region to which the contents of the page should be clipped when output in a production environment.
- [CGPDFBox.trimBox](./cgpdfbox/trimbox.md)
  The page trim box—a rectangle, expressed in default user space units, that defines the intended dimensions of the finished page after trimming.
- [CGPDFBox.artBox](./cgpdfbox/artbox.md)
  The page art box—a rectangle, expressed in default user space units, defining the extent of the page’s meaningful content (including potential white space) as intended by the page’s creator.
### Initializers
- [init?(rawValue: Int32)](./cgpdfbox/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfbox)*