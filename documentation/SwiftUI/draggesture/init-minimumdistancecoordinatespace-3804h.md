# init(minimumDistance:coordinateSpace:)

**Framework**: SwiftUI  
**Kind**: init

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: CoordinateSpace = .local)
```

## Parameters

- `minimumDistance`: The minimum dragging distance for the gesture to   succeed.
- `coordinateSpace`: The coordinate space of the dragging gesture’s   location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-3804h)*