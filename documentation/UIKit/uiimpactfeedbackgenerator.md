# UIImpactFeedbackGenerator

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A concrete feedback generator subclass that creates haptics to simulate physical impacts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIImpactFeedbackGenerator
```

```objc
@interface UIImpactFeedbackGenerator : UIFeedbackGenerator
```

#### Overview

Use impact feedback to indicate when an impact occurs. For example, you might trigger impact feedback when a user interface object collides with another object.

The following code example shows how to use a pan gesture to drag a square, playing haptic feedback to indicate when the square collides with the edge of its superview.

```swift
var feedback = UIImpactFeedbackGenerator()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Create an impact feedback object and associate it with the view.
    feedback = UIImpactFeedbackGenerator(view: view)
    
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

    // Play impact feedback if the square bumps into the edge of its superview.
    if square.hitEdge(of: view) {
        feedback.impactOccurred(intensity: 1, at: sender.location(in: view))
    }
}
```

For more information, read [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md).

## Topics

### Initializing the feedback generator
- [convenience init(style: UIImpactFeedbackGenerator.FeedbackStyle, view: UIView)](./uiimpactfeedbackgenerator/init%28style,view%29.md)
  Creates an impact feedback generator with the specified style and view.
- [UIImpactFeedbackGenerator.FeedbackStyle](./uiimpactfeedbackgenerator/feedbackstyle.md)
  The mass of the objects in the collision simulated by an impact feedback generator object.
- [init(style: UIImpactFeedbackGenerator.FeedbackStyle)](./uiimpactfeedbackgenerator/init%28style%29.md)
  Creates an impact feedback generator with the specified style.
### Reporting impacts
- [func impactOccurred()](./uiimpactfeedbackgenerator/impactoccurred%28%29.md)
  Triggers impact feedback.
- [func impactOccurred(intensity: CGFloat)](./uiimpactfeedbackgenerator/impactoccurred%28intensity%29.md)
  Triggers impact feedback with a specific intensity.
- [func impactOccurred(at: CGPoint)](./uiimpactfeedbackgenerator/impactoccurred%28at%29.md)
  Triggers impact feedback at the specified location.
- [func impactOccurred(intensity: CGFloat, at: CGPoint)](./uiimpactfeedbackgenerator/impactoccurred%28intensity,at%29.md)
  Triggers impact feedback with a specific intensity at the specified location.

## Relationships

### Inherits From
- [UIFeedbackGenerator](./uifeedbackgenerator.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIInteraction](./uiinteraction.md)

## See Also

### Haptic feedback
- [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md)
  Provide tactile feedback when people perform certain actions in your app.
- [class UIFeedbackGenerator](./uifeedbackgenerator.md)
  The abstract superclass for all feedback generators.
- [class UINotificationFeedbackGenerator](./uinotificationfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [class UISelectionFeedbackGenerator](./uiselectionfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [class UICanvasFeedbackGenerator](./uicanvasfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator)*