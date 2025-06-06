# scaleEffect(x:y:anchor:)

**Framework**: FamilyControls  
**Kind**: method

Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, anchor: UnitPoint = .center) -> some View
```

#### Discussion

Use `scaleEffect(x:y:anchor:)` to apply a scaling transform to a view by a specific horizontal and vertical amount.

```swift
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(x: 0.5, y: 0.5, anchor: .bottomTrailing)
    .border(Color.gray)
```

## Parameters

- `x`: An amount that represents the horizontal amount to scale the   view. The default value is  .
- `y`: An amount that represents the vertical amount to scale the view.   The default value is  .
- `anchor`: The anchor point that indicates the starting position for   the scale operation.

## See Also

- [func scaledToFill() -> some View](familyactivitypicker/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](familyactivitypicker/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(_:anchor:)-1mz0o.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](familyactivitypicker/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](familyactivitypicker/aspectratio(_:contentmode:)-7zcef.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/scaleeffect(x:y:anchor:))*