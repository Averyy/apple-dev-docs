# imageScale(_:)

**Framework**: FamilyControls  
**Kind**: method

Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 11.0+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func imageScale(_ scale: Image.Scale) -> some View
```

#### Discussion

The example below shows the relative scaling effect. The system renders the image at a relative size based on the available space and configuration options of the image it is scaling.

```swift
VStack {
    HStack {
        Image(systemName: "heart.fill")
            .imageScale(.small)
        Text("Small")
    }
    HStack {
        Image(systemName: "heart.fill")
            .imageScale(.medium)
        Text("Medium")
    }

    HStack {
        Image(systemName: "heart.fill")
            .imageScale(.large)
        Text("Large")
    }
}
```

## Parameters

- `scale`: One of the relative sizes provided by the image scale   enumeration.

## See Also

- [func scaledToFill() -> some View](familyactivitypicker/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](familyactivitypicker/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(_:anchor:)-1mz0o.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](familyactivitypicker/aspectratio(_:contentmode:)-7zcef.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/imagescale(_:))*