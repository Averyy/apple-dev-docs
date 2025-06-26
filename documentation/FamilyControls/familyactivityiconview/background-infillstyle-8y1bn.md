# background(in:fillStyle:)

**Framework**: FamilyControls  
**Kind**: method

Sets the view’s background to a shape filled with the default background style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func background<S>(in shape: S, fillStyle: FillStyle = FillStyle()) -> some View where S : Shape
```

#### Return Value

A view with the specified shape drawn behind it.

#### Discussion

This modifier behaves like `View/background(_:in:fillStyle:)`, except that it always uses the `ShapeStyle/background` shape style to fill the specified shape. For example, you can create a `Path` that outlines a trapezoid:

```swift
let trapezoid = Path { path in
    path.move(to: .zero)
    path.addLine(to: CGPoint(x: 90, y: 0))
    path.addLine(to: CGPoint(x: 80, y: 50))
    path.addLine(to: CGPoint(x: 10, y: 50))
}
```

Then you can use that shape as a background for a `Label`:

```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(in: trapezoid)
}
```

Without the background modifier, the fill color shows through the label. With the modifier, the label’s text and icon appear backed by a shape filled with a color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views — use `View/background(alignment:content:)` instead. To add a `ShapeStyle` as a background, use `View/background(_:ignoresSafeAreaEdges:)`.

## Parameters

- `shape`: An instance of a type that conforms to   that   SwiftUI draws behind the view using the    shape style.
- `fillStyle`: The   to use when drawing the shape.   The default style uses the nonzero winding number rule and   antialiasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/background(in:fillstyle:)-8y1bn)*