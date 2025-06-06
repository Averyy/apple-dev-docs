# persistentSystemOverlays(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the preferred visibility of the non-transient system views overlaying the app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func persistentSystemOverlays(_ visibility: Visibility) -> some View
```

#### Discussion

Use this modifier to influence the appearance of system overlays in your app. The behavior varies by platform.

In iOS, the following example hides every persistent system overlay. In visionOS 2 and later, the SharePlay Indicator hides if the scene is shared through SharePlay, or not shared at all. During screen sharing, the indicator always remains visible. The Home indicator doesn’t appear without specific user intent when you set visibility to `hidden`. For a `WindowGroup`, the modifier affects the visibility of the window chrome. For an `ImmersiveSpace`, it affects the Home indicator.

```swift
struct ImmersiveView: View {
    var body: some View {
        Text("Maximum immersion")
            .persistentSystemOverlays(.hidden)
    }
}
```

> **Note**: You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

Affected non-transient system views can include, but are not limited to:

- The Home indicator.
- The SharePlay indicator.
- The Multitasking Controls button and Picture in Picture on iPad.

## Parameters

- `visibility`: A value that indicates the visibility of the   non-transient system views overlaying the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/persistentsystemoverlays(_:))*