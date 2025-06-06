# offset(_:)

**Framework**: FamilyControls  
**Kind**: method

Offset this view by the horizontal and vertical amount specified in the offset parameter.

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
func offset(_ offset: CGSize) -> some View
```

#### Return Value

A view that offsets this view by `offset`.

#### Discussion

Use `offset(_:)` to shift the displayed contents by the amount specified in the `offset` parameter.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

```swift
Text("Offset by passing CGSize()")
    .border(Color.green)
    .offset(CGSize(width: 20, height: 25))
    .border(Color.gray)
```

## Parameters

- `offset`: The distance to offset this view.

## See Also

- [func position(CGPoint) -> some View](familyactivitypicker/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func coordinateSpace<T>(name: T) -> some View](familyactivitypicker/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/offset(_:))*