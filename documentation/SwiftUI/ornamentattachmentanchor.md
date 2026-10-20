# OrnamentAttachmentAnchor

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An attachment anchor for an ornament.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct OrnamentAttachmentAnchor
```

## Topics

### Getting an anchor
- [static scene(_:)](./ornamentattachmentanchor/scene%28_%29.md)
  The anchor point for the ornament expressed as a unit point relative to the scene.
### Type Methods
- [static func parent(UnitPoint3D) -> OrnamentAttachmentAnchor](./ornamentattachmentanchor/parent%28_%29.md)
  The anchor point for the ornament expressed as a 3D unit point relative to its parent.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating an ornament
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D, ornament: () -> Content) -> some View](./view/ornament%28visibility,attachmentanchor,contentalignment,ornament%29.md)
  Presents an ornament.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/ornamentattachmentanchor)*