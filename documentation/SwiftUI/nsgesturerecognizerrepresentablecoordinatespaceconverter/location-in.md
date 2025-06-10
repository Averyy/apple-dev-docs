# location(in:)

**Framework**: SwiftUI  
**Kind**: method

Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func location(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint
```

#### Return Value

The represrnted gesture recognizer’s current location converted into the given `coordinateSpace`.

## Parameters

- `coordinateSpace`: The SwiftUI coordinate space to convert to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/location(in:))*