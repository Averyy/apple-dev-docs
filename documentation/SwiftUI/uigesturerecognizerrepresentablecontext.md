# UIGestureRecognizerRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update a represented gesture recognizer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct UIGestureRecognizerRepresentableContext<Representable> where Representable : UIGestureRecognizerRepresentable
```

## Topics

### Instance Properties
- [let converter: UIGestureRecognizerRepresentableCoordinateSpaceConverter](uigesturerecognizerrepresentablecontext/converter.md)
  A structure used to convert locations to/from coordinate spaces in the hierarchy of the associated SwiftUI view.
- [let coordinator: Representable.Coordinator](uigesturerecognizerrepresentablecontext/coordinator.md)
  The custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

## See Also

- [protocol UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md)
  A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [struct UIGestureRecognizerRepresentableCoordinateSpaceConverter](uigesturerecognizerrepresentablecoordinatespaceconverter.md)
  A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [`UIGestureRecognizerRepresentable`](uigesturerecognizerrepresentable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecontext)*