# glassEffectID(_:in:)

**Framework**: FamilyControls  
**Kind**: method

Associates an identity value to glass effects defined within this view.

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

#### Discussion

You use this modifier with the `View/glassEffect(_:in:isEnabled:)` view modifier and `GlassEffectContainer` view. When used together, SwiftUI will use the provided identifier to animate shapes to and from each other during transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/glasseffectid(_:in:))*