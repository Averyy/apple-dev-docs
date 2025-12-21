# ornament(attachmentAnchor:contentAlignment:ornament:)

**Framework**: SwiftUI  
**Kind**: method

Presents an ornament on hover.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
static func ornament<Content>(attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D = .center, @ViewBuilder ornament: () -> Content) -> OrnamentHoverEffect<Content> where Self == OrnamentHoverEffect<Content>, Content : View
```

#### Discussion

Use this method to show an ornament at the specified position when the view is hovered. The ornament will be shown with the default fade animation.

## Parameters

- `attachmentAnchor`: The positioning anchor that defines the   attachment point of the ornament.
- `contentAlignment`: The alignment of the ornament with its attachment anchor.
- `ornament`: The content of the ornament.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:))*