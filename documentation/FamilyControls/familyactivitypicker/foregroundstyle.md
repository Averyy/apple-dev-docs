# foregroundStyle(_:_:_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the primary, secondary, and tertiary levels of the foreground style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func foregroundStyle<S1, S2, S3>(_ primary: S1, _ secondary: S2, _ tertiary: S3) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
```

#### Return Value

A view that uses the given foreground styles.

#### Discussion

SwiftUI uses these styles when rendering child views that don’t have an explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the `SymbolRenderingMode/palette` rendering mode when you apply this modifier, if you don’t explicitly specify another mode.

## Parameters

- `primary`: The primary color or pattern to use when filling in   the foreground elements. To indicate a specific value, use    or  , or one of the gradient   types, like   . To set a   style that’s relative to the containing view’s style, use one of the   semantic styles, like  .
- `secondary`: The secondary color or pattern to use when   filling in the foreground elements.
- `tertiary`: The tertiary color or pattern to use when   filling in the foreground elements.

## See Also

- [func foregroundStyle<S>(S) -> some View](familyactivitypicker/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](familyactivitypicker/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundColor(Color?) -> some View](familyactivitypicker/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/foregroundstyle(_:_:_:))*