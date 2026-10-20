# PaperMarkup

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

The data model object for storing markup data created from a `PaperViewController`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct PaperMarkup
```

## Mentions

- [Integrating PaperKit into your app](./getting-started-with-paperkit.md)

## Topics

### Creating markup
- [init(bounds: CGRect)](./papermarkup/init%28bounds%29.md)
  Initializes and returns a new paper model with the specified bounds.
- [init(dataRepresentation: Data) throws](./papermarkup/init%28datarepresentation%29.md)
  Initializes and returns a new paper model from the specified data.
### Serializing markup
- [func dataRepresentation() async throws -> Data](./papermarkup/datarepresentation%28%29.md)
  Generate a serialized data representation of the data model.
### Accessing elements
- [var subelements: MarkupOrderedSet](./papermarkup/subelements.md)
  The subelements of the paper markup.
- [var id: MarkupID<PaperMarkup>](./papermarkup/id.md)
  The unique identifier of the markup.
- [var bounds: CGRect](./papermarkup/bounds.md)
  The bounds of the paper.
- [var contentsRenderFrame: CGRect](./papermarkup/contentsrenderframe.md)
  The frame that tightly fits the rendered contents on the paper.
- [var featureSet: FeatureSet](./papermarkup/featureset.md)
  The set of features used by this data model.
- [var indexableContent: String?](./papermarkup/indexablecontent.md)
- [var backgroundColor: CGColor?](./papermarkup/backgroundcolor.md)
  The background color of the paper.
### Rendering markup
- [func draw(in: CGContext, frame: CGRect, options: RenderingOptions) async](./papermarkup/draw%28in,frame,options%29.md)
  Draws the entire paper contents in the specified rectangle.
### Appending content
- [func append(contentsOf: PaperMarkup)](./papermarkup/append%28contentsof%29-5668.md)
  Adds the contents of a data model on top of this paper.
- [func append(contentsOf: PKDrawing)](./papermarkup/append%28contentsof%29-5tgti.md)
  Adds the contents of a PencilKit drawing on top of this paper.
### Transforming content
- [func transformContent(CGAffineTransform)](./papermarkup/transformcontent%28_%29.md)
  Transforms the contents of this paper with the specified transform.
### Inserting elements
- [func insertNewShape(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat)](./papermarkup/insertnewshape%28configuration,frame,rotation%29.md)
  Add a new element on top of the paper.
- [func insertNewImage(CGImage, frame: CGRect, rotation: CGFloat)](./papermarkup/insertnewimage%28_,frame,rotation%29.md)
  Add a new image on top of the paper.
- [func insertNewLine(configuration: ShapeConfiguration, from: CGPoint, to: CGPoint, startMarker: Bool, endMarker: Bool)](./papermarkup/insertnewline%28configuration,from,to,startmarker,endmarker%29.md)
  Add a line element on top of the paper.
- [func insertNewTextbox(attributedText: AttributedString, frame: CGRect, rotation: CGFloat)](./papermarkup/insertnewtextbox%28attributedtext,frame,rotation%29-53rs.md)
  Add a new text box on top of the paper.
- [func insertNewTextbox(attributedText: NSAttributedString, frame: CGRect, rotation: CGFloat)](./papermarkup/insertnewtextbox%28attributedtext,frame,rotation%29-67igk.md)
  Add a new text box on top of the paper.
### Removing content
- [func removeContentUnsupported(by: FeatureSet)](./papermarkup/removecontentunsupported%28by%29.md)
  Remove all contents that is not supported by the provided feature set.
### Default Implementations
- [Identifiable Implementations](./papermarkup/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data model
- [struct MarkupOrderedSet](./markuporderedset.md)
  An ordered set of markup elements.
- [struct MarkupID](./markupid.md)
  An opaque ID for markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup)*