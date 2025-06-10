# glassEffectUnion(id:namespace:)

**Framework**: SwiftUI  
**Kind**: method

Associates any Liquid Glass effects defined within this view to a union with the provided identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Discussion

You may want the geometries of multiple views to contribute to a single Liquid Glass effect shape. In these cases, you can use a [`glassEffectUnion(id:namespace:)`](view/glasseffectunion(id:namespace:).md) to specify that a view should contribute to a union of Liquid Glass effects with a particular identifier. All Liquid Glass effects with the same shape and Liquid Glass variant will be combined into a single shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glasseffectunion(id:namespace:))*