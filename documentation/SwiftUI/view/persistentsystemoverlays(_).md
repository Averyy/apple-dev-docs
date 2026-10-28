# persistentSystemOverlays(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the preferred visibility of the non-transient system views overlaying the app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func persistentSystemOverlays(_ visibility: Visibility) -> some View
```

## Discussion

Use this modifier to influence the appearance of system overlays in your app. The behavior varies by platform.

In iOS, the following example hides every persistent system overlay. In visionOS 2 and later, the SharePlay Indicator hides if the scene is shared through SharePlay, or not shared at all. During screen sharing, the indicator always remains visible. The Home indicator doesn’t appear without specific user intent when you set visibility to [`Visibility.hidden`](../visibility/hidden.md). For a [`WindowGroup`](../windowgroup.md), the modifier affects the visibility of the window chrome. For an [`ImmersiveSpace`](../immersivespace.md), it affects the Home indicator.

```swift
struct ImmersiveView: View {
    var body: some View {
        Text("Maximum immersion")
            .persistentSystemOverlays(.hidden)
    }
}
```

> **Note**: You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

Affected non-transient system views can include, but are not limited to:

- The Home indicator.
- The SharePlay indicator.
- The Multitasking Controls button and Picture in Picture on iPad.

## Parameters

- `visibility`: A value that indicates the visibility of the non-transient system views overlaying the app.

## See Also

### Hiding system elements
- [func labelsHidden() -> some View](./labelshidden%28%29.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](./labelsvisibility%28_%29.md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](../environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](./labelsvisibility%28_%29.md).
- [func menuIndicator(Visibility) -> some View](./menuindicator%28_%29.md)
  Sets the menu indicator visibility for controls within this view.
- [enum Visibility](../visibility.md)
  The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.
- [func statusBarHidden(Bool) -> some View](./statusbarhidden%28_%29.md)
  Sets the visibility of the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/persistentsystemoverlays(_:))*