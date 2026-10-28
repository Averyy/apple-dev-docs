# RealityViewAttachmentBuilderContent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A view that gathers the attachment content for your current reality view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct RealityViewAttachmentBuilderContent<Attachment, Content> where Attachment : AttachmentContent, Content : View
```

## Overview

A [`RealityView`](./realityview.md) creates this for you.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### SwiftUI view attachments
- [struct Attachment](./attachment.md)
  An attachment content you can use to gather an identifier and view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewattachmentbuildercontent)*