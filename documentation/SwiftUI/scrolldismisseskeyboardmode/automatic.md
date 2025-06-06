# automatic

**Framework**: SwiftUI  
**Kind**: property

Determine the mode automatically based on the surrounding context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
static var automatic: ScrollDismissesKeyboardMode { get }
```

#### Discussion

By default, a [`TextEditor`](texteditor.md) is interactive while a [`List`](list.md) of scrollable content always dismiss the keyboard on a scroll, when linked against iOS 16 or later.

## See Also

- [static var immediately: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/immediately.md)
  Dismiss the keyboard as soon as scrolling starts.
- [static var interactively: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/interactively.md)
  Enable people to interactively dismiss the keyboard as part of the scroll operation.
- [static var never: ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode/never.md)
  Never dismiss the keyboard automatically as a result of scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolldismisseskeyboardmode/automatic)*