# interactively

**Framework**: SwiftUI  
**Kind**: property

Enable people to interactively dismiss the keyboard as part of the scroll operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
static var interactively: ScrollDismissesKeyboardMode { get }
```

#### Discussion

The software keyboard’s position tracks the gesture that drives the scroll operation if the gesture crosses into the keyboard’s area of the display. People can dismiss the keyboard by scrolling it off the display, or reverse the direction of the scroll to cancel the dismissal.

## See Also

- [static var automatic: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/automatic.md)
  Determine the mode automatically based on the surrounding context.
- [static var immediately: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/immediately.md)
  Dismiss the keyboard as soon as scrolling starts.
- [static var never: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/never.md)
  Never dismiss the keyboard automatically as a result of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolldismisseskeyboardmode/interactively)*