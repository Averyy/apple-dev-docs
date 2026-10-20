# Attachment

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An attachment content you can use to gather an identifier and view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Attachment<Content> where Content : View
```

## Topics

### Initializers
- [init(id: AnyHashable, () -> Content)](./attachment/init%28id,_%29.md)
  Creates an new attachment from an identifier and a closure.
### Instance Properties
- [var content: Content](./attachment/content.md)
  The view associated with this attachment.
- [var id: AnyHashable](./attachment/id.md)
  The identifier of this attachment.

## Relationships

### Conforms To
- [AttachmentContent](./attachmentcontent.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### SwiftUI view attachments
- [struct RealityViewAttachmentBuilderContent](./realityviewattachmentbuildercontent.md)
  A view that gathers the attachment content for your current reality view.
- [struct RealityViewAttachments](./realityviewattachments.md)
  The attachments that belong to a RealityView.
- [class ViewAttachmentEntity](./viewattachmententity.md)
  An entity that has a view attachment.
- [struct ViewAttachmentComponent](./viewattachmentcomponent.md)
  A component containing additional information about a view attachment entity provided  via the [`entity(for:)`](./realityviewattachments/entity%28for%29.md) function.
- [struct PresentationComponent](./presentationcomponent.md)
  A component that presents a SwiftUI modal presentation from a RealityKit entity.
- [struct TextComponent](./textcomponent.md)
  A component that draws 2D text at an entity’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachment)*