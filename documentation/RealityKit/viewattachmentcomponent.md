# ViewAttachmentComponent

**Framework**: RealityKit  
**Kind**: struct

A component containing additional information about a view attachment entity provided  via the [`entity(for:)`](realityviewattachments/entity(for:).md) function.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ViewAttachmentComponent
```

## Topics

### Initializers
- [init<Content>(rootView: Content)](viewattachmentcomponent/init(rootview:).md)
  A RealityKit component that manages a SwiftUI view hierarchy.
### Instance Properties
- [var bounds: BoundingBox](viewattachmentcomponent/bounds.md)
  The bounding box of the view attachment, expressed in meters.
- [var id: AnyHashable](viewattachmentcomponent/id.md)
  The identifier used for this view attachment.

## Relationships

### Conforms To
- [Component](component.md)
- [Identifiable](../Swift/Identifiable.md)
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
- [struct PresentationComponent](presentationcomponent.md)
  A component that presents a SwiftUI modal presentation from a RealityKit entity.
- [struct TextComponent](textcomponent.md)
  A component that draws 2D text at an entity’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/viewattachmentcomponent)*