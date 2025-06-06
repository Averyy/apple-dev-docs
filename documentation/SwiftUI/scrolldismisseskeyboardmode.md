# ScrollDismissesKeyboardMode

**Framework**: SwiftUI  
**Kind**: struct

The ways that scrollable content can interact with the software keyboard.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
struct ScrollDismissesKeyboardMode
```

#### Overview

Use this type in a call to the [`scrollDismissesKeyboard(_:)`](view/scrolldismisseskeyboard(_:).md) modifier to specify the dismissal behavior of scrollable views.

## Topics

### Getting modes
- [static var automatic: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/automatic.md)
  Determine the mode automatically based on the surrounding context.
- [static var immediately: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/immediately.md)
  Dismiss the keyboard as soon as scrolling starts.
- [static var interactively: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/interactively.md)
  Enable people to interactively dismiss the keyboard as part of the scroll operation.
- [static var never: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/never.md)
  Never dismiss the keyboard automatically as a result of scrolling.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md)
  The way that scrollable content interacts with the software keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolldismisseskeyboardmode)*