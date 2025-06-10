# ornament(attachmentAnchor:contentAlignment:ornament:effect:)

**Framework**: SwiftUI  
**Kind**: method

Presents an ornament on hover.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
static func ornament<Content, EffectContent>(attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D = .center, @ViewBuilder ornament: () -> Content, effect: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> EffectContent) -> OrnamentHoverContentEffect<Content, EffectContent> where Self == OrnamentHoverContentEffect<Content, EffectContent>, Content : View, EffectContent : HoverEffectContent
```

#### Discussion

Use this method to present an ornament at the specified position when the view is hovered. The ornament will be presented using the provided `effect`.

## Parameters

- `attachmentAnchor`: The positioning anchor that defines the   attachment point of the ornament.
- `contentAlignment`: The alignment of the ornament with its attachment anchor.
- `ornament`: The content of the ornament.
- `effect`: The effect used to present the ornament.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:effect:))*