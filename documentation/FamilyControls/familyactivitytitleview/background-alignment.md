# background(_:alignment:)

**Framework**: FamilyControls  
**Kind**: method

Layers the given view behind this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func background<Background>(_ background: Background, alignment: Alignment = .center) -> some View where Background : View
```

#### Discussion

Use `background(_:alignment:)` when you need to place one view behind another, with the background view optionally aligned with a specified edge of the frontmost view.

The example below creates two views: the `Frontmost` view, and the `DiamondBackground` view. The `Frontmost` view uses the `DiamondBackground` view for the background of the image element inside the `Frontmost` view’s `VStack`.

```swift
struct DiamondBackground: View {
    var body: some View {
        VStack {
            Rectangle()
                .fill(.gray)
                .frame(width: 250, height: 250, alignment: .center)
                .rotationEffect(.degrees(45.0))
        }
    }
}

struct Frontmost: View {
    var body: some View {
        VStack {
            Image(systemName: "folder")
                .font(.system(size: 128, weight: .ultraLight))
                .background(DiamondBackground())
        }
    }
}
```

## Parameters

- `background`: The view to draw behind this view.
- `alignment`: The alignment with a default value of    that you use to position the background view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/background(_:alignment:))*