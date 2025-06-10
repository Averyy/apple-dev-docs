# progressive(aspectRatio:)

**Framework**: SwiftUI  
**Kind**: method

An immersion style that displays unbounded content that partially replaces passthrough video.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func progressive(aspectRatio: ProgressiveImmersionAspectRatio) -> ProgressiveImmersionStyle
```

#### Discussion

Use the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md) scene modifier to specify this style for an [`ImmersiveSpace`](immersivespace.md).

The immersion style affects how windows interact with virtual objects in the environment. In `progressive` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is off.

The system initially uses a portal effect that replaces passthrough in a portion of the field of view. People can interactively adjust the size of the portal by rotating the Digital Crown, including down to a minimum amount of immersion defined by the app and up to the defined maximum amount of immersion.

## Parameters

- `aspectRatio`: The aspect ratio of the portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle/progressive(aspectratio:))*