# dim(intensity:)

**Framework**: SwiftUI  
**Kind**: method

An effect that dims the passthrough video a custom amount.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
static func dim(intensity: Double) -> SurroundingsEffect
```

#### Discussion

Use this with the [`preferredSurroundingsEffect(_:)`](view/preferredsurroundingseffect(_:).md) view modifier when you want to darken the passthrough while displaying a particular view. The value will be clamped between 0 and 1. This effect will only be applied while an immersive space is opened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surroundingseffect/dim(intensity:))*