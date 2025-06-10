# translation(in:)

**Framework**: SwiftUI  
**Kind**: method

Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func translation(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint?
```

#### Return Value

The represented gesture recognizer’s current translation converted to the given `coordinateSpace`, or `nil` if the represented gesture recognizer doesn’t respond to `-translationInView:` selector.

## Parameters

- `coordinateSpace`: The SwiftUI coordinate space to convert to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/translation(in:))*