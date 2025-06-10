# translation(in:)

**Framework**: SwiftUI  
**Kind**: method

Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
func translation(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint?
```

#### Discussion

If the gesture recognizer does not implement a `translationInView:` method, returns nil.

## Parameters

- `coordinateSpace`: The SwiftUI coordinate space to convert to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/translation(in:))*