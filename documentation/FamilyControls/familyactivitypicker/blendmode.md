# blendMode(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the blend mode for compositing this view with overlapping views.

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
func blendMode(_ blendMode: BlendMode) -> some View
```

#### Return Value

A view that applies `blendMode` to this view.

#### Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual effect to produce the result. The `BlendMode` enumeration defines many possible effects.

In the example below, the two overlapping rectangles have a `BlendMode/colorBurn` effect applied, which effectively removes the non-overlapping portion of the second image:

```swift
HStack {
    Color.yellow.frame(width: 50, height: 50, alignment: .center)

    Color.red.frame(width: 50, height: 50, alignment: .center)
        .rotationEffect(.degrees(45))
        .padding(-20)
        .blendMode(.colorBurn)
}
```

## Parameters

- `blendMode`: The   for compositing this view.

## See Also

- [func compositingGroup() -> some View](familyactivitypicker/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](familyactivitypicker/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/blendmode(_:))*