# preferredSurroundingsEffect(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies an effect to passthrough video.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some CompositorContent
```

#### Return Value

A CompositorContent that exhibits the specified preference.

#### Discussion

Use this modifier to indicate a preference for the appearance of passthrough video when displaying the modified compositor content. For example, you can enhance the immersiveness of a scene that uses the default [`mixed`](immersionstyle/mixed.md) immersion style by applying the [`systemDark`](surroundingseffect/systemdark.md) preference to a compositor content inside the scene.

This also dims passthrough video, which helps to draw attention to the scene’s virtual content while still enabling people to remain aware of their surroundings.

> **Note**: This modifier expresses a preference, but the system might not be able to honor it.

Use a value of `nil` to indicate that you have no preference. You typically do this to counteract a preference expressed by something lower in the view hierarchy.

## Parameters

- `effect`: The effect that you want to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/preferredsurroundingseffect(_:))*