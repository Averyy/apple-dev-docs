# SiriTipView

**Framework**: App Intents  
**Kind**: struct

A SwiftUI view that displays the phrase someone uses to invoke an App Shortcut.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SiriTipView
```

#### Overview

Use a [`SiriTipView`](siritipview.md) to display the spoken phrase for the intent you specify. Include an instance of your intent when you create the view, and bind the view to a Boolean to handle the view’s presentation. The following example shows how to configure a button for a reorder intent and bind it to an `isVisible` variable.

```swift
SiriTipView(intent: ReorderIntent(), isVisible: $isVisible)
    .siriTipViewStyle(.black)
```

Note that you must use the [`AppIntent`](appintent.md) in an [`AppShortcut`](appshortcut.md). Otherwise this will display an empty view.

## Topics

### Creating the view
- [init<Intent>(intent: Intent, isVisible: Binding<Bool>?)](siritipview/init(intent:isvisible:).md)
  Creates a `SiriTipView` for the associated action that displays when the binding to a Boolean value is true .
### Implementing the view
- [var body: some View](siritipview/body-swift.property.md)
  The content and behavior of the view.
- [SiriTipView.Body](siritipview/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](siritipview/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [class SiriTipUIView](siritipuiview.md)
  A view that displays the phrase a person uses to invoke an App Shortcut.
- [struct SiriTipViewStyle](siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview)*