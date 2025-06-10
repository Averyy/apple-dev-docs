# glassEffect(_:in:isEnabled:)

**Framework**: App Intents  
**Kind**: method

Applies a glass effect to this view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func glassEffect(_ glass: Glass = .regular, in shape: some Shape = .capsule, isEnabled: Bool = true) -> some View
```

#### Discussion

When you use a glass effect, the platform:

- Renders a shape anchored behind this view filled with the physical glass material
- Applies the foreground effects of the glass over this view.

For example, you could add a glass effect to a `Label`:

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .glassEffect()
```

SwiftUI uses the `Glass/regular` variant by default along with a `Capsule` shape.

SwiftUI anchors the glass to the view’s bounds. For the example above, the physical glass material fills the entirety of the label’s frame, which includes the padding.

You typically use this modifier with a `GlassEffectContainer` to combine multiple glass shapes into a single shape that can morph shapes into one another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/glasseffect(_:in:isenabled:))*