# UICanvasFeedbackGenerator

**Framework**: UIKit  
**Kind**: class

A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+

## Declaration

```swift
@MainActor
class UICanvasFeedbackGenerator
```

#### Overview

Use canvas feedback to indicate when a drawing event occurs, such as an object snapping to a guide or ruler. When using Apple Pencil Pro with a compatible iPad, this type of feedback can provide a tactile response.

The following code example shows how to use a pan gesture to drag a square, playing haptic feedback to indicate when the square aligns with a gridline on the canvas.

```swift
var gridlines: [Gridline] = []
var feedback = UICanvasFeedbackGenerator()

override func viewDidLoad() {
    super.viewDidLoad()
    configureGridlines()
    
    // Create a canvas feedback object and associate it with the view.
    feedback = UICanvasFeedbackGenerator(view: view)
    
    // Draw a basic square and add it to the view hierarchy.
    let center = CGPoint(x: view.center.x - 50, y: view.center.y - 50)
    let square = UIView(frame: CGRect(origin: center,
                                     size: CGSize(width: 100, height: 100)))
    square.backgroundColor = .tintColor
    view.addSubview(square)
    
    // Add a pan gesture to allow dragging the square.
    let panGesture = UIPanGestureRecognizer(target: self, action: #selector(dragSquare(_:)))
    square.isUserInteractionEnabled = true
    square.addGestureRecognizer(panGesture)
}

@objc
private func dragSquare(_ sender: UIPanGestureRecognizer) {
    guard let square = sender.view else { return }
    
    if sender.state == .began {
        // Prepare the feedback object.
        feedback.prepare()
    }

    // Move the square in response to a pan gesture.
    let distance = sender.translation(in: view)
    square.center = CGPoint(x: square.center.x + distance.x, y: square.center.y + distance.y)
    sender.setTranslation(CGPoint.zero, in: view)
    
    // Play canvas feedback if the square aligns with one of the gridlines.
    if square.aligned(gridlines: gridlines) {
        feedback.alignmentOccurred(at: sender.location(in: view))
    }
}
```

For more information, read [`Playing haptic feedback in your app`](https://developer.apple.com/documentation/ApplePencil/playing-haptic-feedback-in-your-app).

## Topics

### Reporting canvas events
- [func alignmentOccurred(at: CGPoint)](uicanvasfeedbackgenerator/alignmentoccurred(at:).md)
  Triggers feedback to indicate when an alignment occurs, such as snapping an object to a guide or ruler.
- [func pathCompleted(at: CGPoint)](uicanvasfeedbackgenerator/pathcompleted(at:).md)
  Triggers feedback to indicate path completion or shape recognition.

## Relationships

### Inherits From
- [UIFeedbackGenerator](uifeedbackgenerator.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md)
  Provide tactile feedback when people perform certain actions in your app.
- [class UIFeedbackGenerator](uifeedbackgenerator.md)
  The abstract superclass for all feedback generators.
- [class UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [class UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [class UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate a change in selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicanvasfeedbackgenerator)*