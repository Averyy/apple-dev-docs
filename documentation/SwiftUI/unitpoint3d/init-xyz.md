# init(x:y:z:)

**Framework**: SwiftUI  
**Kind**: init

Creates a 3D unit point with the specified offsets.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(x: CGFloat, y: CGFloat, z: CGFloat)
```

#### Discussion

Values outside the range `[0, 1]` project to points outside of a view.

## Parameters

- `x`: The normalized distance from the origin to the point in the   horizontal dimension.
- `y`: The normalized distance from the origin to the point in the   vertical dimension.
- `z`: The normalized distance from the origin to the point in the   depth dimension.

## See Also

- [init()](unitpoint3d/init.md)
  Creates a 3D unit point at the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unitpoint3d/init(x:y:z:))*