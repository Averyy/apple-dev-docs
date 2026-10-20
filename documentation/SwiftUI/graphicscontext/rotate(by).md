# rotate(by:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

Calling this method is equivalent to updating the context’s [`transform`](./transform.md) directly using the `angle` parameter:

```swift
transform = transform.rotated(by: angle.radians)
```

## Parameters

- `angle`: The amount to rotate.

## See Also

### Applying transforms
- [func scaleBy(x: CGFloat, y: CGFloat)](./scaleby%28x,y%29.md)
  Scales subsequent drawing operations by an amount in each dimension.
- [func translateBy(x: CGFloat, y: CGFloat)](./translateby%28x,y%29.md)
  Moves subsequent drawing operations by an amount in each dimension.
- [func concatenate(CGAffineTransform)](./concatenate%28_%29.md)
  Appends the given transform to the context’s existing transform.
- [var transform: CGAffineTransform](./transform.md)
  The current transform matrix, defining user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/rotate(by:))*