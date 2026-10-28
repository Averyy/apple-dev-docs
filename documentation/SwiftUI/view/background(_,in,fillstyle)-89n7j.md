# background(_:in:fillStyle:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the view’s background to a shape filled with a style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : Shape
```

**Other overloads**:

```swift
nonisolated
func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : InsettableShape
```

## Return Value

A view with the specified shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the [`Shape`](../shape.md) protocol behind a view. Specify the [`ShapeStyle`](../shapestyle.md) that’s used to fill the shape. For example, you can create a [`Path`](../path.md) that outlines a trapezoid:

```swift
let trapezoid = Path { path in
    path.move(to: .zero)
    path.addLine(to: CGPoint(x: 90, y: 0))
    path.addLine(to: CGPoint(x: 80, y: 50))
    path.addLine(to: CGPoint(x: 10, y: 50))
}
```

Then you can use that shape as a background for a [`Label`](../label.md):

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: trapezoid)
```

The [`teal`](../shapestyle/teal.md) color fills the shape:

![A screenshot of the flag icon and the word flag inside a trapezoid;](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-background-A@2x.png)

This modifier is a convenience method for placing a single shape behind a view. To create a background with other [`View`](../view.md) types — or with a stack of views — use [`background(alignment:content:)`](./background%28alignment,content%29.md) instead. To add a [`ShapeStyle`](../shapestyle.md) as a background, use [`background(_:ignoresSafeAreaEdges:)`](./background%28_,ignoressafeareaedges%29.md).

## Parameters

- `style`: A [`ShapeStyle`](../shapestyle.md) that SwiftUI uses to the fill the shape that you specify.
- `shape`: An instance of a type that conforms to [`Shape`](../shape.md) that SwiftUI draws behind the view.
- `fillStyle`: The [`FillStyle`](../fillstyle.md) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(_:in:fillstyle:)-89n7j)*