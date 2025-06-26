# overlay(_:in:fillStyle:)

**Framework**: FamilyControls  
**Kind**: method

Layers a shape that you specify in front of this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func overlay<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : Shape
```

#### Return Value

A view with the specified shape drawn in front of it.

#### Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol — like a `Rectangle`, `Circle`, or `Capsule` — in front of a view. Specify a `ShapeStyle` that’s used to fill the shape. For example, you can overlay the outline of one rectangle in front of another:

```swift
Rectangle()
    .frame(width: 200, height: 100)
    .overlay(.teal, in: Rectangle().inset(by: 10).stroke(lineWidth: 5))
```

The example above uses the `InsettableShape/inset(by:)` method to slightly reduce the size of the overlaid rectangle, and the `Shape/stroke(lineWidth:)` method to fill only the shape’s outline. This creates an inset border:

This modifier is a convenience method for layering a shape over a view. To handle the more general case of overlaying a `View` — or a stack of views — with control over the position, use `View/overlay(alignment:content:)` instead. To cover a view with a `ShapeStyle`, use `View/overlay(_:ignoresSafeAreaEdges:)`.

## Parameters

- `style`: A   that SwiftUI uses to the fill the shape   that you specify.
- `shape`: An instance of a type that conforms to   that   SwiftUI draws in front of the view.
- `fillStyle`: The   to use when drawing the shape.   The default style uses the nonzero winding number rule and   antialiasing.

## See Also

- [func foregroundStyle<S>(S) -> some View](familyactivitypicker/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](familyactivitypicker/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](familyactivitypicker/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func foregroundColor(Color?) -> some View](familyactivitypicker/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/overlay(_:in:fillstyle:))*