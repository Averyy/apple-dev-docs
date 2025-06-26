# foregroundColor(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the color of the foreground elements displayed by this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func foregroundColor(_ color: Color?) -> some View
```

#### Return Value

A view that uses the foreground color you supply.

## Parameters

- `color`: The foreground color to use when displaying this   view. Pass   to remove any custom foreground color and to allow   the system or the container to provide its own foreground color.   If a container-specific override doesn’t exist, the system uses   the primary color.

## See Also

- [func foregroundStyle<S>(S) -> some View](familyactivitypicker/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](familyactivitypicker/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](familyactivitypicker/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/foregroundcolor(_:))*