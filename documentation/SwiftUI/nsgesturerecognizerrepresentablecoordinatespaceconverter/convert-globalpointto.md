# convert(globalPoint:to:)

**Framework**: SwiftUI  
**Kind**: method

Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func convert(globalPoint: CGPoint, to coordinateSpace: some CoordinateSpaceProtocol = .local) -> CGPoint
```

#### Return Value

A point converted to the given `coordinateSpace`.

## Parameters

- `globalPoint`: The point in the global coordinate space.
- `coordinateSpace`: The SwiftUI coordinate space to convert to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint:to:))*