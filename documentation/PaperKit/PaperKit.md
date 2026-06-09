# PaperKit

**Framework**: PaperKit  
**Kind**: module

Add drawings, shapes, and a consistent markup experience to your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

#### Overview

PaperKit builds on top of [`PencilKit`](https://developer.apple.com/documentation/PencilKit) to deliver a comprehensive markup experience. It adds a layer of elements — including shapes, images, and text boxes — to help create a unified canvas that supports both drawing and annotation. PaperKit powers the markup experience across all Apple platforms, and provides an easy way to add rich markup capabilities to any app.

PaperKit consists of three main components that work together to deliver a complete markup experience. [`PaperMarkupViewController`](papermarkupviewcontroller.md) serves as the primary markup controller that interactively creates and displays PaperKit elements alongside PencilKit content. [`PaperMarkup`](papermarkup.md) acts as the data model container that handles saving, loading, and rendering both markup elements and PencilKit drawing data. [`MarkupEditViewController`](markupeditviewcontroller.md) (in iOS, iPadOS, and visionOS) and [`MarkupToolbarViewController`](markuptoolbarviewcontroller.md) (in macOS) provide platform-specific insertion menus for adding markup elements.

Configure PaperKit to match your app’s specific needs by providing a [`FeatureSet`](featureset.md) to control which markup tools and capabilities are available. Enable HDR support for stunning visual content, set custom background views, and fine-tune the markup experience to align perfectly with your app’s design and functionality.

## Topics

### Essentials
- [Integrating PaperKit into your app](getting-started-with-paperkit.md)
  Create your first markup experience by setting up a view controller, adding markup editing tools, and implementing data persistence.
### View controllers
- [class PaperMarkupViewController](papermarkupviewcontroller.md)
  A view controller for interactively creating and showing markup.
- [class MarkupEditViewController](markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.
- [class MarkupToolbarViewController](markuptoolbarviewcontroller.md)
### Configuration
- [struct FeatureSet](featureset.md)
  The features PaperKit supports in its UI and data models.
- [struct ShapeConfiguration](shapeconfiguration.md)
  A configuration that specifies the appearance of a shape.
- [struct RenderingOptions](renderingoptions.md)
  The rendering options for drawing paper data models.
- [enum PaperDocumentDisplayMode](paperdocumentdisplaymode.md)
### Data model
- [struct PaperMarkup](papermarkup.md)
  The data model object for storing markup data created from a `PaperViewController`.
- [struct MarkupOrderedSet](markuporderedset.md)
  An ordered set of markup elements.
- [struct MarkupID](markupid.md)
  An opaque ID for markup elements.
### Markup elements
- [protocol Markup](markup.md)
  A markup component.
- [struct ImageMarkup](imagemarkup.md)
  A markup element that represents an image.
- [struct ShapeMarkup](shapemarkup.md)
  A markup element that represents a shape or text box with customizable appearance and behavior.
- [struct LinkMarkup](linkmarkup.md)
  A URL link that a person can tap on in the canvas.
- [struct LoupeMarkup](loupemarkup.md)
  A loupe magnifier that magnifies the content below the loupe.
- [struct MarkupInteractions](markupinteractions.md)
  Interactions that people can perform on markup elements.
### Adornments
- [struct MarkupAdornment](markupadornment.md)
  A visual adornment that appears on top of markup content within a markup view controller.
### Error handling
- [enum MarkupError](markuperror.md)
  The error thrown for encoding / decoding data models.
### Structures
- [struct MarkupAutoresizing](markupautoresizing.md)
  Automatic sizing behaviors for this markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PaperKit)*