# NSGestureRecognizerRepresentableCoordinateSpaceConverter

**Framework**: SwiftUI  
**Kind**: struct

A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [`NSGestureRecognizerRepresentable`](nsgesturerecognizerrepresentable.md).

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
struct NSGestureRecognizerRepresentableCoordinateSpaceConverter
```

## Topics

### Instance Properties
- [var localLocation: CGPoint](nsgesturerecognizerrepresentablecoordinatespaceconverter/locallocation.md)
  The represented gesture recognizer’s current location in the coordinate space of the SwiftUI view it’s attached to.
- [var localTranslation: CGPoint?](nsgesturerecognizerrepresentablecoordinatespaceconverter/localtranslation.md)
  The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-translationInView:` selector.
- [var localVelocity: CGPoint?](nsgesturerecognizerrepresentablecoordinatespaceconverter/localvelocity.md)
  The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-velocityInView:` selector.
### Instance Methods
- [func convert(globalPoint: CGPoint, to: some CoordinateSpaceProtocol) -> CGPoint](nsgesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint:to:).md)
  Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [func location(in: some CoordinateSpaceProtocol) -> CGPoint](nsgesturerecognizerrepresentablecoordinatespaceconverter/location(in:).md)
  Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [func translation(in: some CoordinateSpaceProtocol) -> CGPoint?](nsgesturerecognizerrepresentablecoordinatespaceconverter/translation(in:).md)
  Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [func velocity(in: some CoordinateSpaceProtocol) -> CGPoint?](nsgesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:).md)
  Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

## See Also

- [protocol NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md)
  A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [struct NSGestureRecognizerRepresentableContext](nsgesturerecognizerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update a represented gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter)*