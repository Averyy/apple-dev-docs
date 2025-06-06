# scaleBy(x:y:)

**Framework**: SwiftUI  
**Kind**: method

Scales subsequent drawing operations by an amount in each dimension.

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
mutating func scaleBy(x: CGFloat, y: CGFloat)
```

#### Discussion

Calling this method is equivalent to updating the context’s [`transform`](graphicscontext/transform.md) directly using the given scale factors:

```swift
transform = transform.scaledBy(x: x, y: y)
```

## Parameters

- `x`: The amount to scale in the horizontal direction.
- `y`: The amount to scale in the vertical direction.

## See Also

- [func rotate(by: Angle)](graphicscontext/rotate(by:).md)
  Rotates subsequent drawing operations by an angle.
- [func translateBy(x: CGFloat, y: CGFloat)](graphicscontext/translateby(x:y:).md)
  Moves subsequent drawing operations by an amount in each dimension.
- [func concatenate(CGAffineTransform)](graphicscontext/concatenate(_:).md)
  Appends the given transform to the context’s existing transform.
- [var transform: CGAffineTransform](graphicscontext/transform.md)
  The current transform matrix, defining user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/scaleby(x:y:))*