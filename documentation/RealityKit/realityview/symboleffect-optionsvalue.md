# symbolEffect(_:options:value:)

**Framework**: RealityKit  
**Kind**: method

Returns a new view with a symbol effect added to it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func symbolEffect<T, U>(_ effect: T, options: SymbolEffectOptions = .default, value: U) -> some View where T : DiscreteSymbolEffect, T : SymbolEffect, U : Equatable
```

#### Return Value

A copy of the view with a symbol effect added.

#### Discussion

The following example adds a bounce effect to two symbol images, the animation will play each time `counter` changes:

```None
VStack {
    Image(systemName: "bolt.slash.fill")
    Image(systemName: "folder.fill.badge.person.crop")
}
.symbolEffect(.bounce, value: counter)
```

## Parameters

- `effect`: A symbol effect to add to the view. Existing effects   added by ancestors of the view are preserved, but may be   overridden by the new effect. Added effects will be applied   to the ``SwiftUI/Image` views contained by the child view.
- `value`: The value to monitor for changes, the animation is   triggered each time the value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/symboleffect(_:options:value:))*