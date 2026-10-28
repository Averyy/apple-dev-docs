# background(in:fillStyle:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the view’s background to a shape filled with the default background style.

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
func background<S>(in shape: S, fillStyle: FillStyle = FillStyle()) -> some View where S : Shape
```

**Other overloads**:

```swift
nonisolated
func background<S>(in shape: S, fillStyle: FillStyle = FillStyle()) -> some View where S : InsettableShape
```

## Return Value

A view with the specified shape drawn behind it.

## Discussion

This modifier behaves like [`background(_:in:fillStyle:)`](./background%28_,in,fillstyle%29.md), except that it always uses the [`background`](../shapestyle/background.md) shape style to fill the specified shape. For example, you can create a [`Path`](../path.md) that outlines a trapezoid:

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
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(in: trapezoid)
}
```

Without the background modifier, the fill color shows through the label. With the modifier, the label’s text and icon appear backed by a shape filled with a color that’s appropriate for light or dark appearance:

![A screenshot of a flag icon and the word flag inside a trapezoid; the](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-background-B@2x.png)

To create a background with other [`View`](../view.md) types — or with a stack of views — use [`background(alignment:content:)`](./background%28alignment,content%29.md) instead. To add a [`ShapeStyle`](../shapestyle.md) as a background, use [`background(_:ignoresSafeAreaEdges:)`](./background%28_,ignoressafeareaedges%29.md).

## Parameters

- `shape`: An instance of a type that conforms to [`Shape`](../shape.md) that SwiftUI draws behind the view using the [`background`](../shapestyle/background.md) shape style.
- `fillStyle`: The [`FillStyle`](../fillstyle.md) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(in:fillstyle:)-96bda)*