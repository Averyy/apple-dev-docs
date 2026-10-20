# UIGestureRecognizerRepresentableCoordinateSpaceConverter

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [`UIGestureRecognizerRepresentable`](./uigesturerecognizerrepresentable.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct UIGestureRecognizerRepresentableCoordinateSpaceConverter
```

## Topics

### Instance Properties
- [var localLocation: CGPoint](./uigesturerecognizerrepresentablecoordinatespaceconverter/locallocation.md)
  The represented gesture recognizer’s current location in the coordinate space of the SwiftUI view it’s attached to.
- [var localTranslation: CGPoint?](./uigesturerecognizerrepresentablecoordinatespaceconverter/localtranslation.md)
  The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to.
- [var localVelocity: CGPoint?](./uigesturerecognizerrepresentablecoordinatespaceconverter/localvelocity.md)
  The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to.
### Instance Methods
- [func convert(globalPoint: CGPoint, to: some CoordinateSpaceProtocol) -> CGPoint](./uigesturerecognizerrepresentablecoordinatespaceconverter/convert%28globalpoint,to%29.md)
  Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [func location(in: some CoordinateSpaceProtocol) -> CGPoint](./uigesturerecognizerrepresentablecoordinatespaceconverter/location%28in%29.md)
  Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space  of an ancestor of the view the gesture recognizer is attached to.
- [func translation(in: some CoordinateSpaceProtocol) -> CGPoint?](./uigesturerecognizerrepresentablecoordinatespaceconverter/translation%28in%29.md)
  Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [func velocity(in: some CoordinateSpaceProtocol) -> CGPoint?](./uigesturerecognizerrepresentablecoordinatespaceconverter/velocity%28in%29.md)
  Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

## See Also

### Adding UIKit gesture recognizers into SwiftUI view hierarchies
- [protocol UIGestureRecognizerRepresentable](./uigesturerecognizerrepresentable.md)
  A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [struct UIGestureRecognizerRepresentableContext](./uigesturerecognizerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update a represented gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter)*