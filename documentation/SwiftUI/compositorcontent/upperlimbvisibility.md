# upperLimbVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](immersivespace.md) scene is presented.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func upperLimbVisibility(_ preferredVisibility: Visibility) -> some CompositorContent
```

#### Discussion

The system can show the user’s upper limbs during fully immersive experiences, but you can also hide them, for example, in order to display virtual hands instead.

Note that this modifier only sets a preference and ultimately the system will decide if it will honor it or not. The system may be unable to honor the preference if the immersive space is currently not visible.

## Parameters

- `preferredVisibility`: A value indicating if the upper limbs should be   visible. Use   for a system-defined standard behavior,    to keep the upper limbs visible, and   to hide   the upper limbs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/upperlimbvisibility(_:))*