# persistentSystemOverlays(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred visibility of the non-transient system views overlaying the app.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func persistentSystemOverlays(_ visibility: Visibility) -> some CompositorContent
```

#### Discussion

Use this modifier to influence the appearance of system overlays in your app. The behavior varies by platform. For an [`ImmersiveSpace`](immersivespace.md), it affects the Home indicator.

> **Note**: You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

Affected non-transient system views can include, but are not limited to:

- The Home indicator.
- The SharePlay indicator.
- The Multitasking Controls button and Picture in Picture on iPad.

## Parameters

- `visibility`: A value that indicates the visibility of the   non-transient system views overlaying the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/persistentsystemoverlays(_:))*