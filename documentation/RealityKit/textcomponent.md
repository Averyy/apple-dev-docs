# TextComponent

**Framework**: RealityKit  
**Kind**: struct

A component that draws 2D text at an entity’s location.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct TextComponent
```

#### Overview

`TextComponent` renders two-dimensional text in a RealityKit scene. It creates a rounded rectangle mesh to serve as a canvas and draws an attributed string on the mesh. This component handles everything required to render the text, including updating the plane transform, setting material parameters, and creating mesh components.

Set the component’s [`size`](textcomponent/size.md) to define the area of the canvas in points. This setting also affects the size at which RealityKit renders the text. The world-size of the canvas may be different than the value you specify because the component’s entity inherits its parent’s transform, which may include scale changes that affect the final rendered size.

Text components use the CoreGraphics coordinate space: The origin is at the upper left of the canvas and positive values extend down and to the right. You can’t specify an explicit backing-buffer size. RealityKit dynamically adjusts the backing size to a value that results in high-fidelity text at its current location.

RealityKit lays out text using default `Foundation/AttributedString` behaviors and wraps text instead of truncating it. It keeps the text a constant font size: It doesn’t stretch or scale the text to fit tha canvas. Use Core Text to determine the required canvas size for a particular string or layout.

## Topics

### Initializers
- [init()](textcomponent/init.md)
  Creates a new text component.
### Instance Properties
- [var backgroundColor: CGColor?](textcomponent/backgroundcolor.md)
  The canvas’s background color.
- [var cornerRadius: Float](textcomponent/cornerradius.md)
  The corner radius of the text mesh.
- [var edgeInsets: TextComponent.EdgeInsets](textcomponent/edgeinsets-3n3rn.md)
- [var edgeInsets: TextComponent.EdgeInsets](textcomponent/edgeinsets-49dib.md)
- [var size: CGSize](textcomponent/size.md)
  The size of the canvas in points.
- [var text: AttributedString?](textcomponent/text.md)
  The attributed string this component renders.
### Type Aliases
- [TextComponent.EdgeInsets](textcomponent/edgeinsets-swift.typealias.md)
### Default Implementations
- [Component Implementations](textcomponent/component-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct RealityViewAttachmentBuilderContent](realityviewattachmentbuildercontent.md)
  A view that gathers the attachment content for your current reality view.
- [struct Attachment](attachment.md)
  An attachment content you can use to gather an identifier and view.
- [struct RealityViewAttachments](realityviewattachments.md)
  The attachments that belong to a RealityView.
- [class ViewAttachmentEntity](viewattachmententity.md)
  An entity that has a view attachment.
- [struct ViewAttachmentComponent](viewattachmentcomponent.md)
  A component containing additional information about a view attachment entity provided  via the [`entity(for:)`](realityviewattachments/entity(for:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textcomponent)*