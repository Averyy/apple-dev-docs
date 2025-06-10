# init(minimumDistance:coordinateSpace:)

**Framework**: SwiftUI  
**Kind**: init

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(minimumDistance: CGFloat = 10, coordinateSpace: some CoordinateSpaceProtocol = .local)
```

## Parameters

- `minimumDistance`: The minimum dragging distance for the gesture to   succeed.
- `coordinateSpace`: The coordinate space of the dragging gesture’s   location.

## See Also

- [var minimumDistance: CGFloat](draggesture/minimumdistance.md)
  The minimum dragging distance before the gesture succeeds.
- [var coordinateSpace: CoordinateSpace](draggesture/coordinatespace.md)
  The coordinate space in which to receive location values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-8ffe5)*