# PresentationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that presents a SwiftUI modal presentation from a RealityKit entity.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct PresentationComponent
```

## Topics

### Structures
- [PresentationComponent.Configuration](presentationcomponent/configuration.md)
  A configuration that specifies the modality, appearance, and behavior of the presentation.
### Initializers
- [init<Content>(configuration: PresentationComponent.Configuration, content: Content)](presentationcomponent/init(configuration:content:).md)
  Present `content` using modality and options specified by `configuration`. A component created using this method will have its `isPresented` property default to `true`, which means it will present as soon as an entity with the component is added to the hierarchy.
- [init<Content>(isPresented: Binding<Bool>, configuration: PresentationComponent.Configuration, content: Content)](presentationcomponent/init(ispresented:configuration:content:).md)
  Present `content` when a binding that you provide is `true`, using modality and options specified by `configuration`.
### Instance Properties
- [var isPresented: Bool](presentationcomponent/ispresented.md)
  A boolean value that indicates whether the content is presented.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)

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
- [struct TextComponent](textcomponent.md)
  A component that draws 2D text at an entity’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/presentationcomponent)*