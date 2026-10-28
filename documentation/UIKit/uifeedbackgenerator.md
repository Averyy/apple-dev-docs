# UIFeedbackGenerator

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The abstract superclass for all feedback generators.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIFeedbackGenerator
```

```objc
@interface UIFeedbackGenerator : NSObject
```

## Overview

Don’t subclass or create instances of this class yourself. Instead, instantiate one of the concrete feedback generator subclasses:

- [`UIImpactFeedbackGenerator`](./uiimpactfeedbackgenerator.md). Use impact feedback to indicate when an impact occurs. For example, you might trigger impact feedback when a user interface object collides with something or snaps into place.
- [`UISelectionFeedbackGenerator`](./uiselectionfeedbackgenerator.md). Use selection feedback to indicate a change in selection.
- [`UINotificationFeedbackGenerator`](./uinotificationfeedbackgenerator.md). Use notification feedback to indicate successes, failures, and warnings.
- [`UICanvasFeedbackGenerator`](./uicanvasfeedbackgenerator.md). Use canvas feedback to indicate when a drawing event occurs, such as an object snapping to a guide or ruler.

For more information, read [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md).

## Topics

### Initializing a feedback generator
- [convenience init(view: UIView)](./uifeedbackgenerator/init%28view%29.md)
  Creates a feedback generator and attaches it to the specified view.
- [init()](./uifeedbackgenerator/init%28%29.md)
  Creates a feedback generator.
### Preparing to generate feedback
- [func prepare()](./uifeedbackgenerator/prepare%28%29.md)
  Prepares the generator to trigger feedback.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UICanvasFeedbackGenerator](./uicanvasfeedbackgenerator.md)
- [UIImpactFeedbackGenerator](./uiimpactfeedbackgenerator.md)
- [UINotificationFeedbackGenerator](./uinotificationfeedbackgenerator.md)
- [UISelectionFeedbackGenerator](./uiselectionfeedbackgenerator.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIInteraction](./uiinteraction.md)

## See Also

### Haptic feedback
- [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md)
  Provide tactile feedback when people perform certain actions in your app.
- [class UIImpactFeedbackGenerator](./uiimpactfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [class UINotificationFeedbackGenerator](./uinotificationfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.
- [class UISelectionFeedbackGenerator](./uiselectionfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [class UICanvasFeedbackGenerator](./uicanvasfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifeedbackgenerator)*