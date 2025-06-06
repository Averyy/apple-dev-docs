# scaledToFill()

**Framework**: FamilyControls  
**Kind**: method

Scales this view to fill its parent.

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
func scaledToFill() -> some View
```

#### Return Value

A view that scales this view to fill its parent, maintaining this view’s aspect ratio.

#### Discussion

Use `scaledToFill()` to scale this view to fill its parent, while maintaining the view’s aspect ratio as the view scales:

```swift
Circle()
    .fill(Color.pink)
    .scaledToFill()
    .frame(width: 300, height: 150)
    .border(Color(white: 0.75))
```

This method is equivalent to calling `View/aspectRatio(_:contentMode:)` with a `nil` aspectRatio and a content mode of `ContentMode/fill`.

## See Also

- [func scaledToFit() -> some View](familyactivitypicker/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(_:anchor:)-1mz0o.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](familyactivitypicker/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](familyactivitypicker/aspectratio(_:contentmode:)-7zcef.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/scaledtofill())*