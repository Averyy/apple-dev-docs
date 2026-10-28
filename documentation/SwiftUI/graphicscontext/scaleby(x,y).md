# scaleBy(x:y:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

## Discussion

Calling this method is equivalent to updating the context’s [`transform`](./transform.md) directly using the given scale factors:

```swift
transform = transform.scaledBy(x: x, y: y)
```

## Parameters

- `x`: The amount to scale in the horizontal direction.
- `y`: The amount to scale in the vertical direction.

## See Also

### Applying transforms
- [func rotate(by: Angle)](./rotate%28by%29.md)
  Rotates subsequent drawing operations by an angle.
- [func translateBy(x: CGFloat, y: CGFloat)](./translateby%28x,y%29.md)
  Moves subsequent drawing operations by an amount in each dimension.
- [func concatenate(CGAffineTransform)](./concatenate%28_%29.md)
  Appends the given transform to the context’s existing transform.
- [var transform: CGAffineTransform](./transform.md)
  The current transform matrix, defining user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/scaleby(x:y:))*