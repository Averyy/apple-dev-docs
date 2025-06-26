# scaleEffect(_:anchor:)

**Framework**: FamilyControls  
**Kind**: method

Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some View
```

#### Discussion

Use `scaleEffect(_:anchor:)` to scale a view by applying a scaling transform of a specific size, specified by `scale`.

```swift
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(CGSize(x: 0.9, y: 1.3), anchor: .leading)
    .border(Color.gray)
```

## Parameters

- `scale`: A   that   represents the horizontal and vertical amount to scale the view.
- `anchor`: The point with a default of   that   defines the location within the view from which to apply the   transformation.

## See Also

- [func scaledToFill() -> some View](familyactivitypicker/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](familyactivitypicker/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](familyactivitypicker/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](familyactivitypicker/aspectratio(_:contentmode:)-7zcef.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/scaleeffect(_:anchor:)-1mz0o)*