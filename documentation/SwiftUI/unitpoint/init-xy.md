# init(x:y:)

**Framework**: SwiftUI  
**Kind**: init

Creates a unit point with the specified horizontal and vertical offsets.

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
init(x: CGFloat, y: CGFloat)
```

#### Discussion

Values outside the range `[0, 1]` project to points outside of a view.

## Parameters

- `x`: The normalized distance from the origin to the point in the   horizontal direction.
- `y`: The normalized distance from the origin to the point in the   vertical direction.

## See Also

- [init()](unitpoint/init.md)
  Creates a unit point at the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unitpoint/init(x:y:))*