# PaperMarkup

**Framework**: PaperKit  
**Kind**: struct

The data model object for storing markup data created from a `PaperViewController`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct PaperMarkup
```

## Topics

### Operators
- [static func == (PaperMarkup, PaperMarkup) -> Bool](papermarkup/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(bounds: CGRect)](papermarkup/init(bounds:).md)
  Initializes and returns a new paper model with the specified bounds.
- [init(dataRepresentation: Data) throws](papermarkup/init(datarepresentation:).md)
  Initializes and returns a new paper model from the specified data.
### Instance Properties
- [var bounds: CGRect](papermarkup/bounds.md)
  The bounds of the paper.
- [var contentsRenderFrame: CGRect](papermarkup/contentsrenderframe.md)
  The frame that tightly fits the rendered contents on the paper.
- [var drawing: PKDrawing?](papermarkup/drawing.md)
  The PencilKit drawing that is a part of this paper.
- [var featureSet: FeatureSet](papermarkup/featureset.md)
  The set of features used by this data model.
### Instance Methods
- [func append(contentsOf: PaperMarkup)](papermarkup/append(contentsof:).md)
  Adds the contents of a data model on top of this paper.
- [func dataRepresentation() async throws -> Data](papermarkup/datarepresentation.md)
  Generate a serialized data representation of the data model.
- [func draw(in: CGContext, frame: CGRect, options: RenderingOptions) async](papermarkup/draw(in:frame:options:).md)
  Draws the entire paper contents in the specified rectangle.
- [func insertNewImage(CGImage, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewimage(_:frame:rotation:).md)
  Add a new image on top of the paper.
- [func insertNewLine(configuration: ShapeConfiguration, from: CGPoint, to: CGPoint, startMarker: Bool, endMarker: Bool)](papermarkup/insertnewline(configuration:from:to:startmarker:endmarker:).md)
  Add a line element on top of the paper.
- [func insertNewShape(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewshape(configuration:frame:rotation:).md)
  Add a new element on top of the paper.
- [func insertNewTextbox(attributedText: AttributedString, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewtextbox(attributedtext:frame:rotation:)-53rs.md)
  Add a new text box on top of the paper.
- [func insertNewTextbox(attributedText: NSAttributedString, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewtextbox(attributedtext:frame:rotation:)-67igk.md)
  Add a new text box on top of the paper.
- [func removeContentUnsupported(by: FeatureSet)](papermarkup/removecontentunsupported(by:).md)
  Remove all contents that is not supported by the provided feature set.
- [func transformContent(CGAffineTransform)](papermarkup/transformcontent(_:).md)
  Transforms the contents of this paper with the specified transform.
### Default Implementations
- [Equatable Implementations](papermarkup/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup)*