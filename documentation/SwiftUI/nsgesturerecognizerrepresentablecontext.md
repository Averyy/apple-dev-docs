# NSGestureRecognizerRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update a represented gesture recognizer.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
struct NSGestureRecognizerRepresentableContext<Representable> where Representable : NSGestureRecognizerRepresentable
```

## Topics

### Instance Properties
- [let converter: NSGestureRecognizerRepresentableCoordinateSpaceConverter](nsgesturerecognizerrepresentablecontext/converter.md)
  A structure used to convert locations to and from coordinate spaces in the hierarchy of the associated SwiftUI view.
- [let coordinator: Representable.Coordinator](nsgesturerecognizerrepresentablecontext/coordinator.md)
  The custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

## See Also

- [protocol NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md)
  A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [struct NSGestureRecognizerRepresentableCoordinateSpaceConverter](nsgesturerecognizerrepresentablecoordinatespaceconverter.md)
  A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [`NSGestureRecognizerRepresentable`](nsgesturerecognizerrepresentable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecontext)*