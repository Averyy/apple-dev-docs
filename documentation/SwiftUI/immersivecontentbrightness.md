# ImmersiveContentBrightness

**Framework**: SwiftUI  
**Kind**: struct

The content brightness of an immersive space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ImmersiveContentBrightness
```

#### Overview

Use a value of this type as an input to the [`immersiveContentBrightness(_:)`](scene/immersivecontentbrightness(_:).md) scene modifier to indicate the ambient content brightness of an [`ImmersiveSpace`](immersivespace.md).

When you do this to create an environment that’s suitable for video playback, use one of the standard brightness values like [`bright`](immersivecontentbrightness/bright.md), [`dim`](immersivecontentbrightness/dim.md), or [`dark`](immersivecontentbrightness/dark.md) to provide good results for most use cases. To optimize further, you can create a custom brightness using a normalized value that expresses the linear brightness ratio between a standard dynamic range white video frame and the background that surrounds the player window.

## Topics

### Type Properties
- [static let automatic: ImmersiveContentBrightness](immersivecontentbrightness/automatic.md)
  The default content brightness.
- [static let bright: ImmersiveContentBrightness](immersivecontentbrightness/bright.md)
  A bright content brightness.
- [static let dark: ImmersiveContentBrightness](immersivecontentbrightness/dark.md)
  A dark content brightness.
- [static let dim: ImmersiveContentBrightness](immersivecontentbrightness/dim.md)
  A dimmed content brightness.
### Type Methods
- [static func custom(Double) -> ImmersiveContentBrightness](immersivecontentbrightness/custom(_:).md)
  Creates a content brightness with a custom value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func immersiveContentBrightness(ImmersiveContentBrightness) -> some Scene](scene/immersivecontentbrightness(_:).md)
  Sets the content brightness of an immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivecontentbrightness)*