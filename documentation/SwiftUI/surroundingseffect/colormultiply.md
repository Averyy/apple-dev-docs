# colorMultiply(_:)

**Framework**: SwiftUI  
**Kind**: method

An effect that applies a custom tint to the passthrough video by multiplying the passthrough with a [`Color`](color.md).

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static func colorMultiply(_ color: Color) -> SurroundingsEffect
```

#### Discussion

Use this with the [`preferredSurroundingsEffect(_:)`](view/preferredsurroundingseffect(_:).md) view modifier when you want to tint the passthrough while displaying a particular view. The system may decide to limit how much each color in the passthrough can be brightened or darkened. `Color.black` will cause no passthrough to be visible, and `Color.white` will have no effect. `Color(red: 1.15, green: 1.0, blue: 1.0)` would brighten the red in the passthrough by 15 percent. This effect will only be applied while an immersive space is opened.

## Parameters

- `color`: The color to bias the passthrough toward. The opacity of the   color is ignored. Use the extended color space to brighten the   passthrough.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surroundingseffect/colormultiply(_:))*