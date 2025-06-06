# RealityViewAttachments

**Framework**: RealityKit  
**Kind**: struct

The attachments that belong to a RealityView.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct RealityViewAttachments
```

#### Overview

Use this type to access entities associated with the attachments you provide to your [`RealityView`](realityview.md) via the [`init(make:update:attachments:)`](realityview/init(make:update:attachments:).md) initializer.

## Topics

### Instance Methods
- [func entity(for: some Hashable) -> ViewAttachmentEntity?](realityviewattachments/entity(for:).md)
  Gets the identified attachment view as an entity, if the view with that identifier exists.

## See Also

- [struct RealityViewAttachmentBuilderContent](realityviewattachmentbuildercontent.md)
  A view that gathers the attachment content for your current reality view.
- [struct Attachment](attachment.md)
  An attachment content you can use to gather an identifier and view.
- [class ViewAttachmentEntity](viewattachmententity.md)
  An entity that has a view attachment.
- [struct ViewAttachmentComponent](viewattachmentcomponent.md)
  A component containing additional information about a view attachment entity provided  via the [`entity(for:)`](realityviewattachments/entity(for:).md) function.
- [struct TextComponent](textcomponent.md)
  A component that draws 2D text at an entity’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewattachments)*