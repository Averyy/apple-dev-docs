# ViewAttachmentEntity

**Framework**: RealityKit  
**Kind**: class

An entity that has a view attachment.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency class ViewAttachmentEntity
```

## Topics

### Instance Properties
- [var attachment: ViewAttachmentComponent](viewattachmententity/attachment.md)
  The view attachment component for this entity.

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasHierarchy](hashierarchy.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct RealityViewAttachmentBuilderContent](realityviewattachmentbuildercontent.md)
  A view that gathers the attachment content for your current reality view.
- [struct Attachment](attachment.md)
  An attachment content you can use to gather an identifier and view.
- [struct RealityViewAttachments](realityviewattachments.md)
  The attachments that belong to a RealityView.
- [struct ViewAttachmentComponent](viewattachmentcomponent.md)
  A component containing additional information about a view attachment entity provided  via the [`entity(for:)`](realityviewattachments/entity(for:).md) function.
- [struct PresentationComponent](presentationcomponent.md)
  A component that presents a SwiftUI modal presentation from a RealityKit entity.
- [struct TextComponent](textcomponent.md)
  A component that draws 2D text at an entity’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/viewattachmententity)*