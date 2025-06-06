# concatenate(_:)

**Framework**: SwiftUI  
**Kind**: method

Appends the given transform to the context’s existing transform.

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
mutating func concatenate(_ matrix: CGAffineTransform)
```

#### Discussion

Calling this method is equivalent to updating the context’s [`transform`](graphicscontext/transform.md) directly using the `matrix` parameter:

```swift
transform = matrix.concatenating(transform)
```

## Parameters

- `matrix`: A transform to append to the existing transform.

## See Also

- [func scaleBy(x: CGFloat, y: CGFloat)](graphicscontext/scaleby(x:y:).md)
  Scales subsequent drawing operations by an amount in each dimension.
- [func rotate(by: Angle)](graphicscontext/rotate(by:).md)
  Rotates subsequent drawing operations by an angle.
- [func translateBy(x: CGFloat, y: CGFloat)](graphicscontext/translateby(x:y:).md)
  Moves subsequent drawing operations by an amount in each dimension.
- [var transform: CGAffineTransform](graphicscontext/transform.md)
  The current transform matrix, defining user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/concatenate(_:))*