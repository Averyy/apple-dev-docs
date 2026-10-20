# offsetBy(dx:dy:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a path constructed by translating all its points.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func offsetBy(dx: CGFloat, dy: CGFloat) -> Path
```

#### Return Value

A new copy of the path with the offset applied to all points.

## Parameters

- `dx`: The offset to apply in the horizontal axis.
- `dy`: The offset to apply in the vertical axis.

## See Also

### Transforming the path
- [func applying(CGAffineTransform) -> Path](./applying%28_%29.md)
  Returns a path constructed by applying the transform to all points of the path.
- [func trimmedPath(from: CGFloat, to: CGFloat) -> Path](./trimmedpath%28from,to%29.md)
  Returns a partial copy of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path/offsetby(dx:dy:))*