# position(x:y:)

**Framework**: FamilyControls  
**Kind**: method

Positions the center of this view at the specified coordinates in its parent’s coordinate space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func position(x: CGFloat = 0, y: CGFloat = 0) -> some View
```

#### Return Value

A view that fixes the center of this view at `x` and `y`.

#### Discussion

Use the `position(x:y:)` modifier to place the center of a view at a specific coordinate in the parent view using an `x` and `y` offset.

```swift
Text("Position by passing the x and y coordinates")
    .position(x: 175, y: 100)
    .border(Color.gray)
```

## Parameters

- `x`: The x-coordinate at which to place the center of this view.
- `y`: The y-coordinate at which to place the center of this view.

## See Also

- [func position(CGPoint) -> some View](familyactivitypicker/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func offset(CGSize) -> some View](familyactivitypicker/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func coordinateSpace<T>(name: T) -> some View](familyactivitypicker/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/position(x:y:))*