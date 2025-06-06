# transform

**Framework**: SwiftUI  
**Kind**: property

The current transform matrix, defining user space coordinates.

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
var transform: CGAffineTransform { get set }
```

#### Discussion

Modify this matrix to transform content that you subsequently draw into the context. Changes that you make don’t affect existing content.

## See Also

- [func scaleBy(x: CGFloat, y: CGFloat)](graphicscontext/scaleby(x:y:).md)
  Scales subsequent drawing operations by an amount in each dimension.
- [func rotate(by: Angle)](graphicscontext/rotate(by:).md)
  Rotates subsequent drawing operations by an angle.
- [func translateBy(x: CGFloat, y: CGFloat)](graphicscontext/translateby(x:y:).md)
  Moves subsequent drawing operations by an amount in each dimension.
- [func concatenate(CGAffineTransform)](graphicscontext/concatenate(_:).md)
  Appends the given transform to the context’s existing transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/transform)*