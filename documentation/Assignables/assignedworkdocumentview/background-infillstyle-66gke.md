# background(_:in:fillStyle:)

**Framework**: Assignables  
**Kind**: method

Sets the view’s background to a shape filled with a style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : Shape
```

#### Return Value

A view with the specified shape drawn behind it.

#### Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol behind a view. Specify the `ShapeStyle` that’s used to fill the shape. For example, you can create a `Path` that outlines a trapezoid:

```None
let trapezoid = Path { path in
    path.move(to: .zero)
    path.addLine(to: CGPoint(x: 90, y: 0))
    path.addLine(to: CGPoint(x: 80, y: 50))
    path.addLine(to: CGPoint(x: 10, y: 50))
}
```

Then you can use that shape as a background for a `Label`:

```None
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: trapezoid)
```

The `ShapeStyle/teal` color fills the shape:

This modifier is a convenience method for placing a single shape behind a view. To create a background with other `View` types — or with a stack of views — use `View/background(alignment:content:)` instead. To add a `ShapeStyle` as a background, use `View/background(_:ignoresSafeAreaEdges:)`.

## Parameters

- `style`: A   that SwiftUI uses to the fill the shape   that you specify.
- `shape`: An instance of a type that conforms to   that   SwiftUI draws behind the view.
- `fillStyle`: The   to use when drawing the shape.   The default style uses the nonzero winding number rule and   antialiasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/background(_:in:fillstyle:)-66gke)*