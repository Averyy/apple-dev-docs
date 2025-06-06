# position(x:y:)

**Framework**: Journaling Suggestions  
**Kind**: method

Positions the center of this view at the specified coordinates in its parent’s coordinate space.

**Availability**:
- iOS 13.0+
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

```None
Text("Position by passing the x and y coordinates")
    .position(x: 175, y: 100)
    .border(Color.gray)
```

## Parameters

- `x`: The x-coordinate at which to place the center of this view.
- `y`: The y-coordinate at which to place the center of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/position(x:y:))*