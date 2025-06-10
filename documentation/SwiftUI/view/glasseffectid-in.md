# glassEffectID(_:in:)

**Framework**: SwiftUI  
**Kind**: method

Associates an identity value to Liquid Glass effects defined within this view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func glassEffectID(_ id: (some Hashable & Sendable)?, in namespace: Namespace.ID) -> some View
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Discussion

You use this modifier with the [`glassEffect(_:in:isEnabled:)`](view/glasseffect(_:in:isenabled:).md) view modifier and a [`GlassEffectContainer`](glasseffectcontainer.md) view. When used together, SwiftUI uses the identifier to animate shapes to and from each other during transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glasseffectid(_:in:))*