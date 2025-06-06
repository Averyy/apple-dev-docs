# rotate(by:)

**Framework**: SwiftUI  
**Kind**: method

Rotates subsequent drawing operations by an angle.

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
mutating func rotate(by angle: Angle)
```

#### Discussion

Calling this method is equivalent to updating the context’s [`transform`](graphicscontext/transform.md) directly using the `angle` parameter:

```swift
transform = transform.rotated(by: angle.radians)
```

## Parameters

- `angle`: The amount to rotate.

## See Also

- [func scaleBy(x: CGFloat, y: CGFloat)](graphicscontext/scaleby(x:y:).md)
  Scales subsequent drawing operations by an amount in each dimension.
- [func translateBy(x: CGFloat, y: CGFloat)](graphicscontext/translateby(x:y:).md)
  Moves subsequent drawing operations by an amount in each dimension.
- [func concatenate(CGAffineTransform)](graphicscontext/concatenate(_:).md)
  Appends the given transform to the context’s existing transform.
- [var transform: CGAffineTransform](graphicscontext/transform.md)
  The current transform matrix, defining user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/rotate(by:))*