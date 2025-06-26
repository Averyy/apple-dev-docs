# overlay(_:alignment:)

**Framework**: FamilyControls  
**Kind**: method

Layers a secondary view in front of this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func overlay<Overlay>(_ overlay: Overlay, alignment: Alignment = .center) -> some View where Overlay : View
```

#### Return Value

A view that layers `overlay` in front of the view.

#### Discussion

When you apply an overlay to a view, the original view continues to provide the layout characteristics for the resulting view. In the following example, the heart image is shown overlaid in front of, and aligned to the bottom of the folder image.

```swift
Image(systemName: "folder")
    .font(.system(size: 55, weight: .thin))
    .overlay(Text("❤️"), alignment: .bottom)
```

## Parameters

- `overlay`: The view to layer in front of this view.
- `alignment`: The alignment for   in relation to this view.

## See Also

- [func frame() -> some View](familyactivitypicker/frame.md)
  Positions this view within an invisible frame.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](familyactivitypicker/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func background<Background>(Background, alignment: Alignment) -> some View](familyactivitypicker/background(_:alignment:).md)
  Layers the given view behind this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/overlay(_:alignment:))*